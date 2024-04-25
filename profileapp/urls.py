from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profile/", views.view_profile, name="view-profile"),
    path("edit-profile/", views.edit_profile, name="edit-profile"),
    path("my-properties/", views.my_properties, name="my-properties"),
    path("credits/", views.credits, name="credits"),
]
