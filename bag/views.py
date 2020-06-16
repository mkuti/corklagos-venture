from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_bag(request):
    return render(request, 'bag.html')


def add_to_bag(request, listing_id):
    '''
    If user is not logged in, redirect to login page.
    Setting quantity of item to 1 as one single item available.
    Check if bag exists, if not create it.
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
