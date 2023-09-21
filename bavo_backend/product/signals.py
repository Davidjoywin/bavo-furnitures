from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Cart
from account.models import Profile


@receiver(post_save, sender=Profile)
def create_cart(sender, instance, created, **kwargs):
    if created:
        print(created)
        print(instance)
        Cart.objects.create(user=instance)

def save_cart(sender, created, instance, **kwargs):
    instance.profile.save()