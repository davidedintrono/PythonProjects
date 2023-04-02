import requests
import datetime as dt

USERNAME = "your_username"
TOKEN = "your_token_here"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_request = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)

ADD_PIXEL_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH_ID}'
today = dt.datetime.now().strftime("%Y%m%d")
pixel_configs = {
    "date": today,
    "quantity": "10.4",
}

pixel_request = requests.post(url=ADD_PIXEL_ENDPOINT, json=pixel_configs, headers=headers)

pixel_date = "20200101"
UPDATE_PIXEL_ENDPOINT = f"{ADD_PIXEL_ENDPOINT}/{pixel_date}"
new_pixel_configs = {
    "quantity": "11.4",
}
update_pixel_request = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=new_pixel_configs, headers=headers)