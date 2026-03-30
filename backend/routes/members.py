from __future__ import annotations

from flask import Blueprint, jsonify, request

from services.congress_api import CongressApiClient
from utils.config import Settings
from utils.http import HttpError


members_bp = Blueprint("members", __name__, url_prefix="/api")


def _parse_int(value: str | None, *, default: int, min_value: int, max_value: int) -> int:
    if value is None or value == "":
        return default
    try:
        parsed = int(value)
    except ValueError:
        raise HttpError(message=f"Invalid integer: {value}", code=400)
    if parsed < min_value or parsed > max_value:
        raise HttpError(message=f"Value out of range: {parsed}", code=400)
    return parsed


@members_bp.get("/members")
def get_members():
    settings = Settings.from_env()
    client = CongressApiClient(settings)

    limit = _parse_int(request.args.get("limit"), default=20, min_value=1, max_value=250)
    offset = _parse_int(request.args.get("offset"), default=0, min_value=0, max_value=1000000)

    data = client.get_members(limit=limit, offset=offset)
    return jsonify(data)

