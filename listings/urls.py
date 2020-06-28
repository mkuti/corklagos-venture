from django.urls import path
from .views import all_listings

app_name = 'listings'
urlpatterns = [
    path('', all_listings, name='listings'),
]
