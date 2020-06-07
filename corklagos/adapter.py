from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_username, user_email, user_field

class SignupPopulatesUserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        data = form.cleaned_data
        business_name = data.get('business_name')
        phone = data.get('phone')
        eircode: data.get('eircode')
        city: data.get('city')
        street_address: data.get('street_address')
        street_address2: data.get('street_address2')
        county: data.get('county')

        user_email
        user_username
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return DefaultAccountAdapter.save_user(self, request, user, form)
