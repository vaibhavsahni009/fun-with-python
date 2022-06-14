import requests
import os

OWM_endpoint="https://api.openweathermap.org/data/2.5/onecall"


weather_params={
    "lat":33.44,
    "lon":-94.04,
    "exclude":"current,minutely,daily,alerts",
    "appid":os.environ.get("OWM_API")
}

response=requests.get(OWM_endpoint,params=weather_params)
response.raise_for_status()

weather_data=response.json()
hourly_data=weather_data["hourly"][:13]
flag=False
for i in hourly_data:
    print(i["weather"][0]["id"])
    if int(i["weather"][0]["id"])<=700:
        flag=True
        break
if flag:
    print("Bring an Umbrella")


# print(weather_data)