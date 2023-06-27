import pytest
from src.app import create_app


@pytest.fixture()
def app():
    yield create_app()


@pytest.fixture()
def client(app):
    return app.test_client()


project_a_json = {
    "name": "Modulo de Proyectos - PSA",
    "description": "Modulo de CRUD de proyectos de PSA",
    "project_leader": 2,
    "stage": "Ongoing",
    "start_date": "2023-03-01",
    "end_date": "2023-07-01",
    "estimated_hours": 50,
    "tasks": {}
}

task_a_json = {
    "state": "Ongoing",
    "name": "MVP",
    "start_date": "2023-01-02",
    "end_date_est": "2023-09-02",
    "hours_est": "900"
}

task_b_json = {
    "state": "Finished",
    "name": "MVP",
    "start_date": "2023-01-02",
    "end_date_est": "2023-09-02",
    "hours_est": "24"
}

task_c_json = {
    "state": "Finished",
    "name": "Amigos",
    "start_date": "2023-01-02",
    "end_date_est": "2023-09-02",
    "hours_est": "24"
}

project_b_json = {
    "name": "Modulo de Proyectos - PSA",
    "description": "Modulo de CRUD de proyectos de PSA",
    "project_leader": 2,
    "stage": "Ongoing",
    "start_date": "2023-03-01",
    "end_date": "2023-07-01",
    "estimated_hours": 50,
    "tasks": {"1": task_a_json, "2": task_c_json}
}


# Dado que creo un proyecto, cuando le agrego una tarea, entonces se agrega correctamente
def test_project_task_create_one(client):
    # Escenario
    response = client.post("/projects", json=project_a_json)
    assert response.status_code == 201
    uid = response.json["id"]

    # Cuando
    response = client.post(f"/projects/{uid}/tasks", json=task_a_json)

    # Entonces
    assert response.status_code == 201


# Dado que creo un proyecto y agrego una tarea, cuando leo las tareas, entonces esta correctamente
def test_project_task_create_read_project_one(client):
    # Escenario
    response = client.post("/projects", json=project_a_json)
    assert response.status_code == 201
    uid = response.json["id"]
    response = client.post(f"/projects/{uid}/tasks", json=task_a_json)
    assert response.status_code == 201

    # Cuando
    response = client.get(f"/projects/{uid}")
    project = response.json["project"]

    # Entonces
    assert len(project['tasks']) == 1


# Dado que creo un proyecto y agrego una tarea, cuando leo esa tarea, entonces está la information correcta
def test_project_task_create_read_one(client):
    # Escenario
    response = client.post("/projects", json=project_a_json)
    assert response.status_code == 201
    uid = response.json["id"]
    response = client.post(f"/projects/{uid}/tasks", json=task_a_json)
    assert response.status_code == 201
    tid = response.json["id"]

    # Cuando
    response = client.get(f"/projects/{uid}/tasks/{tid}")
    task = response.json["task"]

    # Entonces
    assert response.status_code == 200
    assert task == task_a_json


# Dado que creo un proyecto y agrego una tarea, cuando modifico esa tarea, entonces está la information correcta
def test_project_task_create_put_read_one(client):
    # Escenario
    response = client.post("/projects", json=project_a_json)
    assert response.status_code == 201
    uid = response.json["id"]
    response = client.post(f"/projects/{uid}/tasks", json=task_a_json)
    assert response.status_code == 201
    tid = response.json["id"]
    response = client.put(f"/projects/{uid}/tasks/{tid}", json=task_b_json)
    assert response.status_code == 200

    # Cuando
    response = client.get(f"/projects/{uid}/tasks/{tid}")
    task = response.json["task"]

    # Entonces
    assert response.status_code == 200
    assert task == task_b_json


# Dado que creo un proyecto con una tarea, cuando borros esa tarea, entonces no esta mas la tarea
def test_project_task_create_delete_one(client):
    # Escenario
    response = client.post("/projects", json=project_b_json)
    assert response.status_code == 201
    uid = response.json["id"]

    # Cuando
    response = client.delete(f"/projects/{uid}/tasks/1", json=task_a_json)
    assert response.status_code == 200

    # Entonces
    response = client.get(f"/projects/{uid}")
    project = response.json["project"]
    assert len(project['tasks']) == 1
