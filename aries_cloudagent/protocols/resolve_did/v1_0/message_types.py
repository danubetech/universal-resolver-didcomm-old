"""Message types for DID resolution."""

PROTOCOL_URI = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/did_resolution/0.1"

RESOLVE = f"{PROTOCOL_URI}/resolve"
RESOLVE_RESULT = f"{PROTOCOL_URI}/resolve_result"

PROTOCOL_PACKAGE = "aries_cloudagent.protocols.resolve_did"

MESSAGE_TYPES = {
    RESOLVE: f"{PROTOCOL_PACKAGE}.messages.resolve_did.ResolveDid",
    RESOLVE_RESULT: f"{PROTOCOL_PACKAGE}.messages.resolve_did_result.ResolveDidResult"
}
