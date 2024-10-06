from .models import Catalog,Photo
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput,ImageField

class CatologForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ['nameobject', 'textobject', 'whoseobject', 'city', 'type','date']  # Без photoobject

class PhotoForm(forms.Form):
    images = forms.ImageField(required=False)