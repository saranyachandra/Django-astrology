from django.http import Http404
from django.shortcuts import render

# Create your views here.

import urllib.request 

import json

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        #start_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=dd482db00265800e476a15f785a84f69'
        #url = start_url.replace(" ","")
        #source = urllib.request.urlopen(url).read()
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +city+ '&units=metric&appid=dd482db00265800e476a15f785a84f69').read()
        list_of_data = json.loads(source)

        data =  {
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate"    : str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp"      : str(list_of_data['main']['temp']) + ' °C',
            "pressure"      : str(list_of_data['main']['pressure']),
            "humidity"      : str(list_of_data['main']['humidity']),
            "main"          : str(list_of_data['weather'][0]['main']),
            "description"       : str(list_of_data['weather'][0]['description']),
            "icon"      : str(list_of_data['weather'][0]['icon']),
            "city"      : str(list_of_data['name']),
        }

        print(data)

    else:
        data = {}

    return render(request, "show_weather.html", data)