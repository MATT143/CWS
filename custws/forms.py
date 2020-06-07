from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile,UserTaskDetails

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'


class createTicketForm(ModelForm):

    class Meta:
        model=UserTaskDetails
        fields=['taskName','taskDescription','taskCategory','taskSubCategory','taskAttachment1','taskAttachment2','taskRevenue']