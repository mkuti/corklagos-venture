from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from listings.models import Listings
from listings.forms import AddListingForm


# Create your views here.
@login_required
def create_or_edit_listing(request, pk=None):
    """ Display the member's profile after login.
    Display current listings
    Render form to add a new listing """
    listing = get_object_or_404(Listings, pk=pk) if pk else None

    if request.method == 'POST':
        form = AddListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            listing = form.save()
    else:
        form = AddListingForm(instance=listing)

    context = {
        'form': form
    }
    return render(request, 'profile.html', context)
