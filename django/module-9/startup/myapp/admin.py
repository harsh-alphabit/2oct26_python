from django.contrib import admin
from django.utils.html import format_html_join
from myapp.models import ContactForm, QuoteRequest, Subscriber, Customer
from myapp.views import SERVICES
# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['created_at']


class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service', 'total_price', 'status', 'created_at']
    search_fields = ['name', 'email', 'service']
    list_filter = ['status', 'service', 'created_at']
    list_editable = ['status']
    # Admin can review the saved bill, but only change its approval status.
    readonly_fields = ['customer', 'name', 'email', 'service', 'selected_work',
                       'total_price', 'message', 'created_at']
    fields = ['customer', 'name', 'email', 'service', 'selected_work',
              'total_price', 'message', 'created_at', 'status']

    def selected_work(self, quote):
        for service in SERVICES.values():
            if service['name'] == quote.service:
                selected = quote.features.split(',')
                items = [(label, price) for code, label, price in service['features'] if code in selected]
                if items:
                    return format_html_join('<br>', '{} — ₹{}', items)
        return 'No priced features (older quotation)'

    selected_work.short_description = 'Bill items'

    def has_add_permission(self, request):
        return False


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    # Password hashes are deliberately not shown on the customer page.
    readonly_fields = ['first_name', 'last_name', 'email', 'phone_number']
    fields = ['first_name', 'last_name', 'email', 'phone_number']

    def has_add_permission(self, request):
        return False


admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(QuoteRequest, QuoteRequestAdmin)
admin.site.register(Subscriber)
admin.site.register(Customer, CustomerAdmin)
