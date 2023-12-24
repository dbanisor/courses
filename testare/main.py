import requests
import json

json_data = requests.get("https://randomuser.me/api/").json()
results = json_data.get("results")[0]
print(results)
last = results.get("name").get("last")
print(last)
state = results.get("location").get("state")
country = results.get("location").get("country")
some_missing_data = results.get("location").get("cory", "no such data")

print(f"{last} is from state {state}, country {country} and smth {some_missing_data}")

# new_site = json.
# print(new_site)
# print(site)
# #
# first_name = site["results"][0]["name"]["first"]
# first_name = results.get("name", {}).get("first")  # ia cheia "nume" din dictionar {}
# print(first_name)
# last_name = site["results"][0]["name"]["last"]
# last_name = results.get("name", {}).get("last")
# print(last_name)
# entire_name = first_name + " " + last_name
# print(f"The entire name is {entire_name}.")
#
# results = site["results"]
#
# everyone = []
#
# for i in results:
#     first_name = i["name"]["first"]
#     last_name = i["name"]["last"]
#     entire_name = first_name + " " + last_name
#     everyone.append(entire_name)

# print(everyone)
# print(site)

# from flask import Flask, render_template, redirect, url_for, request
# import json
# import requests
#
#
#
# URL = "https://api.themoviedb.org/3/search/movie?api_key=7e1d1fec31a01d1f0bb22c63508cae96&query="
# text_searched = URL + "the notebook"
# r = requests.get(url=text_searched)
# data = json.loads(r.text)
# api_id = request.args.get("id")
# print(id)
# # print(int(data["results"][0]["release_date"][:4]))

# from flask import Flask
# import requests
#
# api_key = "680218664f8d091cb26965560d3ad07b"
# url = "https://api.openweathermap.org/data/3.0/onecall"
# parameters = {
#     "lat, lon": (44.429777, 26.147015),
#     "appid": api_key
# }
# app = Flask(__name__)
# response = requests.get(url=url, params=parameters)
#
# @app.route("/")
# def home():
#     response = requests.get(url=url, params=parameters)
#     data = response.json()
#     return data
#
# @app.route("/<string:name>")
# def hello_name(name):
#     return "Hello " + name
#
#
# app.run(debug=True)