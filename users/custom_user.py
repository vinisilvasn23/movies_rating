from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import get_random_string


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault("username", get_random_string(30))
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
