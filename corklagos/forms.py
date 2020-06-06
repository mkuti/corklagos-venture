from allauth.account.forms import SignupForm
from django import forms
# from dashboard.models import Profile


class CustomSignupForm(SignupForm):
    business_name = forms.CharField(max_length=50, label='Your business name')
    phone = forms.CharField(max_length=20, label='Your phone number')
    street_address = forms.CharField(max_length=50, label='Address line 1')
    street_address2 = forms.CharField(max_length=50, label='Address line 2')
    city = forms.CharField(max_length=30, label='City')
    eircode = forms.CharField(max_length=20, label='Eircode')
    county = forms.CharField(max_length=30, label='County')

    def signup(self, request, user):
        user.business_name = self.cleaned_data['business_name']
        user.save()
        return user

