from django import forms
from .models import Profile
from django.forms.widgets import FileInput

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profile_img",
            "user",
            "name",
            "user_rule",
            "profession"
        ]