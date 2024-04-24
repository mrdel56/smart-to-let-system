from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'category',
            'rooms',
            'washrooms',
            'kitchen',
            'balcony',
            'floor',
            'location',
            'description',
            'price',
            'property_img',	           
        ]