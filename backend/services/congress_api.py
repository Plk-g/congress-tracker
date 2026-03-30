from __future__ import annotations

from typing import Any

import requests

from utils.config import Settings
from utils.http import HttpError, raise_for_status_with_body


class CongressApiClient:
    def __init__(self, settings: Settings):
        self._settings = settings

    def _require_key(self) -> str:
        if not self._settings.congress_api_key:
            raise HttpError(
                message="Missing CONGRESS_API_KEY. Set it in backend/.env (or workspace .env) before calling the API.",
                code=500,
            )
        return self._settings.congress_api_key

    def get_bills(
        self,
        *,
        limit: int,
        offset: int,
        q: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> dict[str, Any]:
        # Congress API supports query params; we keep them flexible and pass through.
        params: dict[str, Any] = {
            "api_key": self._require_key(),
            "format": "json",
            "limit": limit,
            "offset": offset,
        }
        if q:
            params["q"] = q
        if from_date:
            params["fromDateTime"] = from_date
        if to_date:
            params["toDateTime"] = to_date

        resp = requests.get(f"{self._settings.base_url}/bill", params=params, timeout=20)
        raise_for_status_with_body(resp)
        return resp.json()

    def get_bill_detail(self, *, congress: str, bill_type: str, bill_number: str) -> dict[str, Any]:
        params = {"api_key": self._require_key(), "format": "json"}
        url = f"{self._settings.base_url}/bill/{congress}/{bill_type}/{bill_number}"
        resp = requests.get(url, params=params, timeout=20)
        raise_for_status_with_body(resp)
        return resp.json()

    def get_members(self, *, limit: int, offset: int) -> dict[str, Any]:
        params = {
            "api_key": self._require_key(),
            "format": "json",
            "limit": limit,
            "offset": offset,
        }
        resp = requests.get(f"{self._settings.base_url}/member", params=params, timeout=20)
        raise_for_status_with_body(resp)
        return resp.json()

