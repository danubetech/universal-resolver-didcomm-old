"""Resolve DID message handler."""

import requests

from ....messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
    HandlerException
)

from ..messages.resolve_did import ResolveDid
from ..messages.resolve_did_result import ResolveDidResult


class ResolveDidHandler(BaseHandler):
    """Message handler class for resolve did messages."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Message handler logic for resolving a did.

        Args:
            context: request context
            responder: responder callback
        """
        self._logger.debug("ResolveDidHandler called with context %s", context)
        assert isinstance(context.message, ResolveDid)

        self._logger.info("Received resolve did: %s", context.message.did)

        # TODO: do I have to call a webhook here? Doesn't make much sense
        await responder.send_webhook(
            "resolve_did",
            {
                "connection_id": context.connection_record.connection_id,
                "message_id": context.message._id,
                "did": context.message.did,
                "state": "received",
            },
        )

        try:
            did_document = resolve_did(context.message.did)
        except Exception as err:
            raise HandlerException(str(err))
        else:
            reply_msg = ResolveDidResult(did_document=did_document)
            reply_msg.assign_thread_from(context.message)
            if "l10n" in context.message._decorators:
                reply_msg._decorators["l10n"] = context.message._decorators["l10n"]
            await responder.send_reply(reply_msg)


def resolve_did(did):
    """Resolve a DID using the uniresolver."""
    url = f"https://uniresolver.io/1.0/identifiers/{did}"
    response = requests.get(url)
    if response.ok:
        content = response.json()
        return content['didDocument']
    raise HandlerException(f"Failed to resolve DID using URL {url}")
