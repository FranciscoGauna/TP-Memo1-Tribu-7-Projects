from flask import request

from src.controller.tasks import post_task, get_task, delete_task, put_task


def route(app):
    @app.route("/projects/<pid>/tasks", methods=["POST"])
    def create_task(pid):
        """
        Creates a Task
        ---
        tags:
          - tasks
        definitions:
            - schema:
                id: Task
                properties:
                    puid:
                       type: string
                       description: Id of the task, it's only unique inside a given project
                    name:
                       type: string
                       description: The name of the task
                    description:
                       type: string
                       description: The description of the task
                    state:
                       type: string
                       description: In what state the process is now
                    human_resource:
                       type: string
                       description: An id indicating who is assigned to the task
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
                    puid: 1
                    name: MVP
                    description: Tenemos que completar un producto minimo viable
                    stage: Ongoing
                    human_resource: 3
                    estimated_hours: 10
                    start_date: "2023-03-01"
                    end_date: "2023-05-01"
        description: Creates a task for a given project
        parameters:
          - name: task
            in: body
            schema:
                $ref: "#/definitions/Task"
        responses:
          201:
            description: Successfully created a task
            schema:
              properties:
                id:
                  type: string
                  description: ID of the task that has been created
                  example: 649a7918e06715f5850b9a41
        """
        if request.json is None:
            return {"message": f"Missing body data"}, 400

        try:
            res = post_task(pid, request.json)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"id": res, "message": f"Created task successfully"}, 201

    @app.route("/projects/<pid>/tasks/<tid>", methods=["GET"])
    def read_task(pid, tid):
        """
        Gets a Task
        ---
        tags:
          - tasks
        description: Returns a task for a given project
        parameters:
          - name: pid
            in: path
            description: The id of the project which contains the task
            required: true
          - name: tid
            in: path
            description: The id of the task to be deleted
            required: true
        responses:
          200:
            description: Task with the given id
            schema:
              properties:
                task:
                  $ref: "#/definitions/Task"
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
          - tasks
        description: Returns a task for a given project
        parameters:
          - name: task
            in: body
            schema:
                $ref: "#/definitions/Task"
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
          - tasks
        description: Deletes a task with a given ID from a given project
        parameters:
          - name: pid
            in: path
            description: The id of the project which contains the task
            required: true
          - name: tid
            in: path
            description: The id of the task to be deleted
            required: true
        responses:
          200:
            description: Successfully deleted the task
        """

        try:
            res = delete_task(pid, tid)
        except KeyError as e:
            return {"message": f"A key is missing {e}"}, 400

        return {"message": f"Deleted task successfully"}, 200
