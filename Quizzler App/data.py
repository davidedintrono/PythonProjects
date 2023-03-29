import requests as r

params = {
    "amount": 10,
    "type": "boolean"
}

response = r.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()["results"]

