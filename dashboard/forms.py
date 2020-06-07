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
            'business_name': 'Business Name',
            'phone': 'Phone Number',
            'eircode': 'Eircode',
            'city': 'City',
            'street_address': 'Street Address',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['business_name'].widget.attrs['autofocus'] = True  # to force cursor to start in business name field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False
