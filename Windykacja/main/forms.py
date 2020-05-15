from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Case
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField



class SignUpForm(UserCreationForm):
    worker_number = forms.DecimalField(max_digits=4, decimal_places=0, required=True, help_text='*')
    phone = PhoneNumberField(region='PL', required=False, help_text='*')
    image = forms.FileField(required=False)
    first_name = forms.CharField(max_length=30, required=True, help_text='*')
    last_name = forms.CharField(max_length=30, required=True, help_text='*')
    email = forms.EmailField(required=True, help_text='*')

    class Meta:
        model = User
        fields = ('worker_number', 'username', 'first_name', 'last_name', 'email', 'phone', 'image', 'password1', 'password2',)



