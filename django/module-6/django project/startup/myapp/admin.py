from django.contrib import admin
from myapp.models import ContactForm, QuoteRequest, Subscriber
# Register your models here.
admin.site.register(ContactForm)
admin.site.register(QuoteRequest)
admin.site.register(Subscriber)
