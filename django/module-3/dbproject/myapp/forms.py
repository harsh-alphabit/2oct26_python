from django import forms
from myapp.models import user_signup

class userForm(forms.ModelForm):
    class Meta:
        model=user_signup
        fields='__all__'
        #fields=['name','email']
