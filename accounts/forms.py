from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User as UserModel
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel  # Cambiado de User a UserModel
        fields = ("username", "email")

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = UserModel  # Cambiado de User a UserModel
        fields = ('email', 'last_name')

