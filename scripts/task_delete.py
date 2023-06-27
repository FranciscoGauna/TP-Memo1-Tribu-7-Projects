import requests

url = "https://projects-backend-service.onrender.com/"
pid = "649b428a2f213ddb078f31bb"
tid = "649b42a02f213ddb078f31bc"
url_projects = url + "projects/" + pid + "/tasks/" + tid
res = requests.delete(url_projects)
print(res.status_code)
print(res.content)
