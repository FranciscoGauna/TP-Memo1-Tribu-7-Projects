from src.controller.projects import get_projects, insert_projects
from src.logger import logger
from flask import request


def route(app):
    @app.route('/projects', methods=['GET'])
    def read_projects():
        return {'projects': get_projects()}


    @app.route('/projects', methods=['POST'])
    def create_project():

        try:
            insert_projects(
                request.json["name"],
                request.json["client"],
                request.json["start_date"],
                request.json["end_date"],
                request.json["project_leader"],
                request.json["development_team"],
                request.json["tasks"],
                request.json["risks"]
            )
        except KeyError as e:
            return f"A key is missing {e}", 400

        return "", 201
