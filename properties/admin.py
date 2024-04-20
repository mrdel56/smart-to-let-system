from django.contrib import admin
from .models import Property
# Register your models here.
@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'space', 'address', 'price', 'property_img']