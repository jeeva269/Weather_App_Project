from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        Widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'City Name'})}