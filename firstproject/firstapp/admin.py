from django.contrib import admin

from firstapp.models import Book, UserData

# Register your models here.
admin.site.register(UserData)
admin.site.register(Book)
