''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.
Here are the steps you can take to create this project:
    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.
    Use the json library to parse the JSON data returned by the API call.
    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.
    Use the Pillow library to display the weather icons.
    Use the datetime library to display the current time and date. '''
import tkinter

import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
from tkinter import *
from PIL import Image, ImageTk


class weather_app:
    window = Tk()
    window.title('Weather App')
    window.geometry('750x500')
    var1 = "Make sure you don't leave any fields empty or make typos!"
    var2 = ""
    error_label = Label()

    def __init__(self):
        self.appid = '134d0952887f9eccb4ede21a70b62bed'
        self.error = True
        self.font = ('Microsoft Sans Serif', 11, 'normal')
        self.background = '#eef0d3'
        self.foreground = '#455249'

        self.label_intro = Label(self.window, text='Welcome to the Weather App!', font=('Microsoft Sans Serif', 14, 'normal'), fg=self.foreground)
        self.label_intro.grid(row=1, column=3, columnspan=3, sticky=N, pady=(5, 30))
        self.label_city = Label(self.window, text='City: ', fg=self.foreground, font=self.font)
        self.label_city.grid(row=2, column=1, sticky=W, padx=30)
        self.label_country = Label(self.window, text='Country: ', fg=self.foreground, font=self.font)
        self.label_country.grid(row=3, column=1, sticky=W, padx=30)
        self.weather_now = Label()
        self.temp_now = Label()
        self.humidity_now = Label()
        self.hour_later = Label()
        self.temp_later = Label()
        self.humidity_later = Label()

        self.entry_city = Entry(self.window)
        self.entry_city.focus_set()
        self.entry_city.grid(row=2, column=2)
        self.entry_country = Entry(self.window)
        self.entry_country.grid(row=3, column=2)

        self.ok_button = Button(self.window, text='OK', font=self.font, highlightthickness=5, command=self.go, fg='blue')
        self.ok_button.grid(row=4, column=2)

        self.reset_button = Button(self.window, text='Reset', font=self.font, highlightthickness=5, command=self.reset, fg='red')
        self.reset_button.grid(row=4, column=1)

        self.window.mainloop()

        self.go()


    def go(self):
        # ------------------------ REQUESTING THE USER INPUT & GETTING THE COUNTRY ISO CODE ------------------------ #
        while self.error:
            try:

                city = self.entry_city.get().title()
                country_requested = self.entry_country.get().title()
                self.entry_city.delete(0, END)
                self.entry_country.delete(0, END)
                if len(city) == 0 or len(country_requested) == 0:
                    self.error_label.grid_forget()
                    self.error_label = Label(self.window, text=self.var1)
                    self.error_label.grid(row=5, column=1, columnspan=2)
                    self.error = True
                    self.__init__()
                    continue
                else:
                    self.error_label.grid_forget()
                    error_label = Label(self.window, text=self.var2)
                    error_label.grid(row=5, column=1, columnspan=2)
                    self.error = False

                codes = requests.get('https://countrycode.org/')
                soup_codes = BeautifulSoup(codes.content, 'html.parser')
                country_iso_code = soup_codes.find("td", string=country_requested).find_next("td").text.strip()

                # ------------------------ DEFINING THE WEATHER & FORECAST ENDPOINTS & PARAMETERS  ------------------------ #
                geocoding_url = 'http://api.openweathermap.org/geo/1.0/direct'
                parameters_geo = {
                    'q': f'{city},{country_iso_code}',
                    'appid': self.appid,
                    'limit': 1
                }
                geocode = requests.get(geocoding_url, params=parameters_geo)
                geocode.raise_for_status()
                lat = geocode.json()[0].get("lat")
                lon = geocode.json()[0].get("lon")
            except:
                self.error_label.grid_forget()
                self.error_label = Label(self.window, text=self.var1)
                self.error_label.grid(row=5, column=1, columnspan=2)
                self.error = True
            else:
                self.error_label.grid_forget()
                self.error_label = Label(self.window, text=self.var2)
                self.error_label.grid(row=5, column=1, columnspan=2)

                # ------------------------ DEFINING THE ENDPOINTS & GEOGRAPHICAL PARAMETERS  ------------------------ #
                open_weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
                parameters_weather = {
                    'lat': lat,
                    'lon': lon,
                    'units': 'metric',
                    'exclude': 'minutely,daily,alerts',
                    'appid': self.appid,
                }

                # ------------------------ GETTING THE WEATHER & FORECAST FOR THAT CITY ------------------------ #

                weather = requests.get(url=open_weather_url, params=parameters_weather)
                weather.raise_for_status()
                data = weather.json()
                data_slice = data['hourly']
                forecast = []

                for slice in data_slice[:8]:
                    dt_object = dt.fromtimestamp(slice['dt'])
                    temperature = slice['temp']
                    humidity = slice['humidity']
                    sky = slice['weather'][0]['description']
                    forecast.append(
                        {'Hour:': f'{dt_object.hour}:00', 'Temperature:': f'{int(temperature)} C', 'Humidity:': f'{humidity}%', 'Sky:': sky})

                # ------------------------ GETTING THE ICONS FOR THAT SPECIFIC WHEATER ------------------------ #

                def get_clear_sky(row, column):
                    clear_sky = Image.open(r'C:\Users\Denis\PycharmProjects\Kreativstorm training\session_5\session_5_tema\clear_sky.png')
                    process_clear_sky = ImageTk.PhotoImage(clear_sky)
                    label_clear_sky = Label(image=process_clear_sky)
                    label_clear_sky.image = process_clear_sky
                    label_clear_sky.grid(row=row, column=column)

                def get_clouds(row, column):
                    clouds = Image.open(r'C:\Users\Denis\PycharmProjects\Kreativstorm training\session_5\session_5_tema\clouds.png')
                    process_clouds = ImageTk.PhotoImage(clouds)
                    label_clouds = Label(image=process_clouds)
                    label_clouds.image = process_clouds
                    label_clouds.grid(row=row, column=column)

                def get_rain(row, column):
                    rain = Image.open(r'C:\Users\Denis\PycharmProjects\Kreativstorm training\session_5\session_5_tema\rain.png')
                    process_rain = ImageTk.PhotoImage(rain)
                    label_rain = Label(image=process_rain)
                    label_rain.image = process_rain
                    label_rain.grid(row=row, column=column)

                def get_snow(row, column):
                    snow = Image.open(r'C:\Users\Denis\PycharmProjects\Kreativstorm training\session_5\session_5_tema\snow.png')
                    process_snow = ImageTk.PhotoImage(snow)
                    label_snow = Label(image=process_snow)
                    label_snow.image = process_snow
                    label_snow.grid(row=row, column=column)

                def get_sky(sky_data):
                    if 'clear sky' in sky_data:
                        return get_clear_sky
                    elif 'clouds' in sky_data:
                        return get_clouds
                    elif 'rain' in sky_data:
                        return get_rain
                    elif 'snow' in sky_data:
                        return get_snow


                for i in forecast:
                    ind = forecast.index(i)
                    hour = i['Hour:']
                    temp = i['Temperature:']
                    humidity = i['Humidity:']
                    sky = i['Sky:']

                    # ------------------------ DISPLAYING THE INFO ON THE TKINTER WINDOW ------------------------ #

                    if forecast.index(i) == 0:
                        self.weather_now = Label(self.window, text=f"{city} now:", font=self.font, fg=self.foreground)
                        self.weather_now.grid(row=6, column=1, padx=30)
                        self.temp_now = Label(self.window, text=f"Temperature: {temp}", font=self.font, fg=self.foreground)
                        self.temp_now.grid(row=6, column=2)
                        self.humidity_now = Label(self.window, text=f"Humidity: {humidity}", font=self.font, fg=self.foreground)
                        self.humidity_now.grid(row=7, column=2)
                        sky_shorthened = get_sky(sky)
                        icon = sky_shorthened(row=8, column=2)

                    else:
                        self.hour_later = Label(self.window, text=hour, font=self.font, fg=self.foreground)
                        self.hour_later.grid(row=ind+1, column=4)
                        self.temp_later = Label(self.window, text=f"Temperature: {temp}", font=self.font, fg=self.foreground)
                        self.temp_later.grid(row=ind+1, column=5)
                        self.humidity_later = Label(self.window, text=f"Humidity: {humidity}", font=self.font, fg=self.foreground)
                        self.humidity_later.grid(row=ind+1, column=6)
                        sky_shorthened = get_sky(sky)
                        icon = sky_shorthened(row=ind+1, column=7)

# ------------------------ DEFINING THE RESET BUTTON ACTIONS ------------------------ #

    def reset(self):
        self.error_label.grid_forget()
        self.weather_now.grid_forget()
        self.error_label = Label(self.window, text=self.var2)
        self.error_label.grid(row=5, column=1, columnspan=2)
        self.__init__()


whats_the_weather = weather_app()













