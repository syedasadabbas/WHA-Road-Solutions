from django import forms
from .models import CarImage

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']  # Only include the image field
