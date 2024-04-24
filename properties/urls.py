from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.home),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
   #path("location-list/", views.location_list, name="location-list"),
   path("add-property/", views.add_property, name="add-property"),
=======
    path("", views.property_list, name="property_list"),
    # path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("<id>", views.property_details, name="property_details"),
    path("category/<slug:val>", views.category, name="category"),
    path("location-list/", views.location_list, name="location-list"),
>>>>>>> 8d67a2f33ec96502128f67916a21890dcb816d86
]
