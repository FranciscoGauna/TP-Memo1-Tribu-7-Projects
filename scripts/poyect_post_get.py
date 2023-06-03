import requests

url = "http://192.168.0.25:35000/"
url_projects = url + "projects"
res = requests.post(url_projects, json={"name": "FooBar"})
print(res.status_code)
print(res.content)