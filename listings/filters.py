import django_filters
from .models import Listing, Category, Brand
from django import forms


class ListingFilter(django_filters.FilterSet):
    listing_category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect,
        empty_label="All",
        label='')
    listing_brand = django_filters.ModelChoiceFilter(
        queryset=Brand.objects.all(),
        widget=forms.RadioSelect,
        empty_label="All",
        label='')

    class Meta:
        model = Listing
        fields = ['listing_category', 'listing_brand']
