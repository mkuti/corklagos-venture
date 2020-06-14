import django_filters
from .models import Listing, Category
from django import forms


class ListingFilter(django_filters.FilterSet):
    listing_category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect,
        label=None)

    class Meta:
        model = Listing
        fields = ['listing_category']
