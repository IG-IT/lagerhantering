from django import forms
from .models import Produkt

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = ['...', 'bild', ...]  # list all the fields you want to use

    bild = forms.ImageField(widget=forms.ClearableFileInput(attrs={'capture': 'camera', 'accept': 'image/*'}))
