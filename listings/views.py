from django.shortcuts import render


# Create your views here.
def all_listings(request):
    return render(request, "listings.html")
