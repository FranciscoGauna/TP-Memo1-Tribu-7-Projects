from bson.errors import InvalidId

from src.controller.projects import put_project, get_project, get_projects, post_project, delete_project
from src.logger import logger
from flask import request


def route(app):
    @app.route("/projects", methods=["POST"])
    def create_project():
        """
        Creates a project
        ---
        tags:
          - projects
        definitions:
            - schema:
                id: Project
                properties:
                    uid:
                        type: string
                        description: Unique internal id of the project
                    name:
                        type: string
                        description: The name of the project
                    description:
                        type: string
                        description: The description of the project
                    stage:
                        type: string
                        description: In what stage the process is now
                    project_leader:
                        type: string
                        description: A string that represents the id for the project leader in the resources module
                    tasks:
                        type: object
                        additionalProperties:
                            $ref: "#/definitions/Task"
                    estimated_hours:
                        type: float
                        description: How many man-hours we estimate the project is going to take
                    start_date:
                        type: Iso8601 compliant date string
                        description: At what date the project has started
                    end_date:
                        type: Iso8601 compliant date string
                        description: At what date the project is estimated to end
                example:
                    uid: 1
                    name: Modulo de Proyectos - PSA
                    description: Modulo de CRUD de proyectos de PSA
                    stage: Ongoing
                    project_leader: 2
                    tasks: {}
                    estimated_hours: 50
                    start_date: "2023-03-01"
                    end_date: "2023-07-01"
        description: Creates a projects
        responses:
          201:
            description: Successfully created a project
            schema:
              properties:
                id:
                  type: string
                  description: uid of the project that has been created
                  example: 649a7918e06715f5850b9a41
        """
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
            schema:
              properties:
                projects:
                  type: array
                  items:
                    $ref: "#/definitions/Project"
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
        parameters:
          - name: uid
            in: path
            description: The id of the project to search
            required: true
        responses:
          200:
            description: return a single project
            schema:
              properties:
                project:
                  $ref: "#/definitions/Project"
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
        description: Updates a project by id
        parameters:
          - name: project
            in: body
            schema:
                $ref: "#/definitions/Project"
        responses:
          200:
            description: updates a single project
        """
        put_project(uid, request.json)
        return {"message": "Successfully updated project"}, 200

    # Tiene endpoint en el nombre para evitar colision
    @app.route("/projects/<uid>", methods=["DELETE"])
    def delete_project_endpoint(uid):
        """
        Deletes a project by id
        ---
        tags:
          - projects
        description: Deletes a project by id
        responses:
          200:
            description: delete a single project
        """
        delete_project(uid)
        return {"message": "Successfully updated project"}, 200
