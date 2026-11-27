from django.contrib import admin
from django.utils.html import format_html_join
from myapp.models import ContactForm, QuoteRequest, Subscriber, Customer
from myapp.views import SERVICES
# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['created_at']


# ModelAdmin configures Django's built-in list and edit pages for quotations.
class QuoteRequestAdmin(admin.ModelAdmin):
    # list_display chooses the columns shown in the quotation table.
    list_display = ['id', 'name', 'service', 'total_price', 'status', 'created_at']
    search_fields = ['name', 'email', 'service']
    # These links filter the table; clicking a filter does not change any status.
    list_filter = ['status', 'service', 'created_at']
    # Show an editable status dropdown in each row of the list page.
    # Changing the dropdown alone does not save it: click the bottom Save button.
    # Django admin validates the submitted choices and saves the changed model rows.
    # We do not need a separate status-update function in views.py.
    list_editable = ['status']
    # Admin can review the saved bill, but only change its approval status.
    readonly_fields = ['customer', 'name', 'email', 'service', 'selected_work',
                       'total_price', 'message', 'created_at']
    # Opening a quote by its ID also shows status on the detail form.
    # It is editable because status is not in readonly_fields above.
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
# Connect the QuoteRequest model to the admin settings defined above.
admin.site.register(QuoteRequest, QuoteRequestAdmin)
admin.site.register(Subscriber)
admin.site.register(Customer, CustomerAdmin)
