from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    categories = [
        ('engines', 'Engines'),
        ('gearboxes', 'Gear Boxes'),
        ('lamps', 'Lamps'),
        ('Radiators', 'radiators'),
        ('bumpers', 'Bumpers'),
    ]

    name = models.CharField(max_length=15, choices=categories, default='')

    def __str__(self):
        return self.name


class Listing(models.Model):
    brands = [
        ('', 'See all'),
        ('toyota', 'Toyota'),
        ('nissan', 'Nissan'),
        ('honda', 'Honda'),
    ]

    listing_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listing_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    listing_name = models.CharField(max_length=50)
    listing_description = models.TextField()
    listing_price = models.CharField(max_length=20)
    listing_image = models.ImageField(upload_to='images')
    listing_brand = models.CharField(max_length=10, choices=brands, default='')

    class Meta:
        ordering = ['listing_name']

    def __str__(self):
        return self.listing_name
