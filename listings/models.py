from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

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
