from django.contrib import admin
from myapp.models import ContactForm, QuoteRequest, Subscriber
# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['created_at']


admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(QuoteRequest)
admin.site.register(Subscriber)
