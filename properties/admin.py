from django.contrib import admin

from .models import Category, Property


# Register your models here.
@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ["category", "space", "address", "price", "property_img"]


admin.site.register(Category)
