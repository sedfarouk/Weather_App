from django.shortcuts import render
import requests
from cred import api_key

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric' + '&appid=' + api_key
        
        res = requests.get(url.format(city)).json()

        
        weather_data = {
            'city': city,
            'icon': res['weather'][0]['icon'],
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'wind_speed': res['wind']['speed'],
            'pressure': res['main']['pressure'],
            'humidity': res['main']['humidity'],
            'visibility': res['visibility']
        }
        
    else:
        city = ''
        weather_data = {}
    
    return render(request, "index.html", weather_data)