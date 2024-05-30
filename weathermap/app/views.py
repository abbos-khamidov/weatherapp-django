from django.shortcuts import render
import requests
from .models import City

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ccf20c337679dacd1e236e4739d4a3ea'
    city = 'Tashkent'
    weather_data = []
    
    cities = City.objects.all()
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        
        weather_data.append(city_weather)
        
    context = {
        'weather_data': weather_data
    }
    return render(request, 'index.html', context)