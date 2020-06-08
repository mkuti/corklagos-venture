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

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=15, choices=categories)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
