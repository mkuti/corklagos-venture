from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    '''
    Extending Django User model by adding fields to the user
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.TextField(max_length=150, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    street_address = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=False)
    county = models.CharField(max_length=30, blank=False)
    eircode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        '''
        Connect create_user_profile & save_user_profile methods to User model, whenever a save event occurs
        '''
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()