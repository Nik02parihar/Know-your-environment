from django.http import HttpResponse
from django.shortcuts import render
from pip import main
import requests


def home(request):
    la = request.GET.get('la', 28.6172 )
    lg = request.GET.get('lg', 77.2082 )

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={la}&lon={lg}&appid=abf5fc50e1c0749e94fbad9f67633939"

    data = requests.get(url).json()
    Api_Data = {
        'Area':data['name'],
        "weather": data["weather"][0]["main"],
        "icon": data["weather"][0]["icon"],
        "k_temp": int(data["main"]["temp"]),
        "c_temp": int(data["main"]["temp"] -273),
        "pressure": data["main"]["pressure"],
        "humidity": data["main"]["humidity"],
        "desc": data["weather"][0]["description"]
    }
    context = {'data':Api_Data}
    print(context)
    return render(request, "home.html",context)
