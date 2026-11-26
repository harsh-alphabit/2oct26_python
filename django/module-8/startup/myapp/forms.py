from django import forms
from myapp.models import ContactForm, Subscriber

class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'   


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


