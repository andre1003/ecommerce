from django import forms
from django.contrib.auth.forms import BaseUserCreationForm

from .models import User


# User creation form
class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['email']
        field_classes = {'email': forms.EmailField}