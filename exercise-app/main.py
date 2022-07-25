from datetime import datetime
from urllib import response
import requests

API=""
NUTRIENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETENDPOINT="https://api.sheety.co/ccb42fda075725a38585e09ec2032c0b/myWorkouts/workouts"
APPID=""
params={
    "query":"ran 3 miles",
    "gender":"male",
    "weight_kg":80,
    "height_cm":180,
    "age":22
}

headers={
    "x-app-id":APPID,
    "x-app-key":API
}

response=requests.post(NUTRIENDPOINT,json=params,headers=headers)

response.raise_for_status()

result=response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    # #No Authentication  
    # sheet_response = requests.post(SHEETENDPOINT, json=sheet_inputs)
    
    # #Basic Authentication
    # sheet_response = requests.post(
    #   SHEETENDPOINT, 
    #   json=sheet_inputs, 
    #   auth=(
    #       YOUR USERNAME, 
    #       YOUR PASSWORD,
    #   )
    # )

    #Bearer Token Authentication
    bearer_headers = {
    "Authorization": "Bearer "
    }
    sheet_response = requests.post(
        SHEETENDPOINT, 
        json=sheet_inputs, 
        headers=bearer_headers
    )