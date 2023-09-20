import tkinter as tk
from tkinter import *
import os
from datetime import datetime
import pytz
import requests
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from googletrans import Translator

translator = Translator()

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

root = Tk()
root.title("Weather App")
canv = Canvas(root, width=900, height=500, bg='#1BB0E8')
canv.grid(row=2, column=3)

def getWeather():
    city = search_box_text.get()

    geolocator = Nominatim(user_agent ="numpy")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

    actual_time.config(text=current_time)
    actual_weather.config(text="CLIMA ACTUAL")

    #weather
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+ str(location.latitude) + "&lon="+ str(location.longitude) +"&appid=646824f2b7b86caffec1d0b16ea77f79"
    
    
    #Api url example
    #https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}

    #My api url (Does not work because my key is not confirm)
    #https://api.openweathermap.org/data/2.5/weather?lat=51.5073359&lon=-0.12765&appid=0ec2d573463938d3144d8293f6e4021a

    #Stranger key
    #646824f2b7b86caffec1d0b16ea77f79 --> key de persona x

    #api result
    json_data = requests.get(api).json()

    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"]-273.15)
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]

    traslated_condition = translator.translate(condition, src='en', dest="es")

    #Sides information
    temp_box.config(text=(temp, "°"))
    climate_box.config(text=(condition, "|", traslated_condition.text))

    #Bottom box
    climate_preset_text.config(text=(traslated_condition.text))
    climate_preset_text.place(x=108, y=449)

    humidity_preset_text.config(text=humidity)
    humidity_preset_text.place(x=268.5, y=449)

    rain_preset_text.config(text= "Si" if humidity > 50 else "No")
    rain_preset_text.place(x=500, y=449)

    wind_preset_text.config(text=wind)
    wind_preset_text.place(x=715, y=449)

#search box
search_box_path = os.path.join(parent_dir, "images", "search_box_logo.png")
search_box_image = ImageTk.PhotoImage(Image.open(search_box_path))
canv.create_image(210, 20, anchor=NW, image=search_box_image)

search_box_text = tk.Entry(root, justify="center", width=20, font=("montserrat", 23, "bold"), bg="#434343", border=0, fg="white")
search_box_text.place(x=280, y=40)
search_box_text.focus()

#search button
search_logo_path = os.path.join(parent_dir, "images", "search_logo.png")
search_logo_image = Image.open(search_logo_path)
search_logo_image = ImageTk.PhotoImage(Image.open(search_logo_path))
search_logo_button = Button(image=search_logo_image, borderwidth=0, cursor="hand2", bg="#434343", activebackground="#434343", command=getWeather)
search_logo_button.place(x=590, y=30, anchor=NW)

#weather logo
weather_logo_path = os.path.join(parent_dir, "images", "weather_logo.png")
weather_logo_image = Image.open(weather_logo_path)
weather_logo_image = ImageTk.PhotoImage(Image.open(weather_logo_path))
canv.create_image(310, 112, anchor=NW, image=weather_logo_image)

#Left Side information
actual_weather = Label(root, font=("arial", 25, "bold"),fg="white", bg="#1BB0E8")
actual_weather.place(x=60,y=120)
actual_time = Label(root, font=("Helvetica", 20),fg="white", bg="#1BB0E8")
actual_time.place(x=60,y=170)

#Right Side information
temp_box = Label(font=("arial", 70, "bold"), fg="white", bg="#1BB0E8")
temp_box.place(x=625, y=150)
climate_box = Label(font=("arial", 15, "bold"), bg="#1BB0E8")
climate_box.place(x=625, y=250)

#Bottom box
weather_data_logo_path = os.path.join(parent_dir, "images", "box_logo.png")
weather_data_logo_image = Image.open(weather_data_logo_path)
weather_data_logo_image = ImageTk.PhotoImage(Image.open(weather_data_logo_path))
canv.create_image(55, 400, anchor=NW, image=weather_data_logo_image)

climate_label = Label(root, text="CLIMA", font=("Helvetica",15,"bold underline"), fg="white", bg="#1CB7F1")
climate_label.place(x=110, y=420)
climate_preset_text = Label(text="-",font=("arial", 20, "bold"), fg="#434343", bg="#1CB7F1")
climate_preset_text.place(x=110, y=449)

humidity_label = Label(root, text="HUMEDAD", font=("Helvetica",15,"bold underline"), fg="white", bg="#1CB7F1")
humidity_label.place(x=230, y=420)
humidity_preset_text = Label(text="-",font=("arial", 20, "bold"), fg="#434343", bg="#1CB7F1")
humidity_preset_text.place(x=230, y=449)

rain_label = Label(root, text="PROBABILIDAD DE LLUVIA", font=("Helvetica",15,"bold underline"), fg="white", bg="#1CB7F1")
rain_label.place(x=390, y=420)
rain_preset_text = Label(text="-",font=("arial", 20, "bold"), fg="#434343", bg="#1CB7F1")
rain_preset_text.place(x=390, y=449)

wind_label = Label(root, text="VIENTO", font=("Helvetica",15,"bold underline"), fg="white", bg="#1CB7F1")
wind_label.place(x=710, y=420)
wind_preset_text = Label(text="-",font=("arial", 20, "bold"), fg="#434343", bg="#1CB7F1")
wind_preset_text.place(x=710, y=449)

root.mainloop()

