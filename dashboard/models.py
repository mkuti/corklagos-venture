from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    '''
    Extending Django User model by adding fields to the user
    '''

    user_type = [
        ('dismantler', 'Irish dismantler'),
        ('dealer', 'Car dealer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15, choices=user_type, default='')
    business_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    street_address = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30, blank=False)
    county = models.CharField(max_length=30, blank=False)
    eircode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f'{self.user.username} Profile'
