from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def view_bag(request):
    return render(request, 'bag.html')


def add_to_bag(request, listing_id):
    '''
    If user is not logged in, redirect to login page.
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
        bag[listing_id] = listing_quantity
        request.session['bag'] = bag
        messages.success(request, 'We have added the listing to your bag')
        return redirect(redirect_url)
    messages.error(request, 'Please log in to buy a listing')
    return redirect(reverse('account_login'))


def remove_from_bag(request, listing_id):
    """Remove the listing from the shopping bag"""

    bag = request.session.get('bag', {})

    bag.pop(listing_id)
    messages.success(request, 'We have removed the listing from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
