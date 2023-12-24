import requests
import os
# from twilio.rest import Client

api_key = "680218664f8d091cb26965560d3ad07b"
latitude = 44.428070
longitude = 26.148260
account_sid = "AC57def140c35c777fe5706b4903c903e8"
auth_token = "116294150a8c9db20126507824ede5fb"

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Remember to bring an ??",
#         from_='+16204728973',
#         to='+40751512677'
#     )
#     print(message.status)
















