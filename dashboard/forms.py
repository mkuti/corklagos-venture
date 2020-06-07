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
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_business_name': 'Business Name',
            'default_phone': 'Phone Number',
            'default_eircode': 'Eircode',
            'default_city': 'City',
            'default_street_address': 'Street Address',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False
