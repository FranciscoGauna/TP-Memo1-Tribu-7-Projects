from flask import Flask
from src.conf import config
from src.routing import apply_routes


def run_app():
    app = Flask("TP-Memo1-Projects")
    app.config.from_mapping(config)
    apply_routes(app)
    app.run(host=config["HOST"], port=config["PORT"], load_dotenv=False)
