from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from dashboard.models import Profile
from listings.models import Listing
from bag.contexts import bag_content
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order
import stripe


stripe.api_key = settings.STRIPE_SECRET


def checkout_details(request):
    '''
    If user manages to type url to access checkout
    and bag does not yet exist in session, redirect to view_bag.
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
    if not request.session.get('bag'):
        return redirect(reverse('view_bag'))

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
                customer = stripe.Charge.create(
                    # total multiplied by 100 as Stripe uses cents
                    amount=int(total * 100),
                    currency="EUR",
                    # who the payment came from on Stripe dashboard
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined!')

            if customer.paid:
                messages.error(request, 'You have successfully paid')
                request.session['bag'] = {}
                return render(request, 'payment_confirmed.html')
            else:
                messages.error(request, "Unable to take payment")

        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")

    try:
        profile = Profile.objects.get(user=request.user)
        print(profile.business_name)
        order_form = OrderForm(initial={
            'full_name': profile.business_name,
            'street_address': profile.street_address,
            'street_address2': profile.street_address2,
            'postcode': profile.postcode,
            'city': profile.city,
            'country': profile.country
        })
    except ObjectDoesNotExist:
        order_form = OrderForm()

    payment_form = MakePaymentForm()

    context = {
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE
    }

    return render(request, 'checkout.html', context)
