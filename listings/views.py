from django.shortcuts import render
from .models import Listing


def all_listings(request):

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }

    return render(request, "listings.html", context)
