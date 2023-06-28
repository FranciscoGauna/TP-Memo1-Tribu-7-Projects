import requests

url = "https://projects-backend-service.onrender.com/"
pid = "649b428a2f213ddb078f31bb"
url_projects = url + "projects/" + pid + "/tasks"
res = requests.post(url_projects, json={
    "state": "Ongoing",
    "description": "Develop a minimum viable product",
    "name": "MVP",
    "start_date": "2023-01-02",
    "end_date_est": "2023-09-02",
    "estimated_hours": "900",
})
print(res.status_code)
print(res.content)
