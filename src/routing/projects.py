from src.controller.projects import get_projects, insert_projects
from src.logger import logger
from flask import request


def route(app):
    @app.route('/projects', methods=['GET'])
    def read_projects():
        """
        Returns a list of all projects
        ---
        tags:
          - projects
        description: Returns a list of all projects
        responses:
          200:
            description: list of projects
        """
        return {'projects': get_projects()}

    @app.route('/projects', methods=['POST'])
    def create_project():
        if request.json is None:
            return {"message": f"Missing body data"}, 400

        try:
            res = insert_projects(request.json)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Created object successfully", "id": f"{res}"}, 201
