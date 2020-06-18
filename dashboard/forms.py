from django import forms
from .models import Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # include all fields except for user since this should never change
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adding placeholders and classes
        """
        super().__init__(*args, **kwargs)  # call default init method to set form up
        placeholders = {
            'business_name': 'Please enter your business name',
            'user_type': 'Please select the type of user',
            'phone': 'Phone Number',
            'eircode': 'Eircode',
            'city': 'City',
            'street_address': 'Street Address',
            'street_address2': 'Street Address 2',
            'county': 'County',
            'country': 'Country'
        }

        self.fields['business_name'].widget.attrs['autofocus'] = True  # to force cursor to start in business name field
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = False
            self.fields[field].label = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
