"""Message types for DID resolution."""

from ...didcomm_prefix import DIDCommPrefix

SPEC_URI = (
    "https://github.com/hyperledger/aries-rfcs/tree/"
    "6509b84abaf5760a8ba1744c8078d513f28456db/features/"
    "0124-did-resolution-protocol"
)

PROTOCOL_URI = "https://didcomm.org/did_resolution/0.9"

RESOLVE = f"{PROTOCOL_URI}/resolve"
RESOLVE_RESULT = f"{PROTOCOL_URI}/resolve_result"
RESOLVE_PROBLEM_REPORT = f"{PROTOCOL_URI}/problem-report"

PROTOCOL_PACKAGE = "aries_cloudagent.protocols.resolve_did.v0_9"

MESSAGE_TYPES = DIDCommPrefix.qualify_all(
    {
        RESOLVE: f"{PROTOCOL_PACKAGE}.messages.resolve_did.ResolveDid",
        RESOLVE_RESULT: f"{PROTOCOL_PACKAGE}.messages.resolve_did_result.ResolveDidResult",
        RESOLVE_PROBLEM_REPORT: f"{PROTOCOL_PACKAGE}.messages.resolve_did_result.ResolveDIDProblemReport",
    }
)
