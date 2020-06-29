from django.shortcuts import render
from .models import Listing
from .filters import ListingFilter


def all_listings(request):
    """
    A view to show all listings and include filtered by category
    """
    listings = Listing.objects.filter(is_active=True)
    filtered_listings = ListingFilter(request.GET, queryset=listings)

    return render(request, "listings.html", {'filter': filtered_listings})
