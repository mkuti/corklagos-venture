from allauth.account.adapter import DefaultAccountAdapter


class SignupPopulatesUserAdapter(DefaultAccountAdapter):
    def save_user(self, request, profile, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        data = form.cleaned_data
        profile.business_name = data.get('business_name')
        profile.phone = data.get('phone')
        profile.eircode = data.get('eircode')
        profile.city = data.get('city')
        profile.street_address = data.get('street_address')
        profile.street_address2 = data.get('street_address2')
        profile.county = data.get('county')

        if 'password1' in data:
            profile.set_password(data['password1'])
        else:
            profile.set_unusable_password()
        if commit:
            profile.save()
        return profile
