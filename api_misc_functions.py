from tkinter import *

from PIL import Image, ImageTk
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
import datetime
import pytz
import os
import requests
import json
import platform




def convert_the_time(string):
    date_parts = string.split('T')
    formatted_time = datetime.datetime.strptime(date_parts[0],'%Y-%m-%d')
    date= formatted_time.strftime('%d-%m-%Y')
    return [date, date_parts[1]]





def get_location_data(input):
    city, country, US_state = input
    URL_location = "https://geocoding-api.open-meteo.com/v1/search?name="+city
    response = requests.get(URL_location)
    if response.status_code == 200:
        data = response.json()

        longitude = None
        latitude = None
        if len(data) == 1:
            return longitude, latitude
        data = data['results']
        flag = False
        
        for i in data:
            if i['country'] == country:
                if country == "United States":
                    
                    if i["admin1"] == US_state:
                        longitude, latitude = i['longitude'], i['latitude']
                        flag = True
                    
                else:
                    longitude, latitude = i['longitude'], i['latitude']
                    flag = True
                    
                
            if flag == True:
                break

        return longitude, latitude
    elif response.status_code == 204 or response.status_code == 400 or response.status_code == 404 or response.status_code == 503:#Check parameters
        return response.status_code
    elif response.status_code == 500:
        return response.status_code
    else: 
        return 'unknown' 
    





def get_weather_data(location_data):
    
    if location_data == (None, None):
        return None
    elif location_data == 204 or location_data == 400 or location_data == 404 or location_data == 503 or location_data == 500:
        return ('location', location_data)
    elif location_data == 'unknown':
        return ('location', location_data)

   
    URL_weather = "https://api.open-meteo.com/v1/forecast?latitude="+ str(location_data[1]) + "&longitude="+ str(location_data[0]) +"&current_weather=true&hourly=temperature_2m&timezone=auto" ##"&hourly=temperature_2m&current_weather=true"##
    
    response = requests.get(URL_weather)
    if response.status_code == 200:
        data = response.json()
        
        return data
    elif response.status_code == 503 or response.status_code == 204 or response.status_code == 404 or response.status_code == 500 or response.status_code == 400:
        return ('weather', response.status_code)
    else:
        return ('weather', 'unknown')
    
    ...




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
    cur_data_sorted = [cur_data['temperature'], cur_data['weathercode'], cur_data['windspeed'], cur_data['time']]
    hourly_data = data['hourly']
    
    return timezone, time_abbr, cur_data_sorted, hourly_data





def sort_hourly_data(data, current_date, current_time):
    time, temperature = data['time'], data['temperature_2m']
    formatted_time = [convert_the_time(t) for t in time]
    current_hour = current_time[0:2] + ':00'
    nec_index = formatted_time.index([current_date, current_hour])
    formatted_time = formatted_time[(nec_index +1):(nec_index + 25)]
    formatted_time = [i[1] for i in formatted_time]
    formatted_temperature = temperature[(nec_index + 1):(nec_index+25)]
    
    return formatted_time, formatted_temperature


