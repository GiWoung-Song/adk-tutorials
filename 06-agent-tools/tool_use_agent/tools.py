from datetime import datetime


def now_utc() -> dict:
    """현재 시각(UTC 기준 ISO 문자열)을 반환합니다."""
    return {"utc_now": datetime.utcnow().isoformat()}
