import requests
import datetime as dt
#
# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response) ### This generates an Status Code: 200 if everything went ok ###
# print(response.status_code) ### If you want to know the actual status code ###
#
# response.raise_for_status() ### "raise_for_status()" will raise an HTTPError if the HTTP request returned any of the unsuccessful status code. ###
#
# '''READING THE DATA'''
# data = response.json()
# print(data)
#
# '''DIGGING INTO THE DATA'''
# iss_position = response.json()["iss_position"]
# print(iss_position)
#
# '''DIGGING MORE INTO THE DATA'''
# iss_latitude = response.json()["iss_position"]["latitude"]
# iss_longitude = response.json()["iss_position"]["longitude"]
# position = (iss_longitude, iss_latitude)
# print(position)

parameters = {
    "lat": 44.429777,
    "lng": 26.147015,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
print(data)
sunrise = data.get("sunrise")
sunset = data.get("sunset")
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = dt.datetime.now()
print(time_now.hour)