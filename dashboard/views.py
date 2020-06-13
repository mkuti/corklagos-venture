from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from listings.forms import AddListingForm
from .forms import EditProfileForm
from .models import Profile


@login_required
def add_profile_details(request):
    """ Welcome the member's profile after register.
    Render form to add profile details """
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST)
        if profile_form.is_valid():
            profile = Profile.objects.create(
                user=request.user,
                business_name=profile_form.cleaned_data['business_name'],
                phone=profile_form.cleaned_data['phone'],
                eircode=profile_form.cleaned_data['eircode'],
                city=profile_form.cleaned_data['city'],
                street_address=profile_form.cleaned_data['street_address'],
                street_address2=profile_form.cleaned_data['street_address2'],
                county=profile_form.cleaned_data['county'],
            )
            profile.save()
            return redirect(reverse('addlisting'))
    else:
        profile_form = EditProfileForm()

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)


@login_required
def get_and_create_listing(request):
    """ Display the member's profile after login.
    Display current listings
    Render form to add a new listing """
    user = request.user
    user_listings = Listing.objects.filter(listing_owner=user)

    if request.method == 'POST':
        addform = AddListingForm(request.POST, request.FILES)
        if addform.is_valid():
            listing = Listing.objects.create(
                listing_owner=user,
                listing_name=addform.cleaned_data['listing_name'],
                listing_description=addform.cleaned_data['listing_description'],
                listing_price=addform.cleaned_data['listing_price'],
                listing_image=request.FILES['listing_image'],
                listing_category=addform.cleaned_data['listing_category'],
                listing_brand=addform.cleaned_data['listing_brand'],
            )
            listing.save()
    else:
        addform = AddListingForm()

    context = {
        'addform': addform,
        'listings': user_listings
    }
    return render(request, 'addlisting.html', context)


@login_required
def view_and_edit_listing(request, listing_id):
    """
    Display individual listing details
    Form to edit details if needed
    """
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.method == 'POST':
        editform = AddListingForm(request.POST, request.FILES, instance=listing)
        if editform.is_valid():
            listing.save()
    else:
        editform = AddListingForm(instance=listing)

    context = {
        'editform': editform,
        'listing': listing
    }
    return render(request, 'editlisting.html', context)


@login_required
def delete_listing(request, listing_id):
    """ Allow user to delete his own listing from the database """
    listing = get_object_or_404(Listing, pk=listing_id)

    listing.delete()

    return redirect(reverse('addlisting'))
