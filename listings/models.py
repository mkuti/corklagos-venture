from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Category(models.Model):
    '''
    Setting all categories which are related to the Listing model.
    '''
    class Meta:
        verbose_name_plural = 'Categories'

    categories = [
        ('Engines', 'engines'),
        ('Gear Boxes', 'gearboxes'),
        ('Lamps', 'lamps'),
        ('Radiators', 'radiators'),
        ('Bumpers', 'bumpers'),
    ]

    name = models.CharField(max_length=15, choices=categories, null=False)

    def __str__(self):
        return self.name


class Make(models.Model):
    '''
    Setting all brands which are related to the Listing model.
    '''
    makes = [
        ('Toyota', 'toyota'),
        ('Nissan', 'nissan'),
        ('Honda', 'honda'),
    ]

    name = models.CharField(max_length=15, choices=makes, null=False)

    def __str__(self):
        return self.name


class Listing(models.Model):
    '''
    Including 3 fields related to other models.
    User who owns the listing.
    Category in which listing belongs.
    Make of the listing.
    Added a validator on the listing price to avoid negative price.
    Ordering alphabetically the listings by name.
    '''
    listing_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True)
    listing_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True)
    listing_make = models.ForeignKey(
        Make,
        on_delete=models.SET_NULL,
        null=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    listing_name = models.CharField(max_length=50)
    listing_description = models.TextField()
    listing_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(20.00)])
    listing_image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['listing_name']

    def __str__(self):
        return self.listing_name
