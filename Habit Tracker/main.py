import requests
from datetime import datetime

USERNAME = "dbanisor87"
TOKEN = "kjfiy34of934ui498#($*"
pixela_endpoint = "https://pixe.la/v1/users"
ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime.now()

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you spend coding today? "),
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)

update_params = {
    "quantity": "150",
}
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_pixel_endpoint, json=update_params,headers=headers)
# print(response.text)
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)


