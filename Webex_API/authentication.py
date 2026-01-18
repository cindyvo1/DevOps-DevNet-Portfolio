import requests
import json

# 1) Vul hier je Webex personal access token in tussen de quotes
access_token = 'ZWUwODQ2MGMtNTYwOS00NmY4LTk4ZTEtNmZjMjViZTk0NGIxMGRkOTBmNGQtNjdk_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'

# 2) Dit is de URL om je eigen gegevens op te vragen
url = 'https://webexapis.com/v1/people/me'

# 3) Headers met je token
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

# 4) GET-request sturen
res = requests.get(url, headers=headers)

# 5) Mooi geformatteerd JSON printen
print(json.dumps(res.json(), indent=4))

