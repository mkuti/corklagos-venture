from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dashboard.models import Profile


@login_required
def view_bag(request):
    '''
    If user is a dismantler user type, redirect to listings page.
    Otherwise render bag.html to view shopping bag
    where general context will be displayed
    '''

    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type

        if user_type == 'dismantler':
            messages.error(
                request,
                'You do not have the correct profile to shop')
            return redirect(reverse('listings'))

        return render(request, 'bag.html')

    except Profile.DoesNotExist:
        return render(request, 'bag.html')


def add_to_bag(request, listing_id):
    '''
    If user is not logged in, redirect to login page.
    If user is a dismantler user type, throw an error message.
    Setting quantity of item to 1 as one single item available.
    Getting bag if already exists or initializing it to empty dictionary
    Add listing ID with its fixed quantity
    Store bag in current user session
    Redirect to listings when listing added
    '''
    listing_quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            user_type = profile.user_type

            if user_type == 'dismantler':
                messages.error(
                    request,
                    'You do not have the correct profile to shop')
                return redirect(redirect_url)
            else:
                bag[listing_id] = listing_quantity
                request.session['bag'] = bag
                messages.success(
                    request,
                    'We have added the listing to your bag')
                return redirect(redirect_url)

        except Profile.DoesNotExist:
            messages.warning(
                request,
                'Please add your profile details before shopping.')
            return redirect(reverse('editprofile'))

    messages.error(request, 'Please log in to buy a listing')
    return redirect(reverse('account_login'))


def remove_from_bag(request, listing_id):
    """Remove the listing from the shopping bag"""

    bag = request.session.get('bag', {})

    bag.pop(listing_id)
    messages.success(request, 'We have removed the listing from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
