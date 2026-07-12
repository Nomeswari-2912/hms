from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="accounts_home"),
    path("register/", views.register, name="accounts_register"),
    path("logout/", views.logout_view, name="accounts_logout"),
]
