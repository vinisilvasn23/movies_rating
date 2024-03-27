from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .forms import ForgotPasswordForm, ResetPasswordForm
from django.template.loader import render_to_string
from django.shortcuts import render


class ForgotPasswordView(APIView):
    def post(self, request):
        form = ForgotPasswordForm(request.data)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                forgot_password_url = (
                    f"http://127.0.0.1:8000/api/reset-password/{user.id}/{token}"
                )

                message = render_to_string(
                    "forgot_password_email.html",
                    {"forgot_password_url": forgot_password_url},
                )

                send_mail(
                    "Recuperação de senha",
                    "",
                    settings.EMAIL_HOST_USER,
                    [email],
                    html_message=message,
                    fail_silently=False,
                )

                return Response(
                    {"message": "A password recovery email has been sent."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "There is no user associated with this email."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(View):
    def get(self, request, user_id, token):
        return render(request, "reset_password.html", {"user_id": user_id, "token": token})

    def post(self, request, user_id, token):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data["password"]
            userFound = User.objects.filter(id=user_id).first()
            user = default_token_generator.check_token(userFound, token)
            if user is not None:
                userFound.set_password(new_password)
                userFound.save()
                return render(request, "password_reset_success.html")
            else:
                return Response(
                    {"error": "Invalid Token"}, status=status.HTTP_403_FORBIDDEN
                )
        return render(request, "reset_password.html", {"form": form, "token": token})
