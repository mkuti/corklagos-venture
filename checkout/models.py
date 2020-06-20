from django.db import models
from dashboard.models import Profile
from listings.models import Listing


class OrderLineItem(models.Model):
    '''
    Creates a new table/model
    including the billing details information from Profile model
    including the listing information from model imported from listings.models
    including the quantity
    including the date
    '''
    billing = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    date = models.DateField()

    def __str__(self):
        '''
        Returns the quantity of products being bought,
        the listing name and listing price
        '''
        return "{0} {1} @ {2}".format(
            self.quantity,
            self.listing.name,
            self.listing.price)
