from django.urls import path
from .views import (
    dashboard,
    add_profile_details,
    get_and_create_listing,
    view_and_edit_listing,
    delete_listing
)

urlpatterns = [
    path(
        '',
        dashboard,
        name='dashboard'),
    path(
        'profile/',
        add_profile_details,
        name='editprofile'),
    path(
        'addlisting/',
        get_and_create_listing,
        name='addlisting'),
    path(
        'editlisting/<int:listing_id>',
        view_and_edit_listing, name='editlisting'),
    path(
        'deletelisting/<int:listing_id>',
        delete_listing, name='deletelisting'),
]
