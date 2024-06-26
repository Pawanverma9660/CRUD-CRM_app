from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput,TextInput
from .models import Record

#  Register/Create a User

class CreateUserForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1' ,'password2']

# Login a User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



# Create a Record 
class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ('first_name','last_name','email','phone','address','city','state','country')


# Update a Record 
class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ('first_name','last_name','email','phone','address','city','state','country')

