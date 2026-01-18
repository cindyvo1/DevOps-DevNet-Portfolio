import requests
import json

access_token = 'ZWUwODQ2MGMtNTYwOS00NmY4LTk4ZTEtNmZjMjViZTk0NGIxMGRkOTBmNGQtNjdk_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'
url = 'https://webexapis.com/v1/people'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {
    'email': 'voccm@hotmail.com'
}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))
