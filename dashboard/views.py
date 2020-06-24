from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from listings.models import Listing, Category
from listings.forms import AddListingForm
from checkout.models import Order
from .forms import EditProfileForm
from .models import Profile


@login_required
def dashboard(request):
    '''
    Simple view for dashboard with two buttons
    to redirect to edit profile or add listing'''
    user = request.user
    previous_orders = user.orders.all()
    for order in previous_orders:
        print(order)

    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
        print(user_type)

        context = {
            'user_type': user_type,
            'previous_orders': previous_orders,
        }

        return render(request, 'dashboard.html', context)

    except Profile.DoesNotExist:
        return redirect(reverse('editprofile'))


@login_required
def add_profile_details(request):
    """ Welcome the member's profile after register.
    1. On post, try to confirm if profile exists for user logged in.
    If profile, use instance of profile to save the existing profile details.
    Except profile object does not exist, create new profile.
    2. On get, try to confirm if profile exists for user logged in.
    If profile, render form with existing details to edit.
    Except profile object does not exist, render blank form.
    """

    if request.method == 'POST':
        try:
            profile = Profile.objects.get(user=request.user)
            edit_profile = EditProfileForm(request.POST, instance=profile)
            if edit_profile.is_valid():
                profile.save()
                messages.success(request, 'Your profile has been updated')
                if profile.user_type == 'dismantler':
                    return redirect(reverse('addlisting'))
                else:
                    return redirect(reverse('listings'))
        except ObjectDoesNotExist:
            profile_form = EditProfileForm(request.POST)
            if profile_form.is_valid():
                profile = Profile.objects.create(
                    user=request.user,
                    user_type=profile_form.cleaned_data['user_type'],
                    business_name=profile_form.cleaned_data['business_name'],
                    phone=profile_form.cleaned_data['phone'],
                    postcode=profile_form.cleaned_data['postcode'],
                    city=profile_form.cleaned_data['city'],
                    street_address=profile_form.cleaned_data['street_address'],
                    street_address2=profile_form.cleaned_data['street_address2'],
                    county=profile_form.cleaned_data['county'],
                    country=profile_form.cleaned_data['country'],
                )
                profile.save()
                messages.success(request, 'Your profile has been saved')
                if profile.user_type == 'dismantler':
                    print(profile.user_type)
                    return redirect(reverse('addlisting'))
                else:
                    return redirect(reverse('listings'))
    else:
        try:
            profile = Profile.objects.get(user=request.user)
            profile_form = EditProfileForm(instance=profile)
        except ObjectDoesNotExist:
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
    categories = Category.objects.all()

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
            messages.success(request, 'Thank you. We have recorded your new listing')
    else:
        addform = AddListingForm()

    context = {
        'addform': addform,
        'listings': user_listings,
        'categories': categories
    }
    return render(request, 'addlisting.html', context)


@login_required
def view_and_edit_listing(request, listing_id):
    """
    Display individual listing details
    Form to edit details if needed
    """
    categories = Category.objects.all()
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.method == 'POST':
        editform = AddListingForm(request.POST, request.FILES, instance=listing)
        if editform.is_valid():
            listing.save()
            messages.success(request, 'Thank you. Your listing has been updated')
    else:
        editform = AddListingForm(instance=listing)

    context = {
        'editform': editform,
        'listing': listing,
        'categories': categories
    }
    return render(request, 'editlisting.html', context)


@login_required
def delete_listing(request, listing_id):
    """ Allow user to delete his own listing from the database """
    listing = get_object_or_404(Listing, pk=listing_id)

    listing.delete()
    messages.success(request, 'Your listing has been removed from the database.')

    return redirect(reverse('addlisting'))
