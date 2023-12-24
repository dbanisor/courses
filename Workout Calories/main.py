import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv("environment.env")

today = datetime.now()
DATE = today.strftime("%x")
HOUR = today.strftime("%X")


NUTRITION_APP_ID = os.environ.get("NUTRINIONIX_APP_ID")
NUTRITION_APP_KEY = os.environ.get("NUTRINIONIX_APP_KEY")
NUTRITION_API_ENDPOINT = os.environ.get("NUTRITIONIX_API_ENDPOINT")
NUTRITION_USER_ID = os.environ.get("NUTRITIONIX_USER_ID")

SHEETY_API_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

nutritionix_headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_APP_KEY,
    "x-remote-user-id": NUTRITION_USER_ID,
}

nutritionix_parameters = {
    "query": input("Tell me which exercise you did: "),
}

response = requests.post(url=NUTRITION_API_ENDPOINT, headers=nutritionix_headers, json=nutritionix_parameters)
exercise_type = (response.json()["exercises"][0]["name"]).title()
exercise_duration = response.json()["exercises"][0]["duration_min"]
exercise_calories = response.json()["exercises"][0]["nf_calories"]

# print(response.text)

params_exercise = {
    "workout": {
        "date": DATE,
        "time": HOUR,
        "exercise": exercise_type,
        "duration": exercise_duration,
        "calories": exercise_calories,
    }
}
bearer = os.environ.get("BEARER_TOKEN")

exercise_header = {
    "Content-Type": "application/json",
    "Authorization": bearer,
}

new_workout = requests.post(url=SHEETY_API_ENDPOINT, json=params_exercise, headers=exercise_header)
print(new_workout.text)
















