from django.db import models
import uuid
from django.contrib.auth.models import User
from listings.models import Listing


class Order(models.Model):
    '''
    All the fields required
    from a customer which will go into database
    as normal billing details but also a date field for the date of the order.
    Add user field as a foreign key which would be associated with his orders.
    Any order associated can be called user.orders
    '''
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='orders')
    full_name = models.CharField(max_length=50, blank=False)
    street_address = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    total = models.IntegerField(blank=False, null=True)
    order_number = models.UUIDField(
        default=uuid.uuid4,
        editable=False)

    def __str__(self):
        '''
        Returns summary of the order
        format injecting information into a string
        '''
        return "{0}-{1}-{2}". format(
            self.order_number,
            self.date,
            self.full_name)


class OrderLineItem(models.Model):
    '''
    Creates a new table/model
    including the billing details information from Profile model
    including the listing information from model imported from listings.models
    including the quantity
    '''
    order = models.ForeignKey(
        Order,
        null=False,
        on_delete=models.CASCADE,
        related_name='orderitems')
    listing = models.ForeignKey(
        Listing,
        null=False,
        on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        '''
        Returns the quantity of products being bought,
        the listing name and listing price
        '''
        return "{0} {1} @ {2}".format(
            self.quantity,
            self.listing.listing_name,
            self.listing.listing_price)
