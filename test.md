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
* __Issue__: Navbar and login button: A slack user gave feedback that takes a while to figure out that the icon below the Member Page was to log in.  or log out. Was advised to add a text.
* __Fix__: Added login or logout next to the icon   
* __Verdict__: Looks better and clearer in Navbar

### 2. 
* __Issue__: When going to login page, the console threw an error.
```Uncaught TypeError: Cannot set property 'onchange' of null```. The filter function attached to an eventhandler was looking for the searchbar which was no longer on the page
* __Fix__: Created separated js file for filter functionality and added an if statement on base.html to render only that js script when home page is active
* __Verdict__: No more console error

### 3. 
* __Issue__: On other pages than home page, the background image took too much space which means had to scroll down to go to login form or register form
* __Fix__: Added attribute of active='home' for the python home function. It means I could use this attribute inside an if statement with jinja template. 
```{% if active == 'home'%}``` which means a different template for a smaller version of image would be included on the base depending of the home page being active or not
* __Verdict__: Image is still nicely displayed but with a smaller height and no attention text

### 4. 
* __Issue__: Feedback from another Slack user about footer not being centered on smaller screens
* __Fix__: Added text-center class on div of footer
* __Verdict__: Footer is nicely centered on smaller screens too

### 5. 
* __Issue__: Feedback from Slack users, friend and mentor about one banner image I had created with different text bubbles and images. It was too overloaded with content and not really responsive
* __Fix__: On suggestion of mentor, found a nice and quiet background image to match thematic and put on top a transparent logo and spinner menu to make the first view of the website very minimalist but effective
* __Verdict__: Output of the home page and all pages is now very pleasant and most people have given very positive feedback on the UI of website

### 6. 
* __Issue__: Not really an issue but a need to quickly send item owner from the card itself. I was advised to use mailto as it is fast and I did not have enough time to implement any other complex feature
* __Fix__: Added user_email on insert function to MongoDB when an item is created or updated. Added jinja template inside the mailto href with the item.item_contact so website user can be redirected to their email tool to send an email.
```<a href="mailto:{{item.item_contact}}"```
* __Verdict__: It worked perfectly

### 7. 
* __Issue__: Edit button showing on the website user's items when he was logged in and on the home page. It meant that the edit button would not show on any other items and it made the cards height different which did not look good.
* __Fix__: Added ```{% if active == 'account'%}``` for the edit button to show on cards which template is included on both home and account page. 
* __Verdict__: It avoided me hard coding twice the cards template. The cards now are nicely rendered

### 8. 
* __Issue__: Item description of cards would not collapse when filtered items were displayed from the searchbar
* __Fix__: Nested collapsible event into a function so I can call it back inside the filtered functionality
* __Verdict__: All cards are now collapsing correclty, on home page, account page and when filtered items displayed

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
