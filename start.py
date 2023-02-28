from tkinter import *
from ui import *
from PIL import Image, ImageTk
import datetime
import os
import requests
import json
import platform

# https://geocoding-api.open-meteo.com/v1/search  location
# https://open-meteo.com/
URL_weather = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
URL_location = "https://geocoding-api.open-meteo.com/v1/search"

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
    
    # if len()
    # print()
    # print(len(response.json()))
    ...
def get_weather_data(location):
    # get_location_data(location)
    location_data = get_location_data(location)
    print(location_data)
    if location_data == (None, None):
        return None
    print('wahy')
    URL_weather = "https://api.open-meteo.com/v1/forecast?latitude="+ str(location_data[0]) + "&longitude="+ str(location_data[1])+"&current_weather=true"
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
time_len = len(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
def get_me_the_current_time():

    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    current_time_visual.config(state=NORMAL)
    current_time_visual.delete("1.0", END)
    current_time_visual.insert(END, current_time)
    current_time_visual.config(font= ("Times New Roman", 14), fg = "black")
    current_time_visual.place_configure(x = (window.winfo_width() - 230), y = 10) #1280 - 1050 = 230
    current_time_visual.config(state=DISABLED)
    window.after(1000, get_me_the_current_time)

def show_the_weather(input):
    # input = 
    result = get_weather_data(input)
    if result == None:
        print("Oops. There is an error.\nCheck the spelling or existence of such location.")
        return
    print(result['current_weather'])
    ...

window = Tk()

window.title("Weather App")

window.geometry("1280x720")
# window.update_idletasks()
# if platform.system() == "Windows":
#     window.wm_minsize(800, 300)
# else:
#     window.minsize(800, 600)

window.update()


# print("wjat+++", window.winfo_width())
# i_need_a_background = os.getcwd()
# background = i_need_a_background(f'images/background.jpg')
# background = Image.open('images/background.jpg')

bg = ImageTk.PhotoImage(Image.open("images/background.jpg"))
ligm = Label(window, i = bg)
ligm.pack()

back = Image.open("images/logo.png")
back = back.resize((round(back.width / 2), round(back.height / 2)))
logo = ImageTk.PhotoImage(back)
# logo = logo.resize(round(logo.width / 10), round(logo.height / 10))

w = Label(window, image = logo)
w.place_configure(x = 10, y = 10)

current_time_visual = Text(window, height=1, width=17, state= DISABLED)
current_time_visual.pack()

get_me_the_current_time()
text_ff = "Enter the location here for weather forecast"
enter_the_text_text = Text(window, height=1, width=36)
enter_the_text_text.insert(END,text_ff )
enter_the_text_text.config(font= ("Times New Roman", 14), fg = "black")
enter_the_text_text.place_configure(x = (window.winfo_width()/2 - 150), y=1)
# 


input_field_city = Entry(window)
input_field_city.config(width= 30)
input_field_city.insert(0, "Enter City Here")
input_field_city.place_configure(x = (window.winfo_width()/2 - 150), y = 50)


input_field_country = Entry(window)
input_field_country.config(width= 30)
input_field_country.insert(0, "Enter Country Here")
input_field_country.place_configure(x = (window.winfo_width()/2 - 150), y = 80)


input_field_state = Entry(window)
input_field_state.config(width= 30)
input_field_state.insert(0, "Enter US State Here (Optional)")
input_field_state.place_configure(x = (window.winfo_width()/2 - 150), y = 110)


# loc_input = ["Amsterdam", "Netherlands", ""]
# weather_data = get_weather_data(loc_input)

def weather_button_clicked(event = None):
    show_the_weather([input_field_city.get(), input_field_country.get(), input_field_state.get()])

weather_button = Button(window, text = "Search")
weather_button.bind("<Button-1>", weather_button_clicked)
weather_button.place_configure(x = (window.winfo_width()/2) + 150, y = 80 )


window.mainloop()

print('HOMIE')

# width = window.winfo_width()
#     height = window.winfo_height()
# the_b = Button(window, text = "Sta")  ## , command = )
# the_b.place_configure(x = 600,y = 360) 
# the_b.pack()