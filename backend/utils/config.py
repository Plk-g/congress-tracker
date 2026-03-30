from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    congress_api_key: str | None
    base_url: str
    frontend_origin: str | None

    @staticmethod
    def from_env() -> "Settings":
        return Settings(
            congress_api_key=os.getenv("CONGRESS_API_KEY"),
            base_url=os.getenv("CONGRESS_API_BASE_URL", "https://api.congress.gov/v3"),
            frontend_origin=os.getenv("FRONTEND_ORIGIN"),
        )

