from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from dashboard.forms import EditProfileForm
from dashboard.models import Profile


def checkout_details(request):
    '''
    If user has profile, get profile instance
    and display details on profile form.
    If not, profile_form is empty.
    '''
    try:
        profile = Profile.objects.get(user=request.user)
        profile_form = EditProfileForm(instance=profile)
    except ObjectDoesNotExist:
        profile_form = EditProfileForm()

    context = {
        'profile_form': profile_form,
    }

    return render(request, 'checkout.html', context)
