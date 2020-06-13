from django.urls import path
from .views import get_and_create_listing, add_profile_details, view_and_edit_listing

urlpatterns = [
    path('', add_profile_details, name='editprofile'),
    path('addlisting/', get_and_create_listing, name='addlisting'),
    path('editlisting/<int:listing_id>', view_and_edit_listing, name='editlisting'),
]
