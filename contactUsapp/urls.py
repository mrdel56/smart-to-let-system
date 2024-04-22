from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact_form, name="contact_form"),
    path("contact/success/", views.contact_success, name="contact_success"),
]
