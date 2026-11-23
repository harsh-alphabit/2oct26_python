from django import forms
from myapp.models import User

#form use= to validate the data and save the data in database

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        