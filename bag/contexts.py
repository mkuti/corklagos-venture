from django.shortcuts import get_object_or_404
from listings.models import Listing


def bag_content(request):
    '''
    Request existing bag if there is one, or blank dictionary if none
    Set total, bag_items and product_count to 0.
    Iterate through all items in shopping bag
    Multiply quantity of item by price
    Add this to continuous running total of cost
    Product_count keeps on adding the quantity
    Append a dictionary to bag_items to display all details of listing
    '''
    bag = request.session.get('bag', {})

    total = 0
    bag_items = []
    product_count = 0

    for listing_id, listing_quantity in bag.items():
        listing = get_object_or_404(Listing, pk=listing_id)
        total += listing_quantity * listing.listing_price
        product_count += listing_quantity
        bag_items.append({
            'listing_id': listing_id,
            'quantity': listing_quantity,
            'listing': listing
            })
    context = {
        "total": total,
        "bag_items": bag_items,
        "product_count": product_count,
    }
    return(context)
