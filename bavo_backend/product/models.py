from django.db import models

from account.models import Profile


class Product(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description=models.TextField()
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_created=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)