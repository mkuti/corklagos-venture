from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from listings.models import Listings
from listings.forms import AddListingForm


# Create your views here.
@login_required
def getandcreatelisting(request, pk=None):
    """ Display the member's profile after login.
    Display current listings
    Render form to add a new listing """
    user = request.user
    user_listings = Listings.objects.filter(listing_owner=user)

    if request.method == 'POST':
        form = AddListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddListingForm()

    context = {
        'form': form,
        'listings': user_listings
    }
    return render(request, 'profile.html', context)
