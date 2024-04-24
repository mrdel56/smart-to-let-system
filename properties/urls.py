from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
   #path("location-list/", views.location_list, name="location-list"),
   path("add-property/", views.add_property, name="add-property"),
]
