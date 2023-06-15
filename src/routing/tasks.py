from flask import request

from src.controller.tasks import post_task


def route(app):
    @app.route("/projects/<pid>/tasks", methods=["POST"])
    def create_task(pid):
        if request.json is None:
            return {"message": f"Missing body data"}, 400

        try:
            res = post_task(pid, request.json)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Created task successfully"}, 201
