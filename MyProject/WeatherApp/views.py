from django.shortcuts import render
from .form import CityForm
from .models import City
import requests
from django.contrib import messages

def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},&appid=69274f166d75241f20012e953932dfbb&units=metric'
    
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            NCity = form.cleaned_data['name']
            CCity = City.objects.filter(name=NCity).count()
            if CCity == 0:
                res = requests.get(url.format(NCity)).json()
                if res['cod'] == 200:
                    form.save()
                    messages.success(request, ""+NCity+" Added Successfully...!!!")
                else:
                    messages.error(request, "City Does Not Exists...!!!")
            else:
                messages.error(request, "City Already Exists...!!!")            
    form = CityForm()
    cities=City.objects.all()
    
    return render(request, "weatherapp.html", {'cities': cities, 'form': form})