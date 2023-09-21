from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        swappable = "AUTH_PROFILE_MODEL"

    def __str__(self):
        return self.username
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create(username, email, password, **extra_fields)


    