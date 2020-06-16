from django import forms
from .models import Listing


class AddListingForm(forms.ModelForm):
    '''
    Form to be displayed for the dismantler user on dashboard
    to add a listing which will be rendered on listings page
    All fields of the model to be used
    '''
    class Meta:
        model = Listing
        exclude = ['listing_owner']

    def __init__(self, *args, **kwargs):
        """
        Adding placeholders and classes
        """
        super().__init__(*args, **kwargs)  # call default init method to set form up
        labels = {
            'listing_name': 'Please provide the name:',
            'listing_description': 'Please provide a brief description of the car part:',
            'listing_price': 'Please enter the price of the car part',
            'listing_image': 'Please upload an image of your product:',
            'listing_category': 'Please select the category:',
            'listing_brand': 'Please select the brand:',
        }

        self.fields['listing_name'].widget.attrs['autofocus'] = True  # to force cursor to start in listing name field

        for field in self.fields:
            label = labels[field]
            self.fields[field].widget.attrs['placeholder'] = False
            self.fields[field].label = label
            self.fields[field].widget.attrs['class'] = 'form-control'
