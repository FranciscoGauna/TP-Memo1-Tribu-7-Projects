from flask import Flask
from flask_cors import CORS
from src.conf import config
from src.routing import apply_routes


def create_app():
    app = Flask("TP-Memo1-Projects")
    app.config.from_mapping(config)
    CORS(app)
    apply_routes(app)
    return app


def run_app(app):
    app.run(host=config["HOST"], port=config["PORT"], load_dotenv=False)
