from django.urls import path

from . import views

urlpatterns = [
    path("credit-package-list/", views.credit_package_list, name="credit-package-list"),
    path("buy-credits/", views.add_transaction, name="buy-credits"),
]
