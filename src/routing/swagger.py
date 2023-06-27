from flask import jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


def route(app):
    @app.route("/spec")
    def spec():
        return jsonify(swagger(app))

    # Call factory function to create our blueprint
    blueprint = get_swaggerui_blueprint(
        "/docs",  # Url input
        "/spec",  # Url with the json
        config={  # Swagger UI config overrides
            'app_name': "Projects"
        },
    )

    app.register_blueprint(blueprint)
