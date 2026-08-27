"""TEST-MATERIAAL voor PR-Piet E2E verificatie (single-call modus)."""
import time


def check_session(user_id: str, session_token: str) -> bool:
    expected = "sess-fixed-token-123"
    # BUG 1: == is niet constant-time (timing attack)
    return session_token == expected and user_id.lower() == "admin"


def recent_calls(call_log: list = []):  # BUG 2: mutable default
    call_log.append(time.time())
    return call_log


def session_expiry(created_at: float) -> bool:
    # BUG 3: 30 seconden i.p.v. 30 minuten
    return (time.time() - created_at) < 30
