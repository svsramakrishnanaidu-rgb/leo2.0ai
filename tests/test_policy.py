"""Tests for reference policy helper; not end-to-end Android or API tests."""
import unittest
from datetime import datetime, timedelta, timezone

from leo_core.policy import ConsentGrant, Decision, Impact, ToolRequest, authorize


class ConsentPolicyTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 11, 6, 12, tzinfo=timezone.utc)
        self.grant = ConsentGrant(
            actor_id="user-a",
            resource_id="file-123",
            capabilities=frozenset({"document.read", "document.rename"}),
            expires_at=self.now + timedelta(minutes=15),
        )
        self.request = ToolRequest(
            actor_id="user-a",
            resource_owner_id="user-a",
            resource_id="file-123",
            capability="document.read",
            impact=Impact.READ,
        )

    def check(self, request=None, grant=None):
        return authorize(
            request or self.request,
            self.grant if grant is None else grant,
            now=self.now,
        )

    def test_valid_read_is_automatic(self):
        self.assertEqual(self.check(), Decision.AUTO)

    def test_missing_grant_is_denied(self):
        self.assertEqual(authorize(self.request, None, now=self.now), Decision.DENY)

    def test_wrong_owner_is_denied(self):
        other = ToolRequest("user-a", "user-b", "file-123", "document.read", Impact.READ)
        self.assertEqual(self.check(request=other), Decision.DENY)

    def test_wrong_resource_is_denied(self):
        other = ToolRequest("user-a", "user-a", "file-999", "document.read", Impact.READ)
        self.assertEqual(self.check(request=other), Decision.DENY)

    def test_wrong_capability_is_denied(self):
        other = ToolRequest("user-a", "user-a", "file-123", "document.delete", Impact.HIGH_IMPACT)
        self.assertEqual(self.check(request=other), Decision.DENY)

    def test_expired_consent_denied(self):
        old = ConsentGrant("user-a", "file-123", frozenset({"document.read"}), self.now)
        self.assertEqual(self.check(grant=old), Decision.DENY)

    def test_revoked_consent_denied(self):
        revoked = ConsentGrant("user-a", "file-123", frozenset({"document.read"}), self.now + timedelta(days=1), True)
        self.assertEqual(self.check(grant=revoked), Decision.DENY)

    def test_external_write_requests_fresh_approval(self):
        req = ToolRequest("user-a", "user-a", "file-123", "document.rename", Impact.EXTERNAL_WRITE)
        self.assertEqual(self.check(request=req), Decision.ASK)

    def test_high_impact_requests_fresh_approval(self):
        req = ToolRequest("user-a", "user-a", "file-123", "document.rename", Impact.HIGH_IMPACT)
        self.assertEqual(self.check(request=req), Decision.ASK)

    def test_forbidden_capability_denied_even_if_granted(self):
        capability = "silent_screen_capture"
        granted = ConsentGrant("user-a", "file-123", frozenset({capability}), self.now + timedelta(days=1))
        req = ToolRequest("user-a", "user-a", "file-123", capability, Impact.READ)
        self.assertEqual(self.check(request=req, grant=granted), Decision.DENY)

    def test_unknown_impact_denied(self):
        req = ToolRequest("user-a", "user-a", "file-123", "document.read", "unknown")  # type: ignore[arg-type]
        self.assertEqual(self.check(request=req), Decision.DENY)


if __name__ == "__main__":
    unittest.main()
