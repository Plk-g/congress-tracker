from __future__ import annotations

import os

from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from utils.config import Settings
from routes.bills import bills_bp
from routes.members import members_bp


def create_app() -> Flask:
    load_dotenv()
    settings = Settings.from_env()

    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    if settings.frontend_origin:
        CORS(app, resources={r"/api/*": {"origins": [settings.frontend_origin]}})
    else:
        CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.get("/api/health")
    def health():
        return jsonify({"ok": True})

    @app.errorhandler(Exception)
    def handle_unexpected_error(err: Exception):
        # Keep error shape consistent for the frontend.
        status = getattr(err, "code", 500)
        return (
            jsonify(
                {
                    "error": {
                        "message": str(err),
                        "type": err.__class__.__name__,
                    }
                }
            ),
            status,
        )

    app.register_blueprint(bills_bp)
    app.register_blueprint(members_bp)

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5050"))
    app.run(host="0.0.0.0", port=port, debug=True)
