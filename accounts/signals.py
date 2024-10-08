from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if kwargs.get("created", False):
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
