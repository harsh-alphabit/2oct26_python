from django.contrib import admin
from myapp.models import user_signup


class user_signup_admin(admin.ModelAdmin):
    list_display=['name','email','mobile','address']

admin.site.register(user_signup,user_signup_admin)
