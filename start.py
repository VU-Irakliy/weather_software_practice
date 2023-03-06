from ui_functions import *


# https://geocoding-api.open-meteo.com/v1/search  location
# https://open-meteo.com/

URL_weather = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
URL_location = "https://geocoding-api.open-meteo.com/v1/search"


time_len = len(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))



#################################################################################################################################################
def get_me_the_current_time():

    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    current_time_visual.config(state=NORMAL)
    current_time_visual.delete('1.0',END)
    current_time_visual.insert(END, current_time)
    current_time_visual.config(font= ("Times New Roman", 14), fg = "black")
    current_time_visual.place_configure(x = (window.winfo_width() - 230), y = 10) #1280 - 1050 = 230
    current_time_visual.config(state=DISABLED)
    window.after(1000, get_me_the_current_time)



def weather_button_clicked(event = None):
    show_the_weather(window, [input_field_city.get(), input_field_country.get().title(), input_field_state.get().title()])


#################################################################################################################################################



bg = ImageTk.PhotoImage(Image.open("images/background.jpg"))
ligm = Label(window, i = bg)
ligm.pack()

back = Image.open("images/logo.png")
back = back.resize((round(back.width / 2), round(back.height / 2)))
logo = ImageTk.PhotoImage(back)

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


# window.resizable(False, False)
# window.update_idletasks()
# if platform.system() == "Windows":
#     window.wm_minsize(800, 300)
# else:
#     window.minsize(800, 600)

# new_frame = Frame(window,   bg="", highlightthickness=0, bd=0)
# new_frame.pack(side='bottom', fill='x')
# new_button = Button(new_frame, text="Help")
# new_button.pack()

# print("wjat+++", window.winfo_width())
# i_need_a_background = os.getcwd()
# background = i_need_a_background(f'images/background.jpg')
# background = Image.open('images/background.jpg')

# window.minsize(width=800,height= 600)
# window.maxsize(width= 1440, height=900)