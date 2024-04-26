from django.urls import path

from . import views

urlpatterns = [
    path("", views.property_list, name="property_list"),
    # path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("<id>", views.property_details, name="property_details"),
    path("category/<slug:val>", views.category, name="category"),
    path("contact-owner/<id>", views.contact_owner, name="contact-owner"),
    path("property/add", views.add_property, name="add-property"),
    path("property/delete/<id>", views.delete_property, name="delete-property"),
    # path("location-list/", views.location_list, name="location-list"),
]
