from django import forms
from myapp.models import ContactForm

class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'   
