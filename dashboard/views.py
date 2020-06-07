from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import EditProfileForm


# Create your views here.
@login_required
def profile(request):
    """ Display the member's profile after login. """
    profile = get_object_or_404(Profile, user=request.user)

    form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)
