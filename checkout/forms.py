from django import forms
from .models import OrderLineItem, Order


class MakePaymentForm(forms.Form):
    '''
    Create payment form to input credit card number
    First create choice fields for month and year expiry date
    required=False is to hide plain text and
    let Stripe encrypt card, as more secure
    stripe_id is created automatically and hidden from customer
    '''
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]

    credit_card_number = forms.CharField(
        label='Credit card number',
        required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month',
        choices=MONTH_CHOICES,
        required=False)
    expiry_year = forms.ChoiceField(
        label='Year',
        choices=YEAR_CHOICES,
        required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.Form):
    class Meta:
        model = Order
        # include all fields except for date since added automatically
        exclude = ('date')

    def __init__(self, *args, **kwargs):
        """
        Adding placeholders and classes
        """
        super().__init__(*args, **kwargs)  # call default init method to set form up
        placeholders = {
            'full_name': 'Please enter the name on the card',
            'street_address': 'Street Address',
            'street_address2': 'Street Address 2',
            'postcode': 'Postcode',
            'city': 'City',
            'country': 'Country'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True  # to force cursor to start in business name field
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = False
            self.fields[field].label = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
