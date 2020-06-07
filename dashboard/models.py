from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Extending Django User model by adding fields to the user
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    street_address = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30, blank=False)
    county = models.CharField(max_length=30, blank=False)
    eircode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.user.username
