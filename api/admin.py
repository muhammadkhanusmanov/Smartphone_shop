from django.contrib import admin
from .models import SmartPhone,Cart,Category
from django.contrib.auth.models import User

admin.site.register([SmartPhone,Cart,Category])