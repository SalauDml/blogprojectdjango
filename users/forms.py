from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields=['username','email','first_name','last_name','password1','password2']