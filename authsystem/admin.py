from django.contrib import admin

# Register your models here.

from .models import CustomModel

admin.site.register(CustomModel)