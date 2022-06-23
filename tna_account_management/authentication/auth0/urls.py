from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="auth_login"),
    path("logout/", views.logout, name="auth_logout"),
    path("logout/success/", views.logout_success, name="auth_logout_success"),
    path("authorize/", views.authorize, name="auth_authorize"),
    path("resend-email-verification/", views.resend_email_verification, name="auth_resend_email_verification"),
]
