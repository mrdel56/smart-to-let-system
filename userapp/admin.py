from django.contrib import admin

from .models import Role, UserInfo

# Register your models here.

admin.site.register(Role)
admin.site.register(UserInfo)
