from flask import Flask
from flask import render_template, request, url_for
import pymongo
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask import jsonify
import datetime as dt
import requests
from views import views
#you would store your own mongodb atlas connection string under the "Config" class in a config.py file created by yourself
from config import Config

#creating app and connecting to mongodb atlas
app = Flask(__name__)
bcrypt = Bcrypt(app)

#connecting to Open Weather Api
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('static/api_key','r').read()
CITY = "St Louis"
url = BASE_URL + "appid=" + API_KEY + "&q=" +CITY
response = requests.get(url).json()


def celsiusConvt(kelvin):
    cel = kelvin - 273.15
    return cel

kelvin = response['main']['temp']
celsius = round(celsiusConvt(kelvin), 3)

if celsius >15 and celsius < 30:
    rec = "Good temperature to workout outside!"
elif celsius > 30:
    rec = "A bit too hot to workout outside"
else:
    rec = "A bit too cold to workout outside"

weather = response['weather'][0]['description']

#print(weather, celsius, rec)


app.register_blueprint(views, url_prefix="/")

@app.route("/")
def home():
    return render_template("index.html", name="User", temp = celsius, weathDesc = weather, recommnedation = rec, city = CITY, showHomePageAlert=True)

if __name__ == '__main__':
    app.run(debug=True, port=3000)