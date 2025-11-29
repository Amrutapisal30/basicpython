from django.contrib import admin

from ecommapp.models import Product, UserData

# Register your models here.
admin.site.register(UserData)
admin.site.register(Product)