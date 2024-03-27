from django.urls import path
from .views import ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path("forgot-password/", ForgotPasswordView.as_view()),
    path("reset-password/<str:user_id>/<str:token>/", ResetPasswordView.as_view(), name="reset_password"),
]
