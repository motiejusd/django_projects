from django.shortcuts import render
import pandas as pd
import requests


def index(request):
    df = pd.read_csv('weather/worldcities.csv')
    if 'city' in request.GET:
        city = request.GET['city']

        if df[df['city_ascii'] == city]['city_ascii'].any():

            lat = df[df['city_ascii'] == city]['lat']
            lon = df[df['city_ascii'] == city]['lng']
            url = "https://climacell-microweather-v1.p.rapidapi.com/weather/realtime"

            querystring = {"unit_system": "si","fields": ["precipitation",
                            "precipitation_type", "temp", "cloud_cover", "wind_speed",
                            "weather_code"], "lat": lat, "lon": lon}

            headers = {
                'x-rapidapi-key': "d98e7d5806msh421ae540a8f402dp17aa5ajsn61ea64253cda",
                'x-rapidapi-host': "climacell-microweather-v1.p.rapidapi.com"
                }

            response = requests.request("GET", url, headers=headers, params=querystring).json()

            context = {'city_name': city, 'temp': response['temp']['value'],
                        'weather_code': response['weather_code']['value'],
                        'wind_speed': response['wind_speed']['value'],
                        'precipitation_type': response['precipitation_type']['value']}
        else:
            context = None
    else:
        context = None
    return render(request, 'weather/index.html', context)
