from django.shortcuts import render


def checkout_details(request):
    return render(request, 'checkout.html')

