import pytest
from src.app import create_app


@pytest.fixture()
def app():
    yield create_app()



@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


project_a_json = {
    "name": "Modulo de Proyectos - PSA",
    "client": "PSA",
    "start_date": "2023-01-01",
    "end_date": "2023-09-01",
    "project_leader": "Aguanti",
    "development_team": ["Tribu A"],
    "tasks": []
}

task_a_json = {
    "id": "1",
    "state": "Ongoing",
    "name": "MVP",
    "start_date": "2023-01-02",
    "end_date_est": "2023-09-02",
    "hours_est": "900"
}


project_b_json = {
    "name": "Modulo de Proyectos - PSA",
    "client": "PSA",
    "start_date": "2023-01-01",
    "end_date": "2023-09-01",
    "project_leader": "Aguanti",
    "development_team": ["Tribu A"],
    "tasks": [task_a_json]
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
def test_project_task_create_read_one(client):
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
