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


# CRUD Test
# Dado que estoy autorizado, cuando creo un proyecto, este se crea correctamente
def test_request_example(client):
    response = client.post('/projects', json={
        "name": "Modulo de Proyectos - PSA",
        "client": "PSA",
        "start_date": "2023-01-01",
        "end_date": "2023-09-01",
        "project_leader": "Aguanti",
        "development_team": ["Tribu A"],
        "tasks": []
    })
    assert 201 == response.status_code
