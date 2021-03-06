from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        profile_form = UserProfileForm(
            request.POST, instance=profile, prefix="profile")
        if profile_form.is_valid():
            profile_form = profile_form.save()
            user = User.objects.get(email=user.email)
            user.first_name = request.POST['first_name']
            user.email = request.POST['email']
            user.save()
            user = User.objects.get(email=user.email)
            profile = UserProfile.objects.get(user=user)
            profile_form = UserProfileForm(prefix="profile", initial={
                'user': profile.user,
                'street_address1': profile.street_address1,
                'street_address2': profile.street_address2,
                'county': profile.county,
                'contact_number': profile.contact_number,
                'latitude': profile.latitude,
                'longitude': profile.longitude,                
            })
            context = {
                'profile_form': profile_form,
                'user': user
            }
        return render(request, 'profiles/profile.html', context)

    else:
        profile_form = UserProfileForm(prefix="profile", initial={
            'user': profile.user,
            'street_address1': profile.street_address1,
            'street_address2': profile.street_address2,
            'county': profile.county,
            'contact_number': profile.contact_number,
            'latitude': profile.latitude,
            'longitude': profile.longitude,
        })

        context = {
            'profile_form': profile_form,
            'user': user
        }
        return render(request, 'profiles/profile.html', context)
