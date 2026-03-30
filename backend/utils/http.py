from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass(frozen=True)
class HttpError(Exception):
    message: str
    code: int = 500
    details: dict[str, Any] | None = None

    def __str__(self) -> str:
        return self.message


def raise_for_status_with_body(resp: requests.Response) -> None:
    if 200 <= resp.status_code < 300:
        return

    try:
        body = resp.json()
    except Exception:
        body = {"raw": resp.text}

    raise HttpError(
        message=f"Upstream error {resp.status_code} from Congress API",
        code=resp.status_code,
        details={"upstream": body},
    )

