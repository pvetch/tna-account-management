from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="auth_login"),
    path("logout/", views.logout, name="auth_logout"),
    path("authorize/", views.authorize, name="auth_authorize"),
]
