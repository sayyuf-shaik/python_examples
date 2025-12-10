import requests

resp = requests.get("http://api.github.com")

data = resp.text

# If we want only json data to be get

print(resp.json())

# Either we can convert then into json data later
import json

print(json.loads(data))



