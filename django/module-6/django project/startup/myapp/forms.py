from django import forms
from myapp.models import ContactForm, QuoteRequest, Subscriber

class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'   


class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = '__all__'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
