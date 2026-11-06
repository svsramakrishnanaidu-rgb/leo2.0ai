"""Reference deterministic authorization for scoped LEO 2.0 operations.

This pure Python reference demonstrates AUTO / ASK / DENY, but it is NOT an
authentication implementation, production authorization service, Android
permission broker, or integrated API endpoint. Integrators must verify the
actor server-side, storage ownership and consent provenance independently.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum


class Decision(str, Enum):
    AUTO = "AUTO"
    ASK = "ASK"
    DENY = "DENY"


class Impact(str, Enum):
    READ = "read"
    PREVIEW = "local_preview"
    EXTERNAL_WRITE = "external_write"
    HIGH_IMPACT = "high_impact"


@dataclass(frozen=True)
class ConsentGrant:
    """An illustrative, already-authenticated consent record."""

    actor_id: str
    resource_id: str
    capabilities: frozenset[str]
    expires_at: datetime
    revoked: bool = False


@dataclass(frozen=True)
class ToolRequest:
    """Caller and ownership fields must be populated by trusted services."""

    actor_id: str
    resource_owner_id: str
    resource_id: str
    capability: str
    impact: Impact


FORBIDDEN_CAPABILITIES = frozenset({
    "unrestricted_cross_app_accessibility",
    "silent_screen_capture",
    "collect_passwords_or_otps",
    "unbounded_private_storage_access",
})


def authorize(
    request: ToolRequest,
    grant: ConsentGrant | None,
    *,
    now: datetime | None = None,
) -> Decision:
    """Fail closed. Any external side effect requires visible approval."""
    if now is None:
        now = datetime.now(timezone.utc)
    if now.tzinfo is None:
        return Decision.DENY

    if not request.actor_id or not request.resource_owner_id or not request.resource_id:
        return Decision.DENY
    if not request.capability or not isinstance(request.impact, Impact):
        return Decision.DENY
    if request.capability in FORBIDDEN_CAPABILITIES:
        return Decision.DENY
    if request.actor_id != request.resource_owner_id:
        return Decision.DENY
    if grant is None or grant.revoked:
        return Decision.DENY
    if grant.actor_id != request.actor_id or grant.resource_id != request.resource_id:
        return Decision.DENY
    if request.capability not in grant.capabilities:
        return Decision.DENY
    if grant.expires_at.tzinfo is None or grant.expires_at <= now:
        return Decision.DENY
    if request.impact in (Impact.EXTERNAL_WRITE, Impact.HIGH_IMPACT):
        return Decision.ASK
    if request.impact in (Impact.READ, Impact.PREVIEW):
        return Decision.AUTO
    return Decision.DENY
