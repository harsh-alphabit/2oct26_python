from django.contrib import admin
from myapp.models import ContactForm, QuoteRequest, Subscriber, Customer, WebsitePhoto
from myapp.views import SERVICES
# These classes tell Django what to show on each admin page.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['created_at']


class QuoteRequestAdmin(admin.ModelAdmin):
    # These columns appear on the quote list page.
    list_display = ['id', 'name', 'service', 'total_price', 'status', 'created_at']
    search_fields = ['name', 'email', 'service']
    list_filter = ['status', 'service', 'created_at']
    # Django makes Status a dropdown in the list. Click Save to store the change.
    list_editable = ['status']
    # Admin can read these quote details but cannot change them.
    readonly_fields = ['customer', 'name', 'email', 'service', 'selected_work',
                       'total_price', 'message', 'created_at']
    # Status is here but not in readonly_fields, so admin can change it.
    fields = ['customer', 'name', 'email', 'service', 'selected_work',
              'total_price', 'message', 'created_at', 'status']

    def selected_work(self, quote):
        # Build a readable list of the features chosen by this customer.
        for service in SERVICES.values():
            if service['name'] == quote.service:
                selected = quote.features.split(',')
                items = []
                for code, label, price in service['features']:
                    if code in selected:
                        items.append(f'{label}: ₹{price}')
                if items:
                    return ', '.join(items)
        return 'No priced features (older quotation)'

    # This name appears above the bill items on the quote detail page.
    selected_work.short_description = 'Bill items'

    def has_add_permission(self, request):
        # Quotes and customer accounts are created on the website.
        return False


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    # Do not show customer password hashes in admin.
    readonly_fields = ['first_name', 'last_name', 'email', 'phone_number']
    fields = ['first_name', 'last_name', 'email', 'phone_number']

    def has_add_permission(self, request):
        # Quotes and customer accounts are created on the website.
        return False


# Register these models so they appear in Django admin.
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(QuoteRequest, QuoteRequestAdmin)
# Admin gets a simple form with a place dropdown and photo upload field.
admin.site.register(WebsitePhoto)
admin.site.register(Subscriber)
admin.site.register(Customer, CustomerAdmin)
