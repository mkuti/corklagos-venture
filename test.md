<h1 align="center">
  <a href="https://corklagos-venture.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/X2x8rHN/Screenshot-2020-06-29-at-2-58-53-PM.png" alt="Multi Device Mockup"/></a>
</h1>

<div align="center">
<a href="https://corklagos-venture.herokuapp.com/" target="_blank"><img src="static/images/logo.png" width='200' height='150' alt="logo"></a>
</div>

<div align="center">
    <h2>Testing document</h2>
</div>

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

### 1. 
* __Issue__: Probably less an issue than a failed attempt to customise the signup form and the user model so the user has a profile created when signing up with more details than the regular Django-allauth signup form. I searched and started to implement a custom model with adapter, a custom signup form which was working but could not save the details of the profile when user created. After spending much time on it and seeking help from Slack and Tutor Support, decided to go with the easier method of redirecting the user to create a profile after they have already signed up.
* __Fix__: Created a new app called dashboard where the user is redirected to add his business details after confirming his email address (redirect is configurated in settings.py with ```ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/dashboard/')```).
* __Verdict__: Although it takes three steps rather than one, the user can get a profile created which is associated with the user model by a OneToOneField. 
* __Future fix__: After project's evaluation, will come back to this and try to have a customised user model with a custom signup form.

### 2. 
* __Issue__: Non-nullable field and default value for ForeignKey ```You are trying to add a non-nullable field new_field to ... without a default. We can't do that (the database needs something to populate existing rows).```. 
* __Fix__: Found beginning of explanation [here](https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a) and with the help of [Chris Z.](https://github.com/ckz8780) on Slack, I found out that it was easier to add ```null=True``` when migrating to avoid this error. Because I had set a wrong default in "makemigrations", I had to cancel the previous migrations so ```python3 manage.py migrate``` would work.
* __Verdict__: Managed to migrate the models with ForeignKey without any further issue.

### 3. 
* __Issue__: Implementing the filter on listings page. I was stuck for a few hours, trying to understand how to use a queryset to filter the listings with category and car make. I could get the categories and makes to render and did try to set up a filter in my views but did not filter any results when testing it.
* __Fix__: After searching more, found the django-filter package and a great article explaining its features, followed the documentation and created a filters.py in my listings app to implement filter and have a for loop with queryset (qs) argument on the html template to show listings depending of the filter queried.
*__Resources__: 
- [Django-Filter documentation](https://django-filter.readthedocs.io/en/stable/index.html)
- [Simple is better than complex](https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html)
* __Verdict__: Filters listings by category or car make. I would like to make it even better by removing the button.

### 4. 
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

### 5. 
* __Issue__: Add to bag template tag causing error: ```Argument ‘’ is not accepted```.
* __Fix__: Changed listing_id to listing.id as listing_id does not exist as I could see in print().
* __Verdict__: Listing gets added to the bag without error.

### 6. 
* __Issue__: Login url for redirect causing error.
* __Fix__: Go to [allauth doc](https://django-allauth.readthedocs.io/en/latest/views.html?highlight=login%20url#login-account-login) and found the correct name: ```account_login```.
* __Verdict__: Redirect works.

### 7. 
* __Issue__: On bag/contexts.py, error: "unsupported operand type(s) for +=: 'int' and 'str'" when adding to bag.
* __Fix__: Found [here](https://stackoverflow.com/questions/2376464/typeerror-unsupported-operand-types-for-str-and-int) a beginning of solution. Confirmed that listing_quantity was int. Remembered that listing_price was not using decimal field
Changed to decimal field and worked.
* __Verdict__: Adding to bag is successful.

### 8. 
* __Issue__: Item list not showing on bag.html inside the loop.
* __Fix__: Investigate result of bag_items only by printing in terminal inside views.py. Checked again the contexts.py and see how listing object could be accessed. After iterating bag_items and setting variable of item, need to call the actual object before calling its attributes: ```{{ item.listing.listing_price}}```.
* __Verdict__: Could see the listings in the bag template.

### 9. 
* __Issue__: Item description of cards would not collapse when filtered items were displayed from the searchbar
* __Fix__: Nested collapsible event into a function so I can call it back inside the filtered functionality
* __Verdict__: All cards are now collapsing correclty, on home page, account page and when filtered items displayed

### 10. 
* __Issue__: Register Screen: can't read the password place holder
* __Fix__: Made it shorter "between 5 and 10 characters"
* __Verdict__: Easier to read now

### 11. 
* __Issue__: About section only showing on home page and the footer showing off color.
* __Fix__: Realised that the about section had to go on all pages so moved it from home.html to base.html above footer
* __Verdict__: Looks better

There were other issues which were found and fixed but did not have time to document them unfortunately.

## Other issues found but yet unsolved

### 1. 
* __Issue__: If image url is not correct when adding an item, no error message for user and card is being created without image
* __Potential Fix__: to throw an error to the user if image url is not correct or to replace image space by default image when invalid url

### 2. 
* __Issue__: 4. If successfully logged in, the app takes you to the home page, the navbar-toggler button goes into the left margin too far. This could be caused by the flash message with a too big font but also because user had entered her email address as username which created a too long message
* __Half Fix__: replaced h1 with h3 inside the jinja template of flash message.But did not test it again with Slack user.
* __Potential Fix__: To create a proper modal for flash message and to stop user to use their email address as username

### 3. 
* __Issue__: Filter button is smaller than its text
* __Potential Fix__: Make the Add Item and filter two separate lines for small devices

### 4. 
* __Issue__: A slack user reported an issue on Chrome with Mac. On the main page when clicking contact, nothing happens. It works on my phone. [Stack overflow](https://stackoverflow.com/questions/45197326/mailto-links-do-not-work-on-my-mac) states that it's an issue with mac configuration of mail. 
* __Potential Fix__: Leave a warning for users to follow process below on their Mac:
> Open Mac Mail and Preferences Dialog. Ensure you have Default email reader set to Mail.app (or whatever app you use for mail).
