<h1 align="center">
  <a href="https://corklagos-venture.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/X2x8rHN/Screenshot-2020-06-29-at-2-58-53-PM.png" alt="Multi Device Mockup"/></a>
</h1>

<div align="center">
<a href="https://corklagos-venture.herokuapp.com/" target="_blank"><img src="static/images/logo.png" width='200' height='150' alt="logo"></a>
</div>

<div align="center">
    <h2>Testing document</h2>
</div>

## Table of Contents

- [Final and official testing:](#final-and-official-testing-)
- [General testing:](#general-testing-)
- [Testing in different browsers:](#testing-in-different-browsers-)
- [Issues found and solved](#issues-found-and-solved)
  * [1. SignUp form](#1-signup-form)
  * [2. Migrating models with ForeignKey](#2-migrating-models-with-foreignkey)
  * [3. Filter on listings page](#3-filter-on-listings-page)
  * [4. Styling of django-filter fields](#4-styling-of-django-filter-fields)
  * [5. Add to bag](#5-add-to-bag)
  * [6. Login url redirect](#6-login-url-redirect)
  * [7. View shopping bag](#7-view-shopping-bag)
  * [8. Remove from shopping bag](#8-remove-from-shopping-bag)
  * [9. Edit user profile](#9-edit-user-profile)
  * [10. Profile details used for orderform](#10-profile-details-used-for-orderform)
  * [11. OrderForm not rendered](#11-orderform-not-rendered)
  * [12. Payment throwing error](#12-payment-throwing-error)
  * [13. View created orders in admin site](#13-view-created-orders-in-admin-site)
  * [14. Static not showing on development mode](#14-static-not-showing-on-development-mode)
  * [15. User not re-directed to edit profile](#15-user-not-re-directed-to-edit-profile)
  * [16. User verification of email address](#16-user-verification-of-email-address)
  * [17. Views import line too long](#17-views-import-line-too-long)
  * [18. Display past orders](#18-display-past-orders)
  * [19. Error after collectstatic](#19-error-after-collectstatic)
  * [20. Logout button with JS](#20-logout-button-with-js)
  * [21. Invalid email address on contactform](#21-invalid-email-address-on-contactform)
  * [22. Placeholder and required not working on textarea](#22-placeholder-and-required-not-working-on-textarea)
  * [23. Edit profile form](#23-edit-profile-form)
  * [24. AddListing form pre-filled after adding a listing](#24-addlisting-form-pre-filled-after-adding-a-listing)
  * [25. Login and register error messages](#25-login-and-register-error-messages)
  * [26. Buttons styling issues on Safari](#26-buttons-styling-issues-on-safari)
  * [27. Page left banner stretched](#27-page-left-banner-stretched)
  * [28. No message for user when filter returns nothing](#28-no-message-for-user-when-filter-returns-nothing)
  * [29. Listings images stretched](#29-listings-images-stretched)
  * [30. Negative price on adding a listing](#30-negative-price-on-adding-a-listing)
  * [31. Car dealer adding a listing](#31-car-dealer-adding-a-listing)
  * [32. Car dismantler buying a listing](#32-car-dismantler-buying-a-listing)
  * [33. Overflow/responsiveness](#33-overflow-responsiveness)
- [Other issues found but yet unsolved](#other-issues-found-but-yet-unsolved)
  * [1.](#1)

## Final and official testing:
  * [W3 MarkUp validation](https://validator.w3.org)
  * [W3 CSS validation](https://jigsaw.w3.org/css-validator/)
  * [JS validator](https://jshint.com/)
  * [PEP8 Python Validator](http://pep8online.com)

I checked the validity of my code and the browser various pages at different times and received few errors on HTML markup which I worked on correcting. I did not get any errors with my CSS.

For Javascript, I did get errors for 'const' or 'let being available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz) or "Missing semicolon" but chose to ignore as not anymore a requirement in ES6.

For Python, I ran python3 manage.py flake8 in my terminal and received a list of errors which I worked to clear on each django app. I removed all the unused python files for testing, admin or models. The other main errors were lines being too long which I have all corrected and "Missing namespace in urls include()". I have tried to correct this one by following the suggestion of adding a namespace and an app_name for each included module but the app then failed in Heroku and I did not find any solution to clear the error and avoid the build failing in Heroku. So this can be considered an unsolved bug. Finally there are 4 lines being too long on the django project settings.py but this is not a code written by me and while it was been reported to Django [here](https://code.djangoproject.com/ticket/28163), Django has chosen not to fix it. 

## General testing:
As I did not have a lot of time and I was not really expert in Jasmine or any automated testing, I decided to do all the testing manually via the browser, Chrome Developer tools and testing each feature one by one.
My strategy is very simple: as soon as I write a line of code, I open the page in my browser to test it, make sure it works until I am fully happy with what I see and how it functions. After the whole project was written and working, I went back to each feature and re-tested it to ensure nothing I added made it fail later. I also asked people in Slack community to test the website for me. 

Through my own testing and with views of others, I have fixed a lot of design flaws and numerous bugs in my Python code. Thanks to that, I can present a website which looks professional and is valid.

## Testing in different browsers:
I used Google Chrome as my primary browser and constantly tested it on my mobile phone also using the same browser. 
I also tested the website on Safari via an iMac with a very big screen, on an iPhone XR and an iPod touch with probably the smallest screen regularly and never found any specific issue. 

## Issues found and solved

### 1. SignUp form
* __Issue__: Probably less an issue than a failed attempt to customise the signup form and the user model so the user has a profile created when signing up with more details than the regular Django-allauth signup form. I searched and started to implement a custom model with adapter, a custom signup form which was working but could not save the details of the profile when user created. After spending much time on it and seeking help from Slack and Tutor Support, decided to go with the easier method of redirecting the user to create a profile after they have already signed up.
* __Fix__: Created a new app called dashboard where the user is redirected to add his business details after confirming his email address (redirect is configurated in settings.py with ```ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/dashboard/')```).
* __Verdict__: Although it takes three steps rather than one, the user can get a profile created which is associated with the user model by a OneToOneField. 
* __Future fix__: After project's evaluation, will come back to this and try to have a customised user model with a custom signup form.

### 2. Migrating models with ForeignKey
* __Issue__: Non-nullable field and default value for ForeignKey ```You are trying to add a non-nullable field new_field to ... without a default. We can't do that (the database needs something to populate existing rows).```. 
* __Fix__: Found beginning of explanation [here](https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a) and with the help of [Chris Z.](https://github.com/ckz8780) on Slack, I found out that it was easier to add ```null=True``` when migrating to avoid this error. Because I had set a wrong default in "makemigrations", I had to cancel the previous migrations so ```python3 manage.py migrate``` would work.
* __Verdict__: Managed to migrate the models with ForeignKey without any further issue.

### 3. Filter on listings page
* __Issue__: Implementing the filter on listings page. I was stuck for a few hours, trying to understand how to use a queryset to filter the listings with category and car make. I could get the categories and makes to render and did try to set up a filter in my views but did not filter any results when testing it.
* __Fix__: After searching more, found the django-filter package and a great article explaining its features, followed the documentation and created a filters.py in my listings app to implement filter and have a for loop with queryset (qs) argument on the html template to show listings depending of the filter queried.
*__Resources__: 
- [Django-Filter documentation](https://django-filter.readthedocs.io/en/stable/index.html)
- [Simple is better than complex](https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html)
* __Verdict__: Filters listings by category or car make. I would like to make it even better by removing the button.

### 4. Styling of django-filter fields
* __Issue__: Format of the django-filter fields not looking great.
* __Fix__: 
- Specify the type of format for the filter: specifically ```widget=forms.RadioSelect```
- Render the filter form by field so I could control the classes and the bootstrap columns using ```{{ filter.form.listing_category|as_crispy_field }}```
- Removed the automatic label from django-filter: ```label=''```
*__Resources__: 
- [Add custom css class to Django-filter fields](https://stackoverflow.com/questions/50175858/django-add-atributes-to-filter-fields)
- [Render filter.form as field](https://django-crispy-forms.readthedocs.io/en/latest/api_templatetags.html)
- [Removing label for form](https://django-filter.readthedocs.io/en/stable/ref/filters.html?highlight=label#label)
* __Verdict__: Filter feature fits the rest of the website design.

### 5. Add to bag
* __Issue__: Add to bag template tag causing error: ```Argument ‘’ is not accepted```.
* __Fix__: Changed listing_id to listing.id as listing_id does not exist as I could see in print().
* __Verdict__: Listing gets added to the bag without error.

* __Issue__: On bag/contexts.py, error: "unsupported operand type(s) for +=: 'int' and 'str'" when adding to bag.
* __Fix__: Found [here](https://stackoverflow.com/questions/2376464/typeerror-unsupported-operand-types-for-str-and-int) a beginning of solution. Confirmed that listing_quantity was int. Remembered that listing_price was not using decimal field
Changed to decimal field and worked.
* __Verdict__: Adding to bag is successful.

### 6. Login url redirect
* __Issue__: Login url for redirect causing error.
* __Fix__: Go to [allauth doc](https://django-allauth.readthedocs.io/en/latest/views.html?highlight=login%20url#login-account-login) and found the correct name: ```account_login```.
* __Verdict__: Redirect works.

### 7. View shopping bag
* __Issue__: Item list not showing on bag.html inside the loop.
* __Fix__: Investigate result of bag_items only by printing in terminal inside views.py. Checked again the contexts.py and see how listing object could be accessed. After iterating bag_items and setting variable of item, need to call the actual object before calling its attributes: ```{{ item.listing.listing_price}}```.
* __Verdict__: Could see the listings in the bag template.

### 8. Remove from shopping bag
* __Issue__: On bag template, when user clicks on the remove button, error comes up: ```Argument ‘,’ is not accepted```
* __Fix__: I had it ```{% url 'remove_from_bag' item.listing_id %}``` then tried to change it as the rest of listing details: ```{{ item.listing.listing_id}}``` but same error. I then checked context.py and found that listing_id is saved as its own argument when appended to bag_items(). So I could call item.listing_id directly. 
* __Verdict__: Triggered another error ```KeyError at /cart/remove/1```

* __Issue__: ```KeyError at /cart/remove/1``` after clicking on removing item from bag
* __Fix__: Changed url to 'remove/<listing_id>' instead of ‘remove/<int:listing_id>'
Item removed from bag as I could find [in this Slack thread](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1589041701161300)
* __Verdict__: Removed successfully the listing from the bag

### 9. Edit user profile
* __Issue__: 404 error with if statement on get_object_or_404 on dashboard/views.py when trying to use instance of profile in EditProfileForm if profile exists
* __Fix__: Replaced get_object_or_404 by try/except statement to get profile instance (Profile.objects.get(user=request.user)) and except ObjectDoesNotExist
* __Verdict__: Confirmed that the profile details show on profile.html when profile exists already for user in session

### 10. Profile details used for orderform
* __Issue__: ```__init__() got an unexpected keyword argument 'instance'``` when rendering checkout page
* __Fix__: Trying to display profile details if exists by adding instance argument when instantiating the form
Try/except worked with EditProfileForm but when using OrderForm. Replaced instance by initial as found on [documentation](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/) on using forms and providing initial values.
* __Verdict__: Confirmed that the profile details show on checkout.html when profile exists already for user in session

### 11. OrderForm not rendered
* __Issue__: When displaying the checkout.html, throwing error: ```Exception Type KeyError at /checkout/ Exception Value full_name```
* __Error__: Exact error in terminal: ```order_form = OrderForm(initial={File "/workspace/corklagos-venture/checkout/forms.py", line 51, in __init__self.fields['full_name'].widget.attrs['autofocus'] = True```
* __Fix__: If I removed statement ```self.fields['full_name']....```, could see that no form was displayed at all. Found typo when declaring class OrderForm(forms.Form). Fixed with this: ```class OrderForm(forms.ModelForm)```
* __Verdict__: Checkout.html rendered without any errors

### 12. Payment throwing error
* __Issue__: Test payment keeps returning an error that "We were unable to take a payment with that card!"
My log is showing the following: ```"GET /static/js/stripe.js HTTP/1.1" 304 0 <ul class="errorlist"><li>stripe_id<ul class="errorlist"><li>This field is required.</li></ul></li></ul>```
* __Fix__: Found different suggestions and threads in [Slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1589651081388900). Moved {% block head_js %}{% endblock head_js %} at the bottom of base.html before body end tag and after all main scripts are loaded.
* __Verdict__: Threw two other errors
- Missing field id_expiry_year: typo id_expiry-year in stripe.js
- AuthenticationError at /checkout/, No API key provided: typo in checkout/views.py. stripe_api_key >> stripe.api_key

### 13. View created orders in admin site
* __Issue__: When checking orders made in admin site: error as ```Listing (foreignKey) does not have an attribute “name”```
* __Fix__: Went to checkout/models.py and changed self.listing.listing_name, self.listing.listing_price).
* __Verdict__: Can check orders on admin site.

### 14. Static not showing on development mode
* __Issue__: Static not showing on development mode after deploying to heroku
* __Resource__: Googled and searched Slack and found old [thread](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1589456279295700)
*__Fix__: 
- Added the following code in settings.py: 
```if 'DEVELOPMENT' in os.environ: STATIC_URL = '/static/', STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)```
- at the top of settings: ```if os.environ.get("DEVELOPMENT"): development = True >> else: development = False```
- In Gitpod env.py, added ```os.environ["DEVELOPMENT"] = "1"```
* __Verdict__: Deployed successfully to heroku, static files working on development and production and travis build passing

### 15. User not re-directed to edit profile
* __Issue__: Redirect to edit profile when registered and confirming email address
* __Fix__: Used following resources to redirect users just registered with their email address verified. [github](https://github.com/pennersr/django-allauth/issues/633) and [django-allauth](https://django-allauth.readthedocs.io/en/latest/configuration.html).
* __Verdict__: User redirected to add profile details after email address is verified.

### 16. User verification of email address
* __Issue__: Server Error (500) in production environment when sending email to user for confirming email address: SMTPSenderRefused
* __Fix__: Changed DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER'). Added EMAIL_HOST_PASS and EMAIL_HOST_USER as heroku env variables.
* __Verdict__: Email sent successfully in production environment.

### 17. Views import line too long
* __Issue__: From .views import Line too long
* __Fix__: Found solution [here](https://stackoverflow.com/questions/40003378/pep8-error-in-import-line-e501-line-too-long). Changed it to import(..., ...)
* __Verdict__: PEP8 error is gone.

### 18. Display past orders
* __Issue__: Tried Order.objects.get(user=request.user) to display past orders of user in session. Wrong queryset, user does not exist in the fields of Order. 
* __Fix__: Checked Order model and realised it is currently not associated with user. Added ForeignKey to associate user to more than one order. Used part of video course to set the ON_DELETE and add related_name to be able to query orders from user in views. When looking to display OrderLineItem, it also needed to add a related name to access the items of a specific item inside a loop.
* __Verdict__: Can access the order and the order items.

### 19. Error after collectstatic
* __Issue__: Made changes on css and pushed but not showing on heroku. Full error in terminal after running Python3 manage.py collectstatic, ```django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.```
* __Fix__: Found solution [here](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1573317900209900). Changed it to import(..., ...) and added the following code: ```STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') if 'DEV' in os.environ:STATIC_URL = '/static/' >> else: STATIC_URL = '/staticfiles/' >> STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)```
* __Verdict__: Latest changes of static files show in AWS and heroku deployed app.

### 20. Logout button with JS
* __Issue__: Logout button not working after writing the JS script. No errors in the console. As I console.log(response), I only got the response with status 200 but user does not show logged out. But when refreshing the page, the user is logged out and I get this error in the console ```logout.js:1 Uncaught TypeError: Cannot read property 'value' of null at logout.js:1```
* __Fix__: I finally understood that if status was 200, the POST request was successful and if user was logged out when refreshing the page, it meant I only need to reload the page in my function. [https://www.w3schools.com/jsref/met_loc_reload.asp](https://www.w3schools.com/jsref/met_loc_reload.asp). I triggered location.reload(); after an alert is displayed to the user.
- ```logout.js:1 Uncaught TypeError: Cannot read property 'value' of null at logout.js:1```, I added an if statement inside template tag on nav.html to only show js script if user is in session.
* __Verdict__: User clicks on logout button, alert shows "You've been logged out", page reload and user is logged out.

### 21. Invalid email address on contactform
* __Issue__: Contact form, email can be sent with an invalid email address.
* __Fix__: Searched and found that email html input type allows email addresses without a TLD (the “example.com” part of “email@example.com”). This is because RFC822, the standard for email addresses, allows for localhost emails which don’t need one. Found solution to add a pattern to the input [here](https://www.w3schools.com/TAGS/att_input_pattern.asp). Added it on footer.html
* __Verdict__: User gets error message is email address is not a full email address.

### 22. Placeholder and required not working on textarea
* __Issue__: Textarea attributes placeholder and required not working
* __Fix__: Found solution [here](https://stackoverflow.com/questions/10585759/why-isnt-my-textareas-placeholder-showing-up) explaining that the attributes dont work on textarea element if space between opening and closing elements. Fixed this in footer.html
* __Verdict__: Placeholder showing and contact form not sending if no message.

### 23. Edit profile form
* __Issue__: UnboundLocalError: local variable 'profile' referenced before assignment when user is redirected to edit profile after confirming their email address. 
* __Fix__: In dashboard/views.py, made two different contexts if profile exists or not so profile argument is not called when profile does not exist.
* __Verdict__: Error gone, editprofileform is displayed correctly to new user after registration.

### 24. AddListing form pre-filled after adding a listing
* __Issue__: Addlisting form showing new listing details just after adding it.
* __Fix__: Found solution [here](https://stackoverflow.com/questions/5773408/how-to-clear-form-fields-after-a-submit-in-django) and added `addform = AddListingForm()` after saving the new listing in dashboard/views.py.
* __Verdict__: Addlistingform shows empty after adding a new listing.

### 25. Login and register error messages
* __Issue__: Login or register error messages show in unreadable color
* __Fix__: Added django-allauth message 'invalid-feedback' class in style.css and set text color to inherit.
* __Verdict__: Error messages show clearly for user.

### 26. Buttons styling issues on Safari
* __Issue__: Buttons styling not showing on Safari browser.
* __Fix__: Found `type="button` was being used on the <a></a> elements so Safari browser handled the button styling and ignored the css custom classes. See [commit dd70ac5a27199fe4ef440352d2447740cb3a566c](https://github.com/mkuti/corklagos-venture/commit/dd70ac5a27199fe4ef440352d2447740cb3a566c).
* __Verdict__: Buttons show with custom style.

### 27. Page left banner stretched
* __Issue__: Page left banner shows stretched and is not fixed, almost shows as scrolling with screen.
* __Fix__: A slack alumna, [Malia Havlicek](https://github.com/maliahavlicek), helped me to move the image as a border-image style and put it inside the body tag. See [commit 870d8241a11bc76b7439503c442b91802f7e45b3](https://github.com/mkuti/corklagos-venture/commit/870d8241a11bc76b7439503c442b91802f7e45b3).
* __Verdict__: Left banner now shows fixed and no longer stretch.

### 28. No message for user when filter returns nothing
* __Issue__: When the user selects filters that return no results, no message to the user. Same for current listings and previous orders on addlisting.html and profile.html.
* __Fix__: On listing.html, added at the end of {% for loop %}, {% empty %} with a message to show users if no listings.
* __Verdict__: Message showing if no listings.

### 29. Listings images stretched
* __Issue__: The list images on large screens seem stretched out of proportion.
* __Fix__: Added object-fit: cover to .card-img class.
* __Verdict__: Image zoom and unzoom with screen size.

### 30. Negative price on adding a listing
* __Issue__: When adding a listing, can enter a negative price
* __Fix__: In listings/models.view, added imported MaxValueValidator from django.core.validators and updated Listing model with listing_price = DecimalField(validators=[MinValueValidator(20.00)])].
* __Verdict__: A listing cannot be entered below 20.00.

### 31. Car dealer adding a listing
* __Issue__: A car dealer in Nigeria can also add a listing or see the button to add a listing when this feature is only for Irish car dismantlers user type.
* __Fix__: For home page, added if user.is_authenticated: return redirect(reverse('listings')) so users already logged in cannot access the homepage. Changed the text for call action on home page to "login or register". On dashboard/views.py, added statement `if user_type == 'dealer': messages.error( request, 'You do not have the correct profile to add a listing')return redirect(reverse('dashboard'))` to redirect car dealer user if url is manually typed in. Added a main page for dashboard which is different for car dealer or dismantler. 
* __Verdict__: A user with 'dealer' user_type cannot access to add a listing.

### 32. Car dismantler buying a listing
* __Issue__: A car dismantler in Ireland can buy a listing when this feature is only for 'dealer' user type.
* __Fix__: On bag/views.py, added a try/except statement to throw an error message to card dismantler users if they access the view bag url, redirect them to listings.html, same if they click on add to bag. If profile does not exist, redirect user to add profile details before shopping. 
* __Verdict__: A user with 'dismantler' user_type cannot add a listing to bag or view shopping bag or access checkout.

### 33. Overflow/responsiveness
* __Issue__: Overflow on expertise page
* __Fix__: Added vertical margin on the who-card
* __Verdict__: No overflow anymore

## Other issues found but yet unsolved

### 1. 
* __Issue__: Full background image not being displayed on Google Chrome of Huawei 
* __Potential Fix__: Unsure as I did not have time to troubleshoot further.

I could not see any other issues or bugs during manually testing.
