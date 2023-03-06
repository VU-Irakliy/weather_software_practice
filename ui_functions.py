
from api_misc_functions import *

window = Tk()
window.title("Weather App")
window.geometry("1280x720")

window.update()
ct = Text(window, height=1, width=7, bg='white')
city = Text(window, height=4, width=20, bg='white')
status_text = Text(window, height=1, width=0, bg='white')
local_time_text = Text(window, height=2, width=0)
time_zone = Text(window, height=1, width=0)
last_update = Text(window, height=1, width=0, bg='white')
hourly_text_box = Text(window, height=11, width=23)
# hourly_frame = Frame(window, bg='blue')


######################################################################################################################


def show_the_weather(window, input):
   
   
    def create_the_weather_display(window, data, location, local_time, local_date):
        timezone, time_abbr, cur_data, hourly_data = sort_data(data)
        current_temperature, weathercode, wind_speed, unform_time = cur_data

        time = convert_the_time(unform_time)
        weather_status = get_the_weather_status(weathercode)
        hourly_time, hourly_temperature = sort_hourly_data(hourly_data, local_date, local_time)
        
        
        
        
        ###################################################################
        
        ######### y = 200 is the starting line
       
        global ct, city, status_text, local_time_text, time_zone, hourly_text_box
        ct.destroy()
        ct = Text(window, height=1, width=7, bg='white')
        ct.config(state=NORMAL)
        ct.delete('1.0',END)
        ct.insert(END, str(current_temperature) + '°C')
        ct.config(font= ("Grotesco", 30, 'bold'), fg = "black")
        ct.place_configure(x= 100, y= 200)
        ct.config(state=DISABLED)
        
        city.destroy()
        city = Text(window, height=4, width=20, bg='white')
        if location[1] == 'United States':
            city.config(state=NORMAL)
            city.delete('1.0',END)
            city.insert(END, location[0] + '\n' + location[2] + '\n' + location[1])
            city.config(font= ("Davish", 20), fg = "black")
            city.place_configure(x= 100, y= 270)
            city.config(state=DISABLED)
        else:
            city.config(state=NORMAL)
            city.delete('1.0',END)
            city.insert(END, location[0] + '\n' + location[1])
            city.config(font= ("Davish", 20), fg = "black")
            city.place_configure(x= 100, y= 270)
            city.config(state=DISABLED)
        
        global status_text
        status_text.destroy()
        status_text = Text(window, height=1, width=0, bg='white')
        # status_text.()
        status_text.config(state=NORMAL)
        status_text.delete('1.0',END)
        status_text.config(width=len(weather_status))
        # status_text.config(text= weather_status)
        status_text.insert(END, weather_status)
        status_text.config(font= ("Davish", 15), fg = "black")
        status_text.place_configure(x= 100, y= 410)
        status_text.config(state=DISABLED)

        local_time_text.destroy()
        local_time_text = Text(window, height=2, width=0)
        local_time_text.config(state=NORMAL)
        local_time_text.delete('1.0',END)
        local_time_text.config(width=len(time[0]))
        local_time_text.insert(END, time[0] + '\n' + time[1])
        local_time_text.config(font= ("Davish", 15), fg = "black")
        local_time_text.place_configure(x = 300, y= 200)
        local_time_text.config(state=DISABLED)

        time_zone.destroy()
        time_zone = Text(window, height=1, width=0)
        time_zone.config(state=NORMAL)
        time_zone.delete('1.0',END)
        time_zone.config(width=len(timezone) + 10)
        time_zone.insert(END, 'Timezone: '+ timezone)
        time_zone.config(font= ("Davish", 10), fg = "black")
        time_zone.place_configure(x = 300, y= 175)
        time_zone.config(state=DISABLED)

        hourly_string = ''
        for i in range(0, len(hourly_time), 6):
            time_row = " ".join(hourly_time[i:i+6])
            temp_row = "   ".join(str(temp) for temp in hourly_temperature[i:i+6])
            hourly_string += f'{time_row}\n{temp_row}\n\n'

        hourly_text_box.destroy()
        hourly_text_box = Text(window, height=11, width=30)
        hourly_text_box.config(state=NORMAL)
        hourly_text_box.delete('1.0',END)
       
        hourly_text_box.insert(END, hourly_string)
        hourly_text_box.config(font= ("Davish", 12), fg = "black")
        hourly_text_box.place_configure(x = 700, y= 200)
        hourly_text_box.config(state=DISABLED)



    def refresh(event=None):
        
        local_timezone = pytz.timezone(result['timezone'])
        local_datetime = datetime.datetime.now(local_timezone).strftime("%d-%m-%Y %H:%M:%S")
        local_date, local_hour = local_datetime.split(" ")
        result = get_weather_data(location_data)
        create_the_weather_display(window, result, input, local_hour, local_date)
        # last_update.()
        global last_update
        last_update.destroy()
        last_update = Text(window, height=1, width=0, bg='white')
        last_update.config(state=NORMAL)
        last_update.config(width=len(current_time) + 12)
        last_update.insert(END, 'Last updated: ' + current_time)
        last_update.config(font= ("Davish", 10), fg = "black")
        last_update.place_configure(x= 50, y= 455)
        last_update.config(state=DISABLED)
        

   
    # input = 
    # fahren_flag = False
    # if input[1] == "United States":
    #     print("HS")
    #     fahren_flag == True
    location_data = get_location_data(input)
    result = get_weather_data(location_data)
    #need TO OUTPUT AN ERROR
    if result == None:
        print("Oops. There is an error.\nCheck the spelling or existence of such location.")
        return
    # print(result)
    
    

    current_time  = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    local_timezone = pytz.timezone(result['timezone'])
    local_datetime = datetime.datetime.now(local_timezone).strftime("%d-%m-%Y %H:%M:%S")
    current_date, current_hour = current_time.split(" ")
    local_date, local_hour = local_datetime.split(" ")
    print(current_date, current_hour)
    # cur_weather = 
    ##
    create_the_weather_display(window, result, input,local_hour, local_date)
    global last_update
    last_update.destroy()
    last_update = Text(window, height=1, width=0, bg='white')
    last_update.config(state=NORMAL)
    last_update.config(width=len(current_time) + 12)
    last_update.insert(END, 'Last updated: ' + current_time)
    last_update.config(font= ("Davish", 10), fg = "black")
    last_update.place_configure(x= 50, y= 455)
    last_update.config(state=DISABLED)

    refresh_button = Button(window, text = 'Refresh')
    refresh_button.bind('<Button-1>', refresh)
    refresh_button.place_configure(x= 310, y= 450)
    
    ...

