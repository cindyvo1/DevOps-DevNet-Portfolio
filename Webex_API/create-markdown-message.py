import requests
import json

access_token = 'ZWUwODQ2MGMtNTYwOS00NmY4LTk4ZTEtNmZjMjViZTk0NGIxMGRkOTBmNGQtNjdk_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNDVmNTlhMzAtZjQ5YS0xMWYwLWI5OTUtZWY0MWM4YTI1OTZj'
message = 'Hello **DevNet Associates**!!'

url = 'https://webexapis.com/v1/messages'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {
    'roomId': room_id,
    'markdown': message
}

res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))
