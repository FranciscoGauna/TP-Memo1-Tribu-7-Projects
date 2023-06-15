from flask import jsonify
from flask_swagger import swagger


def route(app):
    @app.route("/spec")
    def spec():
        return jsonify(swagger(app))
