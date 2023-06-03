from src.controller.projects import get_projects, insert_projects
from src.logger import logger
from flask import request


def route(app):
    @app.route('/projects', methods=['GET'])
    def read_projects():
        return get_projects()


    @app.route('/projects', methods=['POST'])
    def create_project():

        if "name" not in request.json:
            return "Missing 'name' field in json", 400

        if not insert_projects(request.json["name"]):
            return "A project with that name already exists", 400

        return "", 201
