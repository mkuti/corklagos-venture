[![Build Status](https://travis-ci.org/mkuti/corklagos-venture.svg?branch=master)](https://travis-ci.org/mkuti/corklagos-venture)

<h1 align="center">
  <a href="https://corklagos-venture.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/X2x8rHN/Screenshot-2020-06-29-at-2-58-53-PM.png" alt="Multi Device Mockup"/></a>
</h1>

<div align="center">
<a href="https://corklagos-venture.herokuapp.com/" target="_blank"><img src="static/images/logo.png" width='50%' height='auto' alt="logo"></a>
</div>

The website of CorkLagos Venture was designed, developed and deployed by MPia Kuti as her final project for the Code Institute Full Stack Web Development diploma.

I have used the opportunity of the Code Institute Milestone 4 project to build an ecommerce website which would be used by an Nigerian import/export business known through connections. Many Nigerians living in Ireland engage themselves in an import/export trade between Ireland and their home country. But often without any specific organisation, built network or online presence. They always have to rely on ephemere places where they hope to sell their goods once shipped to Nigeria. 

With an online presence, they could develop their reliable customer network in Nigeria while also targeting the car dismantlers here in Ireland so goods trade could almost be agreed from distance, saving time and precious funds.

The website is built for this venture, formed of 3 different trade men in the business for many years. The website is targeting two sorts of clients, one upstream advertising and selling goods, one downstream scrolling and buying goods before they get shipped. So we have a masculine audience with an interest in cars and a goal to make money.

### Note to Assessors:

First, to enable assessment of the backend/admin side of the app (if needed), a 'staff' account with read-only privileges has been created:

- username: __viewadmin__
- password: __testadmin789__

Since the website targets two types of users with different access, please note you might need to change the user_type when editing the profile details so you can test all features.

Both users can edit their profile details and view the available listings.
- A 'dealer' user type can then buy any listings and then views his past orders in his dashboard. A 'dealer' user type cannot add any, edit or delete listings and will be redirected if url is typed manually.
- A 'dismantler' user type can then add a new listing, and view, edit or delete his own listings. A 'dismantler' user type cannot buy a listing and will be redirected to view listings if button is clicked or url is typed manually.

## Table of Contents

- [UX](#ux)
  * [Strategy plane](#strategy-plane)
    + [What are the goals and needs of the site owner?](#what-are-the-goals-and-needs-of-the-site-owner-)
    + [User stories](#user-stories)
      - [Venture owner](#venture-owner)
      - [Irish Car Dismantler (upstream client)](#irish-car-dismantler--upstream-client-)
      - [Nigerian Car Dealer (downstream client)](#nigerian-car-dealer--downstream-client-)
  * [Scope plane: How?](#scope-plane--how-)
    + [Existing Features:](#existing-features-)
    + [Features which appear on every page:](#features-which-appear-on-every-page-)
    + [Features on Home page:](#features-on-home-page-)
    + [Features on expertise page:](#features-on-expertise-page-)
    + [Features on Spare parts page:](#features-on-spare-parts-page-)
    + [Features on Login and Register pages:](#features-on-login-and-register-pages-)
    + [Features on Dashboard pages](#features-on-dashboard-pages)
    + [Features on Bag page](#features-on-bag-page)
    + [Features on Checkout page](#features-on-checkout-page)
    + [2. Features Left to Implement:](#2-features-left-to-implement-)
  * [Database Architecture](#database-architecture)
    + [Choice of Database](#choice-of-database)
    + [Data model](#data-model)
      - [Users](#users)
      - [Profile](#profile)
      - [Listing](#listing)
      - [Category](#category)
      - [Make](#make)
      - [Order](#order)
      - [OrderLineItem](#orderlineitem)
  * [Skeleton plane: Presentation and navigation?](#skeleton-plane--presentation-and-navigation-)
    + [1. Wireframes](#1-wireframes)
  * [Surface plane: Design](#surface-plane--design)
        * [Colours:](#colours-)
        * [Logo:](#logo-)
        * [Fonts:](#fonts-)
        * [Icons:](#icons-)
        * [Images:](#images-)
- [Technologies Used:](#technologies-used-)
    + [IDE:](#ide-)
    + [Languages:](#languages-)
    + [Frameworks & Libraries:](#frameworks---libraries-)
    + [Databases](#databases)
    + [Tools](#tools)
- [Testing](#testing)
- [Deployment](#deployment)
  * [How to run this project locally](#how-to-run-this-project-locally)
    + [Instructions](#instructions)
  * [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
- [Special thanks](#special-thanks)
        * [Disclaimer:](#disclaimer-)

# UX
## Strategy plane

### What are the goals and needs of the site owner?

The website needs to be very streamline, traditional and classic. After speaking with some clients on both sides, either the site owners or the clients are not very big internet users so are not interested in innovation or images, they're busy and want to go straight to their own particular tasks. 

### User stories

#### Venture owner 
1. As a user, I want to have a new online presence.
2. As a user, I am looking to expand the network and relationship with car dismantlers in Ireland so I can access more spare parts and have a priority on buying.
3. As a user, I want the online presence to help finding direct buyers in Nigeria to avoid shipping without sale.
4. As as user, I want to increase the number of dealers in Nigeria who trust my products and services.
5. As a user, I want to keep track of orders and guarantee a safe record and payment to my clients.
6. As a user, I want to keep track of my clients, upstream and downstream, so I can directly contact them for new arrivals or needs.
7. As a user, I want the website to explain our policies and processes to the clients to ensure trust.

#### Irish Car Dismantler (upstream client)
1. As a user, I am expecting a website where I can upload any new product I have to sell.
2. As a user, I often have difficulty to sell, so I hope to increase my sales and to reduce the delay of selling.
3. As a user, I dont like website with too much reading and unclear navigation, I want to go straight to the point and know which section is built for me.
4. As a user, I would like to know the process and policies of this business so I can trust them in doing business.
5. As a user, I would like a guarantee that any details I am providing will not be shared but kept on record only for business purposes.

#### Nigerian Car Dealer (downstream client)
1. As a user, I am expecting a website where I can check all the latest available products in one click.
2. As a user, I want to be taken intuitively to the section built for my purpose.
3. As a user, I dont like using too much the navbar so I want clear buttons on each page to take me to the next one.
4. As a user, I would like to know the process and policies of this business so I can trust them in doing business.
5. As a user, I would like a guarantee that the payment made is safe and is confirmed by an email.
5. As a user, I would like a guarantee that any details I am providing will not be shared but kept on record only for business purposes.
6. As a user, I would love to track my order once I've confirmed the purchase.
7. As a user, I want a clear section which guides me to contact the business for any information.

[Back to Top](#table-of-contents) 

## Scope plane: How?

### Existing Features:
### Features which appear on every page:

__Feature 1: Navbar__
- The navbar provides the user a quick way to navigate around the website. 
- With the logo in the middle which redirects to home page if user is not logged in and to listings if user is logged in.
- At first, when user is not authenticated, the navbar show login and register nav-items. Once logged in, the user will be presented a dashboard and logout nav-items.
- Logout button logs out the user by simply clicking on the button with a POST request sent to Django using Javascript.
- The shopping bag appears with same color as the other nav-items when empty.
- The same shopping bag changes color if listings added and also shows the current total of the bag, with the sumn incrementing when user adds more items.
- Each nav-item brings the user to other pages.
- Home nav-item disappear once user is logged in.

__Feature 2: Footer__
- For adding an easier navigation and to match the current trend of most commercial websites, we've added the same links as the navbar.
- A contact form can be filled by user with his contact details, a subject and a message and will be sent to the business owner via emailjs.
- A bottom banner explains to user that the website is designed for educational purpose.

__Feature 3: African print left banner__
- Since the business owners' country of origin and the purpose of the website is to trade with an African country and maybe more, we have added an African print as a left border which shows on every page and every screens. Its colors match perfectly the rest of the website and logo.

__Feature 4: Feedback messages__


### Features on Home page:
__Feature 5: Background image__
- A rich and detailed image of an engine.

__Feature 6: Calls for action__
- Calling the different types of user
- If dismantler, you might want to sell, so login or register.
- If car dealer, you're wondering what parts are available so go to check the latest.
- The call boxes have the rich wheel color with some opacity so we can still see the rich background image underneath.

### Features on expertise page:
__Feature 7: Photo and pitch__
- Photo shows modern business team, professional but smiling, ready to support their clients.
- Pitch or slogan confirms the commitment, purpose and availability, reminding the users that the business is about an international trade. It also reassure the users of their engagement towards both sides of the business which is unique in the trade. 

__Feature 8: Flipping cards__
-  Unique way to introduce the abilities of a business by revealing those behind iconic animals from the African continent. 
- The idea is to attract the eyes and catch the attention of the user by only showing the content behind photos.
- A leopard with fierce and determined eyes which can reassure the users of the expertise and impressive goals of expansion displayed by the business.
- An eagle, showing the flexibility and connection of the business going beyond lands.
- Giraffes inviting the users to participate in this goal of expansion and network.

### Features on Spare parts page:
__Feature 9: Filters__
- The user can quickly see that the business is trying to specialise in certain categories and makes.
- **By category*: With 5 categories to choose, the user can filter different parts and go back to all available parts.
- **By make*: The user can choose between 3 different makes to filter through the parts.
- If no listings available in a certain category or make, a message comes up.

__Feature 10: Listings__
- In a bootstrap horizontal card using the unique website colors, the listing is displayed with its image, category, name, description and price. 
- All active listings are displayed. When a product gets purchased, the products becomes inactive which means it cannot be purchased anymore.
- The user does not have to go to another page, he can add to bag with a button.
- If dismantler user clicks on the button, he has a warning message to advise he does not have the correct profile and is redirected to listings.

### Features on Login and Register pages:
we have used Django-Allauth package to implement authentication features and we've then customised our own templates.

__Feature 4: Background image__
- A rich and detailed image of an engine. Same as home page.

__Feature 11: Login Box__
- The same call box and colors as home page are used.
- A button to reset password if forgotten.

__Feature 12: Call to register__
- If user never registered before, invited to register
- Suggest to user that by registering, he can enjoy great services.
- Small reminder about the types of car makes we sell and that our business is to export to Nigeria so we depend of downstream demand too.

__Feature 13: Register Box__
- A button to sign in if user has already registered.
- Form to enter username, email address and twice password.
- Form is designed by Django-Allauth package and we decided in the configuration settings to ask the password twice.

__Feature 14: What types of users__
- Explain the types of users and their special accesses.

### Features on Dashboard pages
__Feature 4: Background image__
- A rich and detailed image of an engine. Same as home page.

__Feature 15: Welcome banner__
- The same call box and colors as home page are used but taking the whole width of the screen.
- Welcoming the user with his business name.
- Showing the profile details: address, email address, phone number, using font awesome icons to give more attention to the section.

__Feature 16: Calls for action__
- Since we display the user's details, we then give them a button to go and edit the details if they want.
- If user is dismantler, 2nd button is to add a new listing.
- If user is dealer, 2nd button is to review past orders.

__Feature 17: Edit Profile__
- A form displayed in two different columns on larger screens, one column on smaller screens.
- Form comes from the EditProfileForm and if user has already a profile, his details will be already pre-filled.
- If user changes one or no details, the form will save what is already pre-filled.
- Button to add a new listing if user is dismantler
- Button to Review past orders if user is car dealer

__Feature 18: View and add a new listing__
- Only accessible for user with dismantler type.
- View current listings of the user displayed as cards, with only the image and the name.
- Button on the listing to edit or remove the listing.
- If no current listings, banner announcing no current listings.
- Form to add listing displayed in two different columns on larger screens, one column on smaller screens.
- Drop down menu for categories and makes.
- An option to upload a product image which will be saved to the media folder in AWS as set up in settings.py.
- As soon as the listing is added, it shows on the same page above and the page reload with blank form for a new listing.

__Feature 19: Edit a listing__
- Only accessible for user with dismantler type.
- Same form as add a listing is displayed in one column next to the listing details
- All listing details are also pre-filled as an instance on the form.
- If user changes one or no details, the form will save what is already pre-filled.
- Once listing is edited, the user is redirect to view current listings.

__Feature 20: Review past orders__
- Only accessible for user with dealer type.
- Looping through the user's past orders.
- Past orders are displayed as a table.
- Within each order, to loop through any items and display a single item on its own row.
- Displaying the date, the order number, the listing name, make and price as well as the total of the order.

### Features on Bag page
Bag items have been made available on all pages via a context.py file created inside bag app. We can call the bag_items and any of its arguments like total on any views or templates without importing the model.
Bag in session which empties itself when user logs out.

__Feature 21: View bag items__
- Looping through the bag, displaying each item on its own row, with same details as on the listings page
- On the card, button to remove listing from shopping bag.

__Feature 22: Remove from bag__
- When user clicks on remove listing from the shopping bag, the listing pops out of the bag and the user gets redirected to the bag with the item not showing anymore.

__Feature 23: Total__
- Total made of the addition of number of listings and their respective price.

__Feature 24: Checkout button__
- Takes the user to the checkout form

### Features on Checkout page
__Feature 23: Total__
- Total made of the addition of number of listings in the bag and their respective price.

__Feature 25: Edit bag button__
- Takes the user back to view the shopping bag.

__Feature 26: Two forms in one__
- OrderForm which creates an order associated with the user for viewing later, which contains the details of the profile, which user can edit if needed.
- PaymentForm which contains a stripe id for stripe to process the payment with the credit card provided in the form.

__Feature 27: Submit payment button__
- By submitting payment, saves the order and its items associated, and stripe process the payment.
- Django sends email to the user to confirm the payment.
- Listing purchased becomes inactive in the backend so is not displayed anymore on listings page.

### 2. Features Left to Implement:
* In the future, to be even more secure, we will remove the user_type field from the profile_form if profile exists already, so users cannot change their profile access themselves.
* To have the user sign up with a full profile in one step. I tried to customise the user model with an adapter and create a customised signup form but could not save the profile and because of time, I chose to make the user create a full profile after registering and confirming their email address. But it would be faster to get them to sign up on the first step. 
* Add a system for the car dealers where they show their interest for a car part before even buying it. This way, the CorKLagos Venture owners can base their movement on the downstream demand and could then make contact with the sellers to confirm the part and add more details for the dealer.
* Privacy Policy and more details about the business to add more trust for the users and clients.
* Add pagination to the listings. Could not make it work with the time I add.
* Add a currency converter for the Nigerian Car dealers to convert Euro to Naira
* Add shipping costs and timelines when venture owners are more settled and have better visibility of shipping. Right now, it depends of so many factors they cannot control due to the ephemere networks. This website will hopefully help making a more regular and reliable shipping logistic.
* Add more categories and makes when business starts booming.


[Back to Top](#table-of-contents) 

## Database Architecture
### Choice of Database
- As a framework Django works with SQL databases. During development on GitPod, since Django is a Python Web framework, and Python includes a lightweight database called SQLite, this is what I used.
- For the production, I installed the Heroku Postgres addon which is a managed SQL database service provided directly by Heroku.

### Data model

#### Users
I have chosen to use the [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) package to handle all authentication and registration.

#### Profile
From the user model, I have then created a profile model, associated with the user by a OneToOneField.
The profile model exists within the dashboard app but is being imported and used throughout the project.
The 2nd field for address is optional, the county is optional because not for Nigeria, country is optional for Irish dismantlers.
A profile gets deleted when its related model, user, is deleted with the following validation: on_delete=models.CASCADE.

| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|
| user       |  on_delete=models.CASCADE | OneToOneField to User        |
| user_type     |  max_length=15, choices=user_type, default=''   | CharField             |
| business_name    |  max_length=50, blank=False   | CharField             |
| phone |  max_length=20, blank=False   | CharField |
| street_address |  max_length=50, blank=False   | CharField |
| street_address2 |  max_length=50, blank=True   | CharField |
| postcode |  max_length=20, blank=True   | CharField |
| city |  max_length=30, blank=False   | CharField |
| county |  max_length=30, blank=True   | CharField |
| country |  max_length=30, blank=True   | CharField |

#### Listing
The Listing model was created within the listings app to contain all details for a listing which will then be used for adding and edit a listing, displaying all available listings with a filter to its related model, category and make.
If category or make are deleted, the listing does not get deleted and the related fields can stay blank.
Listing is also related to User model for its owner. If user gets deleted, all related listings also get deleted.
The choice of user_type is defined within the same model.

The Listing model uses Pillow to store all image files in an AWS S3 bucket via a media folder configured in settings.

| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|
| listing_owner       |  on_delete=models.CASCADE, null=True | ForeignKey to User         |
| listing_category     |  on_delete=models.SET_NULL, null=True   | ForeignKey to Category             |
| listing_make     |  on_delete=models.SET_NULL, null=True   | ForeignKey to Make             |
| is_active    |  null=False, blank=False, default=True   | BooleanField             |
| listing_name |  max_length=50,    | CharField |
| listing_description |     | TextField |
| listing_price |  max_digits=6, decimal_places=2, validators=[MinValueValidator(20.00)]   | DecimalField |
| listing_image |  upload_to='images'   | ImageField |

#### Category
The choice of categories is defined within the same model. A class of filter "ListingFilter" is then defined in a [filters.py](https://github.com/mkuti/corklagos-venture/blob/master/listings/filters.py) file created in the listings app. This applies to Category and Make models.

| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|
| name       |  max_length=15, choices=makes, null=False | CharField         |

#### Make
The choice of makes is defined within the same model.

| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|
| name       |  max_length=15, choices=categories, null=False | CharField         |

#### Order
The Order and OrderItem models are the checkout app, and are strictly related. The OrderLineItem cannot be created without an order as it hold the items of each order created and can be called with a related name. Those models are needed for users to create and pay for their orders.
The order is related to the User model and if user gets deleted, the order will stay in the database for record purpose.

| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|
| user       |  on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to User         |
| full_name    |  max_length=50, blank=False   | CharField             |
| street_address |  max_length=40, blank=False   | CharField |
| street_address2 |  max_length=40, blank=True   | CharField |
| postcode |  max_length=20, blank=True   | CharField |
| city |  max_length=40, blank=False   | CharField |
| country |  max_length=40, blank=False   | CharField |
| date |  | DateField |
| total |  blank=False, null=True   | IntegerField |
| order_number |  default=uuid.uuid4, editable=False   | UUIDField |

#### OrderLineItem
A row of OrderLineItem is created for each item existing in the shopping bag which then gets saved with the order. 

| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|
| order       |  on_delete=models.CASCADE, null=False, related_name='orderitems') | ForeignKey to Order         |
| listing    |  on_delete=models.CASCADE, null=False   | ForeignKey to Listing            |
| quantity |  blank=False   | IntegerField |



[Back to Top](#table-of-contents) 
	
## Skeleton plane: Presentation and navigation? 
### 1. Wireframes

I used Balsamiq tool for the wireframes and attached them to the workspace within their own directory at the root level. While I did not spend too much time on the design at that stage,.
For the tablet format, I chose to use the horizontal size (1024x780) as this is how most users would use their tablet size to see websites. 

Please find a few wireframes showing the main page, the Our Team, the signup and payment. All the other wireframes can be found [here](https://github.com/mkuti/corklagos-venture/tree/master/wireframes)

<div align="center">
    <img src="wireframes/home-desktop.png" alt="Wireframe of Home page on desktop" aria-label="Wireframe of Home page on desktop" />
</div>

<div align="center">
    <img src="wireframes/home-mobile.png" alt="Wireframe of Home page on mobile" aria-label="Wireframe of Home page on mobile" />
</div>

<div align="center">
    <img src="wireframes/signup-desktop.png" alt="Wireframe of Signup page on desktop" aria-label="Wireframe of Signup page on desktop" />
</div>

<div align="center">
    <img src="wireframes/signup-mobile.png" alt="Wireframe of Signup page on mobile" aria-label="Wireframe of Signup page on mobile" />
</div>

<div align="center">
    <img src="wireframes/payment-desktop.png" alt="Wireframe of Payment page on desktop" aria-label="Wireframe of Payment page on desktop" />
</div>

<div align="center">
    <img src="wireframes/payment-mobile.png" alt="Wireframe of Payment page on mobile" aria-label="Wireframe of Payment page on mobile" />
</div>

[Back to Top](#table-of-contents) 

## Surface plane: Design 

Since design and UX are not my biggest qualities, I often spend time deciding on the right elements which will ensure the website being a success for the site owners and the users.
I inspired myself from general ecommerce websites and did not want to innovate too much here because we want to attract traditional website users who do not have huge time to spend searching for the exact information. 
I looked around at different templates and liked the animations suggested on [BootStrapMade Company template](https://bootstrapmade.com/demo/Company/), which I will apply to the display of car parts listing.

##### Colours:
With a primary audience of men and the website main goal in attracting more users, the keywords which helped me to find the colors were reliability, power, excitement, engagement. The colors chosen will complement each other in achieving this, as well as making the website somehow reflecting the origins of the site owners and reviving their pride.

<div align="center">
    <img src="wireframes/color-palette.png" alt="CorkLagos Venture Brand Colours" aria-label="CorkLagos Venture Brand colours" />
</div>

- Eerie Black: #201E1F;
- Red-Orange (Color Wheel): #FF4000;
- Antique White: #FEEFDD;
- Oxford Blue: #03254E;
- Tumbleweed: #D7AF8E;

* Primary:  <strong>Oxford Blue</strong> I chose this as the primary colour as blue's psychological perception is associated with competence, reliability and high quality which is the main message we want to communicate here for our clients and users. The website need to trigger a feeling that the business owners are reliable partners whom they can trust to sell or buy. The color works also perfectly in association with the secondary color, reminding the users the African colors.
* Secondary:  <strong>Red-Orange (Color Wheel)</strong>I chose this as the secondary colour as red and orange conveys a sense of speed and excitement which can be associated with anything related to car. Also its bright color associated with blue is reminding that the trade is done with Nigeria where the site owners are from. The two colors remind the sun, the spectacular landscapes, the beautiful colors used in native clothes proudly wore by the Nigerians.
* Tertiary:  <strong>Tumbleweed</strong> This tertiary colour will compliment the main orange color and will be used for small parts, such as icons or the text color of box or buttons highlighted by the primary color. This color is also a reminder of the sand hugely present in Africa.

To add an extra tribal reminder for Africa, took a screenshot of a colorful print and placed it as a vertical banner on the left only for big screen sizes.
[African print](https://images.fabric.com/images/605/605/0692828.jpg)

##### Logo:
I used [Hatchful Shopify](https://hatchful.shopify.com/) to find the most suitable logo. With the keywords of the website in my head, I first selected the bold, reliable and energetic visual styles for the logo. I instantly picked one suggestion of logo with the earth and enveloppe going around. See [the original logo](https://raw.githubusercontent.com/mkuti/corklagos-venture/master/static/images/originallogo.png). It looked smart and bold. I changed slightly the style to have the business name outside the icon which gave a more professional look. I also straight away chose to have the contrast between blue and orange, which made me think of the bold colors of Africa. [JimLynx](https://github.com/JimLynx) in Slack re-worked on the logo for me to make it cleaner and brighter.

##### Fonts: 
Importing the fonts directly in my css file with the Import Url option.

__[Lato](http://www.latofonts.com/)__:
Simple, professional and elegant without having any spectacular innovative trait matches perfectly the corporate goal of the website. The semi-rounded details of the letters give Lato a feeling of warmth, while the strong structure provides stability and seriousness. The main idea of Lato is classical which will reassure our users when visiting the website.
It is used as main font for the body.

__[Crimson Text](https://fonts.google.com/specimen/Crimson+Text?preview.text=We%27ll+ship+any+car+parts+you+want!&preview.text_type=custom&sort=popularity&preview.size=24&query=crimson+text)__:
While Lato is representing the corporate and reliable character of the website, Crimson Text is giving that flash of innovation for small parts of the website without overwhelming the user with a different or unknown style. 
It is used for the slogan and any direct messages to the user.

##### Icons:
Without flooding too much the website with icons everywhere, I am only mainly using the icons for the categories and brands associated with the product listings so the user can quickly identify the category even if the word itself does not give a meaning.

##### Images:

Again, I wanted to have the website as simple and effective as possible so used only a few images.
I will have a full background image on the home page, slightly faded below the main elements of the page, showing a car dismantled.
For the expertise page presenting the business, I downloaded an image of a business woman and man looking very professional and friendly. And I also downloaded the photos of animals from Pexels, referred with their author below.
- [Photo of the car motor](https://www.pexels.com/photo/close-up-photo-of-black-and-silver-car-engine-3757226/) by [Hebert Santos](https://www.pexels.com/@hebert-santos-1346254) from Pexels
- [Photo of business man and woman](https://www.pexels.com/photo/man-and-woman-smiling-inside-building-1367269/) by [Rebrand Cities](https://www.pexels.com/@rebrand-cities-581004) from Pexels
- [Photo of leopard ](https://www.pexels.com/photo/animal-eyes-big-dangerous-87403/) by [Public Domain Pictures](https://www.pexels.com/@public-domain-pictures) from Pexels
- [Photo of eagle](https://www.pexels.com/photo/flight-bird-beak-eagle-3959918/) by [Frank Cone](https://www.pexels.com/@frank-cone-140140) from Pexels
- [Photo of giraffe](https://www.pexels.com/photo/pattern-formation-wild-animals-south-africa-34098/) by [Pixabay](https://www.pexels.com/@pixabay) from Pexels

All test listings image and details were inspired from [CarPartsNigeria](https://www.carpartsnigeria.com).

# Technologies Used: 

### IDE:
- [GitPod](gitpod.io) - I used __GitPod__ as my IDE for the development of this website.

### Languages:
This project used __HTML__, __CSS__, __Javascript__ and __Python__ as programming languages.

### Frameworks & Libraries:
- [Django](https://www.djangoproject.com/) as a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) to address authentication, registration, account management.
- [django-filter](https://django-filter.readthedocs.io/en/latest/index.html) to filter down a queryset based on a model’s fields, displaying the form to let them do this.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) to control the rendering behavior of your Django forms in a very elegant and DRY way.
- [django-storages](https://django-storages.readthedocs.io/en/latest/) to collect custom storage backends for Django.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to create, configure, and manage AWS services.
- [DJ-Database-URL](https://github.com/jacobian/dj-database-url) to utilize the DATABASE_URL environment variable to configure Django application.
- [Pillow](https://pillow.readthedocs.io/en/stable/index.html) to add image processing capabilities to Python interpreter.
- [Heroku](https://dashboard.heroku.com/apps) to build, deploy, and manage your apps
- [gunicorn](https://docs.gunicorn.org/en/stable/#) to connect Django to Heroku.
- [psycopg2](https://pypi.org/project/psycopg2/) as a PostgreSQL database adapter.
- [Stripe](https://stripe.com/ie) to handle the payments.
- [Travis CI](https://travis-ci.org/) for continuous integration.
- [AWS S3 Buckets](https://s3.console.aws.amazon.com/s3) for storing the static files and data uploaded by the website users.
- [AWS IAM](https://console.aws.amazon.com/iam) for S3 buckets Identity and Access Management.
- [PIP](https://pypi.org/project/pip/) for installing all Python libraries and packages needed in this project.
- [Git](https://git-scm.com/) to track changes in source code during software development and for version control.
- [GitHub](https://github.com/) to store and share all project code remotely.
- [Bootstrap](https://getbootstrap.com/) as a front-end open source toolkit, to handle the responsive grid system.
- [jQuery](https://jquery.com/) to handle DOM traversal and manipulation, event handling, animation, and Ajax.
- [Popper.js](https://popper.js.org/) used by Bootstrap for tooltip and popover positioning engine. 
- [EmailJS](https://www.emailjs.com/) to send user's emails directly from JavaScript from the contact form.
- [FontAwesome](https://fontawesome.com/) as an icon library.
- [Google Fonts](https://fonts.google.com/) for the website fonts.

### Databases

- [PostgreSQL](https://devcenter.heroku.com/categories/heroku-postgres) for production database, as addon of heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, included with django.

### Tools
- [AutoPrefixer](https://autoprefixer.github.io/) to make sure the css code worked on all browsers.
- [Tiny.jpg](https://tinyjpg.com) to compress logo image of the website to increase the website loading on browser
- [Coolors](https://coolors.co/) to find matching colors for the website
- [Balsamiq](https://balsamiq.cloud) to build the wireframes which I then exported to the IDE
- [Favicon converter](https://favicon.io/favicon-converter/) to convert the logo into a favicon which I was able to insert in the static folder and I tested it to be working
- [Sweetalert2](https://sweetalert2.github.io/)
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) to show content structure, margin and paddings and fix any offset
- [Techsini Multi-Mockup](https://techsini.com/multi-mockup/index.php) to create multi-device photo of README

[Back to Top](#table-of-contents) 

# Testing

I created a separate document for Testing writeup which can be found [here](https://github.com/mkuti/corklagos-venture/blob/master/TESTING.md)

[Back to Top](#table-of-contents) 

# Deployment
I have been using the Integrated development environment (IDE) [GitPod](gitpod.io) to develop this milestone project.
As I used it for the first time and Code Institute changed the preferred IDE for the whole course, I was lucky to avail of the full template prepared by Code Institute at the time.

I went to Code Institute [full template repository](https://github.com/Code-Institute-Org/gitpod-full-template), cloned it and created my own repository with the template ready. From there, I opened GitPod which started a workspace.

From that point, I could add, commit any update of my code and push it to the remote repository so it could be regularly backed up and accessed by others.

__GitHub__: All versions and branches of the code are stored in github.

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [GitPod](https://gitpod.io/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- If you use Code Institute template, all the above will be already installed

Ensue to create free accounts with the following online services in order to run this project.
- [Stripe](https://stripe.com/ie)
- [EmailJS](https://www.emailjs.com/)
- Change security settings of an email account so Django can send emails via your email address.
- [Travis CI](https://travis-ci.org/) can be connected with GitHub credentials.
- [AWS S3](https://s3.console.aws.amazon.com/s3)

### Instructions
1. Clone the git repository by downloading it [here](https://github.com/mkuti/corklagos-venture) or typing the following command in your terminal:
`git clone https://github.com/mkuti/corklagos-venture`
2. Once you're in the new project, set virtual environments (You do not have to do this in GitPod) with the following command in your terminal:
`python3 -m .venv venv`
3. Initialize the environment by using the following command:
`.venv\bin\activate`
4. Install all required modules with the command 
```pip3 install -r requirements.txt```
5. In your local IDE create a file called `env.py`.
6. Inside the env.py file, add all the following environment variables which you will need for the project and you will access via import env:
- os.environ["DEVELOPMENT"] = "1"
- os.environ.setdefault(
    'SECRET_KEY', 'secretkeyhere')
os.environ.setdefault(
    'STRIPE_PUBLISHABLE', 'stripepublishablekey')
os.environ.setdefault(
    'STRIPE_SECRET', 'stripesecretkey')
os.environ.setdefault(
    'DATABASE_URL',
    'postgresdatabaseurl')
os.environ.setdefault(
    'AWS_SECRET_ACCESS_KEY', 'awssecretkey')
os.environ.setdefault(
    'AWS_ACCESS_KEY_ID', 'awsaccesskey')
7. Make sure to add env.py to a .gitignore file so it's not pushed to the repository.
8. Enter the following command into the terminal to migrate models into database.
`python3 manage.py migrate`
9. Create a 'superuser' for the project by entering the following command in the terminal and give all required credentials when prompted:
`python3 manage.py createsuperuser`
10. You can now run the application with the command
```python3 manage.py runserver```
11. The website is now running locally. 

## Heroku Deployment

To deploy the app to heroku, you would need to follow the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. Install add-ons, Heroku Postgres database.

5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the heroku app to the correct GitHub repository.

7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8. Set the following config vars:

| Key | Value |
 --- | ---
SECRET_KEY | `your_secret_key`
AWS_ACCESS_KEY_ID | `aws_access_key`
AWS_SECRET_ACCESS_KEY | `aws_secret_key`
DATABASE_URL | `postgres_database_url`
EMAIL_HOST_PASS | `email_host_password`
EMAIL_HOST_USER | `host_email_adddress`
SECRET_KEY | `django_secret_key`
STRIPE_PUBLISHABLE | `stripe_publishable`
STRIPE_SECRET | `stripe_secret`
USE_AWS | `True` (AWS Bucket name and region in [settings.py](https://github.com/mkuti/corklagos-venture/blob/master/corklagos/settings.py))
EMAILJS_USER_ID | `email_js_user_id`

9. Move all models to the new heroku database by typing the following command in the terminal:
`python3 manage.py migrate`

10. Create a 'superuser' for the new database by entering the following command in the terminal and give all required credentials when prompted:
`python3 manage.py createsuperuser`

11. In the heroku dashboard, click "Deploy".

12. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

13. The site is now successfully deployed [here](https://corklagos-venture.herokuapp.com/).

[Back to Top](#table-of-contents) 

# Credits
1. General credits

I first relied a lot on the course videos and previous mini-projects to fully understand the Django structures and functionality.

While I never litterally copied-pasted the code from the course, at the start of building the django apps (the user/profile app and the initial stages of the listings app) I did code along with the tutorials a lot. But I always ensured to understand it before applying to my own project and the specific needs of my app. Later I relied constantly on Django and different django-packages documentation to implement the desired functionality.

I relied heavily on django-allauth and django-filter documentation to understand how to implement each feature. 

I read and used the written tutorials of [Simple is better than complex](https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html) on django-filter and [The complete django-allauth guide](https://dev.to/gajesh/the-complete-django-allauth-guide-la3) on django-allauth for guidance.

In my testing document, I have referred each resource, Slack thread or Stack Overflow discussions I have used to debug my code and resolve any founds issues.

2. Logout functionality

For the logout feature on POST without the confirmation page, I followed the recommendation of django-allauth documentation to use Javascript [here](https://django-allauth.readthedocs.io/en/latest/views.html#logout). I then used a number of different github and Stack Overflow discussions to implement the Javascript feature.
- [https://stackoverflow.com/questions/43606056/proper-django-csrf-validation-using-fetch-post-request](https://stackoverflow.com/questions/43606056/proper-django-csrf-validation-using-fetch-post-request)
- [https://stackoverflow.com/questions/3521290/logout-get-or-post](https://stackoverflow.com/questions/3521290/logout-get-or-post)
- [https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CSRF_COOKIE_HTTPONLY](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CSRF_COOKIE_HTTPONLY)

3. Shortening the order number on past orders view

|truncatechars:10 from https://github.com/ckz8780/boutique_ado_v1/blob/master/profiles/templates/profiles/profile.html

4. How to css flip card

[https://www.w3schools.com/howto/howto_css_flip_card.asp](https://www.w3schools.com/howto/howto_css_flip_card.asp)

5. Navbar with centered logo

[https://bootstrapcreative.com/pattern/navbar-centered-logo-links-left-right/](https://bootstrapcreative.com/pattern/navbar-centered-logo-links-left-right/)

6. Remove asterisk from the crispy forms fields

[https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html?highlight=remove%20label_suffix%20on%20required#change-required-fields](https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html?highlight=remove%20label_suffix%20on%20required#change-required-fields)

7. Modify a boolean field in django

- [https://stackoverflow.com/questions/42089277/how-to-modify-a-boolean-field-model-in-django](https://stackoverflow.com/questions/42089277/how-to-modify-a-boolean-field-model-in-django)
- [https://www.geeksforgeeks.org/booleanfield-django-models/](https://www.geeksforgeeks.org/booleanfield-django-models/)

8. Credits to [Malia Havlicek](https://github.com/maliahavlicek) for providing the code of the border-image inside the body so the border banner could be beautifully rendered. See [commit 870d8241a11bc76b7439503c442b91802f7e45b3](https://github.com/mkuti/corklagos-venture/commit/870d8241a11bc76b7439503c442b91802f7e45b3).

9. Credits to [JimLynx](https://github.com/JimLynx) in Slack who re-worked on the logo for me to make it cleaner and brighter.

10. Credits to [Simen Dehlin](https://github.com/Eventyret) for helping me to find the forgotten inline styling on the html logo element which could not render the logo well on large screens.

# Special thanks

To my mentor, [Simen Dehlin](https://github.com/Eventyret), who has accompanied me for the past 9months along this coding journey, who has always provided professional guidance, who has given so much time, support and encouragement, pushing and challenging me to go further and beyond so I could deliver great project!

To my study-buddy [Malia Havlicek](https://github.com/maliahavlicek) who has constantly encouraged me during the project development, who has tested the website when deployed and helped me to find various bugs and guidance on how to resolve them.

To [Chris Z.](https://github.com/ckz8780) for always answering my questions, even when I am sinking under my own complexity, for trying to provide guidance and resources without giving solutions. This helped me to push further and resolve my own issues which was so great!

To my two sons Léon and Seyi whose time with me has been sacrificed hugely lately, for being patient with me when I am tired after sleepless nights.
To my husband who has provided support to me and care to our children in the past year.

##### Disclaimer:
The content of the website is for educational purposes only.

[Back to Top](#table-of-contents) 