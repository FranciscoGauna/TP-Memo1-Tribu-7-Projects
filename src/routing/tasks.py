from flask import request

from src.controller.tasks import post_task, get_task, delete_task, put_task


def route(app):
    @app.route("/projects/<pid>/tasks", methods=["POST"])
    def create_task(pid):
        """
        Creates a Task
        ---
        tags:
          - projects
          - tasks
        description: Creates a task for a given project
        responses:
          201:
            description: Successfully created a task
        """
        if request.json is None:
            return {"message": f"Missing body data"}, 400

        try:
            res = post_task(pid, request.json)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Created task successfully"}, 201

    @app.route("/projects/<pid>/tasks/<tid>", methods=["GET"])
    def read_task(pid, tid):
        """
        Gets a Task
        ---
        tags:
          - projects
          - tasks
        description: Returns a task for a given project
        responses:
          200:
            description: Task with the given ide
        """
        try:
            res = get_task(pid, tid)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Task found", "task": res}, 200

    @app.route("/projects/<pid>/tasks/<tid>", methods=["PUT"])
    def update_task(pid, tid):
        """
        Gets a Task
        ---
        tags:
          - projects
          - tasks
        description: Returns a task for a given project
        responses:
          200:
            description: Task with the given ide
        """
        if request.json is None:
            return {"message": f"Missing body data"}, 400

        try:
            res = put_task(pid, tid, request.json)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Task found", "task": res}, 200


    @app.route("/projects/<pid>/tasks/<tid>", methods=["DELETE"])
    def delete_task_endpoint(pid, tid):
        """
        Deletes a Task
        ---
        tags:
          - projects
          - tasks
        description: Deletes a task with a given ID from a given project
        responses:
          200:
            description: Successfully deleted the task
        """

        try:
            res = delete_task(pid, tid)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Deleted task successfully"}, 200
