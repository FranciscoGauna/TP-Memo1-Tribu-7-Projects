import requests

url = "http://192.168.0.25:35000/"
url_projects = url + "projects"
res = requests.post(url_projects, json={
    "name": "Modulo de Proyectos - PSA",
    "description": "Modulo de CRUD de proyectos de PSA",
    "project_leader": 2,
    "stage": "Ongoing",
    "start_date": "2023-03-01",
    "end_date": "2023-07-01",
    "estimated_hours": 50,
    "tasks": {}
})
print(res.status_code)
print(res.content)
