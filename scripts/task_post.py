import requests

url = "http://192.168.0.25:35000/"
pid = "649a8bc43dc4b5dfacfd4daa"
url_projects = url + "projects/" + pid + "/tasks"
res = requests.post(url_projects, json={
    "state": "Ongoing",
    "description": "Develop a minimum viable product",
    "name": "MVP",
    "start_date": "2023-01-02",
    "end_date_est": "2023-09-02",
    "hours_est": "900",
})
print(res.status_code)
print(res.content)
