from django import forms

from .models import Location, Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "title",
            "category",
            "rooms",
            "washrooms",
            "kitchen",
            "balcony",
            "floor",
            "property_img",
            "description",
            "price",
        ]


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            "area",
            "road_no",
            "upazila",
            "post_code",
            "district",
        ]
