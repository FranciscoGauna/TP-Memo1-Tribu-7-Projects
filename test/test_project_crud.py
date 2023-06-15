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
    "tasks": {}
}


project_b_json = {
    "name": "Modulo de Soporte - PSA",
    "client": "PSA",
    "start_date": "2023-01-01",
    "end_date": "2023-09-01",
    "project_leader": "Aguanti",
    "development_team": ["Tribu A"],
    "tasks": {}
}


# CRUD Test
# Dado que estoy autorizado, cuando creo un proyecto, entonces se crea correctamente
def test_project_create_one(client):
    response = client.post("/projects", json=project_a_json)
    assert response.status_code == 201


# Dado que creo un proyecto, cuando lo busco por ID, entonces muestra la info correctamente
def test_project_create_and_read_one(client):
    # Escenario
    response = client.post("/projects", json=project_a_json)
    assert response.status_code == 201
    uid = response.json["id"]

    # Cuando
    response = client.get(f"/projects/{uid}")
    project = response.json["project"]

    # Entonces
    project.pop("uid")
    assert project == project_a_json


# Dado que creo un proyecto, cuando lo modifico por ID, entonces muestra la info correctamente
def test_project_create_and_update_one(client):
    # Escenario
    response = client.post("/projects", json=project_a_json)
    assert 201 == response.status_code
    uid = response.json["id"]

    # Cuando
    client.put(f"/projects/{uid}", json=project_b_json)

    # Entonces
    response = client.get(f"/projects/{uid}")
    project = response.json["project"]
    project.pop("uid")
    assert project == project_b_json


# Dado que no existe un proyecto, cuando lo busco por ID, entonces devuelve 404
def test_project_read_one_doesnt_exist(client):
    # Escenario
    uid = "012345678901234567890123"

    # Cuando
    response = client.get(f"/projects/{uid}")

    # Entonces
    assert response.status_code == 404


# Dado que estoy creo un proyecto, cuando lo borro, entonces no se puede encontrar
def test_project_create_delete_one(client):
    # Escenario
    response = client.post("/projects", json=project_a_json)
    assert response.status_code == 201
    uid = response.json["id"]

    # Cuando
    client.delete(f"/projects/{uid}")

    # Entonces
    response = client.get(f"/projects/{uid}")
    assert response.status_code == 404

