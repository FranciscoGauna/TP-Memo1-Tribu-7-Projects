from src.service.tasks import save_task


def post_task(pid, task):
    save_task(pid, task)
