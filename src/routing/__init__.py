import src.routing.projects
import src.routing.tasks
import src.routing.swagger


def apply_routes(app):
    src.routing.projects.route(app)
    src.routing.tasks.route(app)
    src.routing.swagger.route(app)
