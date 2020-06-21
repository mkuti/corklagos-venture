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
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # include all fields except for date since added automatically
        exclude = ['date']

    def __init__(self, *args, **kwargs):
        """
        Adding labels and classes
        """
        super().__init__(*args, **kwargs)  # call default init method to set form up
        labels = {
            'full_name': 'Please enter the name on the card',
            'street_address1': 'Street Address',
            'street_address2': 'Street Address (optional)',
            'postcode': 'Postcode',
            'city': 'City',
            'country': 'Country',
        }

        for field in self.fields:
            label = labels[field]
            self.fields[field].widget.attrs['placeholder'] = False
            self.fields[field].label = label
            self.fields[field].widget.attrs['class'] = 'form-control'
