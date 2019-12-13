"""Basic message admin routes."""

from aiohttp import web
from aiohttp_apispec import docs, request_schema

from marshmallow import fields, Schema

from ...connections.models.connection_record import ConnectionRecord
from ...storage.error import StorageNotFoundError

from .messages.resolve_did import ResolveDid


class ResolveDidSchema(Schema):
    """Request schema for sending a message."""

    did = fields.Str(description="DID",
                     example="did:sov:WRfXPg8dantKVubE3HX8pw")


@docs(tags=["resolvedid"], summary="Resolve a DID via a DID resolver")
@request_schema(ResolveDidSchema())
async def connections_resolve_did(request: web.BaseRequest):
    """
    Request handler to resolve a DID using a local or remote service like the
    uniresolver

    Args:
        request: aiohttp request object

    """
    context = request.app["request_context"]
    connection_id = request.match_info["id"]
    outbound_handler = request.app["outbound_message_router"]
    params = await request.json()

    try:
        connection = await ConnectionRecord.retrieve_by_id(context, connection_id)
    except StorageNotFoundError:
        raise web.HTTPNotFound()

    if connection.is_ready:
        msg = ResolveDid(did=params["did"])
        await outbound_handler(msg, connection_id=connection_id)

    # returning the actual response is thought to be done using webhooks, see
    # https://github.com/hyperledger/aries-cloudagent-python/blob/master/docs/deploymentModel.md
    return web.json_response({})


async def register(app: web.Application):
    """Register routes."""

    app.add_routes(
        [web.post("/connections/{id}/resolve-did", connections_resolve_did)]
    )
