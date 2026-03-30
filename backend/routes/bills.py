from __future__ import annotations

from flask import Blueprint, jsonify, request

from services.congress_api import CongressApiClient
from utils.config import Settings
from utils.http import HttpError


bills_bp = Blueprint("bills", __name__, url_prefix="/api")


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


@bills_bp.get("/bills")
def get_bills():
    settings = Settings.from_env()
    client = CongressApiClient(settings)

    limit = _parse_int(request.args.get("limit"), default=20, min_value=1, max_value=250)
    offset = _parse_int(request.args.get("offset"), default=0, min_value=0, max_value=1000000)

    q = request.args.get("q") or None
    from_date = request.args.get("fromDate") or None
    to_date = request.args.get("toDate") or None

    data = client.get_bills(limit=limit, offset=offset, q=q, from_date=from_date, to_date=to_date)
    return jsonify(data)


@bills_bp.get("/bill/<congress>/<bill_type>/<bill_number>")
def get_bill_detail(congress: str, bill_type: str, bill_number: str):
    settings = Settings.from_env()
    client = CongressApiClient(settings)
    data = client.get_bill_detail(congress=congress, bill_type=bill_type, bill_number=bill_number)
    return jsonify(data)

