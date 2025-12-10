import requests


## Query string parameters are part of the url querying that can customize the get request

resp = requests.get(
    "https://api.github.com/search/repositories",
    params={
        "q": "language:python",
        "sort": "stars",
        "order": "desc"
    }
)

print(resp.json())

