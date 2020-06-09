from django.db import models


class Listings(models.Model):
    categories = [
        ('', 'See all'),
        ('engines', 'Engines'),
        ('gearboxes', 'Gear Boxes'),
        ('lamps', 'Lamps'),
        ('Radiators', 'radiators'),
        ('bumpers', 'Bumpers'),
    ]

    brands = [
        ('', 'See all'),
        ('toyota', 'Toyota'),
        ('nissan', 'Nissan'),
        ('honda', 'Honda'),
    ]

    listing_name = models.CharField(max_length=50)
    listing_description = models.TextField()
    listing_price = models.DecimalField(max_digits=6, decimal_places=2)
    listing_image = models.ImageField(upload_to='images')
    listing_category = models.CharField(max_length=15, choices=categories, default='')
    listing_brand = models.CharField(max_length=10, choices=brands, default='')

    class Meta:
        ordering = ['listing_name']

    def __str__(self):
        return self.listing_name
