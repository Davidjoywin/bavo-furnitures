from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    date_created = models.DateField(auto_created=True)

    def __str__(self):
        return self.username
    