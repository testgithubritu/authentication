from django.contrib import admin

# Register your models here.
from . models import UserProfile,loginTable

admin.site.register(UserProfile)
admin.site.register(loginTable)
