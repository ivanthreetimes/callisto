from django.db.models.signals import post_save
from django.dispatch import receiver

from callisto.auth_app.models import AppUser
from callisto.main_app.models import Profile


@receiver(post_save, sender=AppUser)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AppUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
