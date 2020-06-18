from django.shortcuts import render
from dashboard.forms import EditProfileForm
from dashboard.models import Profile


def checkout_details(request):
    profile_form = EditProfileForm()

    context = {
        'profile_form': profile_form,
    }

    return render(request, 'checkout.html', context)

