from django.contrib import admin
from .models import User, Stats

#Accessing model from admin site
admin.site.register(User)
