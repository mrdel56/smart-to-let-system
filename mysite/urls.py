from django.contrib import admin
from django.urls import path,include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("", include("properties.urls")),
    path("", include("profileapp.urls")),
]+ static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
