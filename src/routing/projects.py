from bson.errors import InvalidId

from src.controller.projects import put_project, get_project, get_projects, post_project, delete_project
from src.logger import logger
from flask import request


def route(app):
    @app.route("/projects", methods=["POST"])
    def create_project():
        if request.json is None:
            return {"message": f"Missing body data"}, 400

        try:
            res = post_project(request.json)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Created object successfully", "id": f"{res}"}, 201

    @app.route("/projects", methods=["GET"])
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
        return {"projects": get_projects()}

    @app.route("/projects/<uid>", methods=["GET"])
    def read_project(uid):
        """
        Returns a project by id
        ---
        tags:
          - projects
        description: Returns a project by id
        responses:
          200:
            description: return a single project
        """
        try:
            return {"project": get_project(uid)}, 200
        except InvalidId:
            return {"message": "Wrong ID format"}, 400
        except IndexError:
            return {"message": "ID not found"}, 404

    @app.route("/projects/<uid>", methods=["PUT"])
    def update_project(uid):
        """
        Updates a project by id
        ---
        tags:
          - projects
        description: Returns a project by id
        responses:
          200:
            description: return a single project
        """
        put_project(uid, request.json)
        return {"message": "Successfully updated project"}, 200

    # Tiene endpoint en el nombre para evitar colision
    @app.route("/projects/<uid>", methods=["DELETE"])
    def delete_project_endpoint(uid):
        """
        Updates a project by id
        ---
        tags:
          - projects
        description: Returns a project by id
        responses:
          200:
            description: return a single project
        """
        delete_project(uid)
        return {"message": "Successfully updated project"}, 200
