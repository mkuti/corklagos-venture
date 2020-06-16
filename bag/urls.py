from django.urls import path
from .views import view_bag, add_to_bag

urlpatterns = [
    path('', view_bag, name='view_bag'),
    path('add/<int:listing_id>', add_to_bag, name='add_to_bag')
]
