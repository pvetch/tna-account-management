from django.urls import path

from . import views

urlpatterns = [
    path("update-name", views.UpdateNameView.as_view(), name="update_name"),
    path("update-address", views.UpdateAddressView.as_view(), name="update_address"),
    path("verify-your-email", views.VerifyEmailView.as_view(), name="verify_email"),
    path("change-email", views.ChangeEmailView.as_view(), name="change_email"),
    path("change-password", views.ChangePasswordView.as_view(), name="change_password"),
    path("", views.AccountDashboardView.as_view(), name="dashboard"),
]
