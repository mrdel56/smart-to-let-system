from django.contrib import admin

from .models import Booking, Category, Location, Property, Review

# Register your models here.
# @admin.register(Property)
# class PropertyModelAdmin(admin.ModelAdmin):
#     list_display = ["price", "property_img"]


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Property)
# admin.site.register(PropertyOwner)
admin.site.register(Review)
admin.site.register(Booking)
