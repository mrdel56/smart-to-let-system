from django.urls import path

from . import views

urlpatterns = [
    path('view-profile/', views.view_profile, name = 'view-profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
]