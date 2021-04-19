import requests


r = requests.get("https://prolificsys.com")
print(r.status_code)
