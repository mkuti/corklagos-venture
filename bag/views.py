from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_bag(request):
    return render(request, 'bag.html')


def add_to_bag(request, listing_id):
    listing_quantity = 1
    bag = request.session.get('bag', {})

    bag[listing_id] = bag.get(listing_id, listing_quantity)

    request.session['bag'] = bag

    return redirect(reverse('listings'))
