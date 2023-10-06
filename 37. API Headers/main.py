import requests
import secret
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USERNAME = secret.PIXELA_USER_NAME
PIXELA_TOKEN = secret.PIXELA_TOKEN
PIXELA_GRAPH_ID = "coding-hours"

HEADERS = {"X-USER-TOKEN": PIXELA_TOKEN}

def create_pixela_account() -> None:
    user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params, timeout=20)
    response.raise_for_status()
    print(response.text)

def delete_pixela_account() -> None:
    delete_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}"
    response = requests.delete(url=delete_endpoint, timeout=20, headers=HEADERS)
    response.raise_for_status()
    print(response.text)

def create_pixela_graph() -> None:
    graph_endpoint=f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
    graph_params = {
        "id": PIXELA_GRAPH_ID,
        "name": "Coding hours",
        "unit": "hours",
        "type": "float",
        "color": "sora",
        "timezone": "Europe/Warsaw"
    }

    response = requests.post(url=graph_endpoint,json=graph_params, timeout=20, headers=HEADERS)
    print(response.text)
    response.raise_for_status()

def create_pixela_pixel(pixel_data: float, date:str) -> None:
    create_pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"

    pixel_data = {
        "date": date,
        "quantity": str(pixel_data)
    }

    response = requests.post(url=create_pixel_endpoint, json=pixel_data, timeout=20, headers=HEADERS)

    print(response.text)
    response.raise_for_status()

def update_pixela_pixel(pixel_data: float, date:str) -> None:
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{date}"

    pixel_data = {
        "quantity": str(pixel_data)
    }

    response = requests.put(url=update_pixel_endpoint, json=pixel_data, timeout=20, headers=HEADERS)

    print(response.text)
    response.raise_for_status()

def delete_pixela_pixel(date:str) -> None:
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{date}"

    response = requests.delete(url=update_pixel_endpoint, timeout=20, headers=HEADERS)

    print(response.text)
    response.raise_for_status()


today = datetime.today()
strToday = today.strftime("%Y%m%d")
