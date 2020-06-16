from django.shortcuts import get_object_or_404
from listings.models import Listing
from django.conf import settings


def bag_content(request):
    total = 0
    bag_items = []
    product_count = 0

    context = {
        total,
        bag_items,
        product_count
    }
    return {context}
