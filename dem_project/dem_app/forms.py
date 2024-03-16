from django import forms
from django.contrib.auth.models import User
from dem_app.models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'type',
            'phone_number',
            'birth_date',
            'profile_image',
        ]