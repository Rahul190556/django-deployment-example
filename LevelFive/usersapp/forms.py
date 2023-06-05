from django import forms
from django.contrib.auth.models import User
from usersapp.models import UserprofileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserprofileInfo
        fields = ("portfolio_site", "profile_pic")
