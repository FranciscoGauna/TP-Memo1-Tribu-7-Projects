from src.service.tasks import save_task, remove_task, retrieve_task


def post_task(pid, task):
    return save_task(pid, task)


def get_task(pid, tid):
    return retrieve_task(pid, tid)


def put_task(pid, tid, task):
    save_task(pid, task, tid)


def delete_task(pid, tid):
    remove_task(pid, tid)
