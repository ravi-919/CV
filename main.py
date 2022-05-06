import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

USER = 'ravi18'
PASSWORD = 'Remos@18'
TOKEN = 'hgmdsgaegy'

headers2 = {
    "Authorization": "Bearer hgmdsgaegy"
}

APP_ID = '3f60cc98'
APP_KEY = '53544fc76ea3ac1122a31a888c921e8d'

GENDER = 'male'
WEIGHT = 77
HEIGHT = 172.72
AGE = 25

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_input = input("Which exercises you did today?")

params = {
    "x-remote-user-id": 0
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}


exer_para = {
    "query": exercise_input,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}


today = datetime.now()
sheet_post_endpoint = 'https://api.sheety.co/e85a96f97550d4b253bce2e51a89c91e/copyOfMyWorkouts/workouts'

response = requests.post(url=exercise_endpoint, json=exer_para, headers=headers)
op = response.json()
print(op)

for i in op['exercises']:
    work_param = {
        "workout":
            {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%X"),
                "exercise": i['user_input'].title(),
                "duration": i['duration_min'],
                "calories": i['nf_calories'],

            }

    }

    response2 = requests.post(url=sheet_post_endpoint, headers=headers2, json=work_param)
    print(response2)