from tkinter import *

from PIL import Image, ImageTk
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
import datetime
import os
import requests
import json
import platform
#######SORT DATA AND UI OF WEATHER################################################################
def get_the_weather_status(number):
    switcher = {
        0: 'Clear Sky',
        1: 'Mostly Clear Sky',
        2: 'Partly Cloudy',
        3: 'Overcast',
        45: 'Foggy',
        48: 'Depositing Rime Fog',
        51: 'Light Drizzle',
        53: 'Moderate Drizzle',
        55: "Dense Drizzle",
        56: 'Light Freezing Drizzle',
        57: 'Heavy Freezing Drizzle',
        61: 'Slight Rain',
        63: 'Moderate Rain',
        65: 'Heavy Rain',
        66: 'Slight Freezing Rain',
        67: 'Heavy Freezing Rain',
        71: 'Slight Snow Fall',
        73: 'Moderate Snow Fall',
        75: 'Heavy Snow Fall',
        77: 'Snow Grains',
        80: 'Slight Rain Showers',
        81: 'Moderate Rain Showers',
        82: 'Violent Rain Showers',
        85: 'Slight Snow Showers',
        86: 'Heavy Snow Showers',
        95: 'Thunderstorm',
        96: 'Thunderstorm With Slight Hail',
        99: 'Thunderstorm With Heavy Hail'
    }
    return switcher.get(number, 'Ooops, something went wrong.')


def sort_data(data):
    timezone, time_abbr = data["timezone"], data['timezone_abbreviation']
    cur_data = data['current_weather']
    current_temperature, weathercode, wind_speed = cur_data['temperature'], cur_data['weathercode'], cur_data['windspeed']
    return timezone, time_abbr, current_temperature, weathercode, wind_speed
    ...

def create_the_weather_display(window, data, location):
    timezone, time_abbr, current_temperature, weathercode, wind_speed = sort_data(data)
    weather_status = get_the_weather_status(weathercode)
    # print(type(current_temperature))
    ######### y = 200 is the starting line
    ct = Text(window, height=1, width=7, bg='white')
    ct.insert(END, str(current_temperature) + '°C')
    ct.config(font= ("Grotesco", 30, 'bold'), fg = "black")
    ct.place_configure(x= 100, y= 200)
    ct.config(state=DISABLED)

    if location[1] == 'United States':

        city = Text(window, height=4, width=20, bg='white')
        city.insert(END, location[0] + '\n' + location[2] + '\n' + location[1])
        city.config(font= ("Davish", 20), fg = "black")
        city.place_configure(x= 100, y= 270)
        city.config(state=DISABLED)
    else:
        city = Text(window, height=3, width=20, bg='white')
        city.insert(END, location[0] + '\n' + location[1])
        city.config(font= ("Davish", 20), fg = "black")
        city.place_configure(x= 100, y= 270)
        city.config(state=DISABLED)

    status_text = Text(window, height=1, width=len(weather_status), bg='white')
    status_text.insert(END, weather_status)
    status_text.config(font= ("Davish", 15), fg = "black")
    status_text.place_configure(x= 100, y= 400)
    status_text.config(state=DISABLED)

    ...

###########DATA ACQUIREMENT#######################################################################################################

def get_location_data(input):
    city, country, US_state = input
    URL_location = "https://geocoding-api.open-meteo.com/v1/search?name="+city
    response = requests.get(URL_location)
    data = response.json()
    longitude = None
    latitude = None
    if len(data) == 1:
        return longitude, latitude
    data = data['results']
    # print(data)
    flag = False
    
    for i in data:
        if i['country'] == country:
            if country == "United States":
                print("MERICA")
                print(i['admin1'])
                if i["admin1"] == US_state:
                    longitude, latitude = i['longitude'], i['latitude']
                    flag = True
                
            else:
                longitude, latitude = i['longitude'], i['latitude']
                flag = True
                
            
        if flag == True:
            break

    print(len(data))
    return longitude, latitude
    

def get_weather_data(location):
    # get_location_data(location)
    location_data = get_location_data(location)
    print(location_data)
    if location_data == (None, None):
        return None
    print('wahy')
    # fhr = ''
    # if fahren_flag == True:
        # fhr = '&temperature_unit=fahrenheit'
    URL_weather = "https://api.open-meteo.com/v1/forecast?latitude="+ str(location_data[1]) + "&longitude="+ str(location_data[0]) +"&current_weather=true&timezone=auto" ##"&hourly=temperature_2m&current_weather=true"##
    
    response = requests.get(URL_weather)
    data = response.json()
    # print()
    # print(location_data)
    # print(data["current_weather"])
    return data
    # response = requests.get(URL_weather)
    # data = response.json()

    # print()
    ...


###########MAIN  FUNCTION#########################################################################################################
def show_the_weather(window, input):
    # input = 
    # fahren_flag = False
    # if input[1] == "United States":
    #     print("HS")
    #     fahren_flag == True
    result = get_weather_data(input)
    if result == None:
        print("Oops. There is an error.\nCheck the spelling or existence of such location.")
        return
    print(result)
    
    

    
    # cur_weather = 
    ##
    create_the_weather_display(window, result, input)
    
    ...