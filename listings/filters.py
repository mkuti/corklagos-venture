import django_filters
from .models import Listing, Category, Make
from django import forms


class ListingFilter(django_filters.FilterSet):
    listing_category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect,
        empty_label="All",
        label='')
    listing_make = django_filters.ModelChoiceFilter(
        queryset=Make.objects.all(),
        widget=forms.RadioSelect,
        empty_label="All",
        label='')

    class Meta:
        model = Listing
        fields = ['listing_category', 'listing_make']
