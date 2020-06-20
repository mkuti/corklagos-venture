from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import Profile
from listings.models import Listing
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order
from django.conf import settings
from django.utils import timezone
import stripe


stripe_api_key = settings.STRIPE_SECRET


def checkout_details(request):
    '''
    If user has profile, get profile instance
    and display details of profile on OrderForm.
    If not, OrderForm is displayed blank to fill.
    Import MakePaymentForm and added as argument.
    On post, if forms are valid, save() with commit=False,
    which creates a new order
    Getting bag if already exists or initializing it to empty dictionary
    Via the cart_items, we get listing id which gives us Listing information
    One line item to resume the order which we save
    '''
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            bag = request.session.get('bag', {})
            total = 0
            for listing_id, listing_quantity in bag.items():
                listing = get_object_or_404(Listing, pk=listing_id)
                total += listing_quantity * listing.listing_price
                order_line_item = OrderLineItem(
                    order=order,
                    listing=listing,
                    quantity=listing_quantity
                )
                order_line_item.save()

    try:
        profile = Profile.objects.get(user=request.user)
        order_form = OrderForm(instance=profile)
    except ObjectDoesNotExist:
        order_form = OrderForm()

    payment_form = MakePaymentForm()

    context = {
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE}
    }

    return render(request, 'checkout.html', context)

 