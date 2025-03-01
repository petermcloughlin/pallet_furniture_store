# PALLET-FURNITURE-STORE

![Am-I-Responsive](/documentation/validations/am-i-responsive/am-i-responsive.PNG)

## Introduction
Welcome to the Pallet Furniture Store,

This is an online furniture store which builds, assembles and sells bespoke, han-dmade furntiure from refurbished, used and un-used pallets. This is a business set up with both the customer and the environment in mind. At the Pallet Furniture Store, our dedicated team have partnered up with a number of building contractors and small businesses, nationwide to ensure a policy of reduced waste and increased recycling continues, whilst supporting our team members as they provide a continuous range of bespoke fuurniture pieces, for both home and gardens, all made from refurbished, used and unused pallets.

You can access the deployed site [here](https://django-pallet-furniture-a8821c2711e7.herokuapp.com/)

The site allows visitors to browse our latest range of products currently in stock at our storage base in Cork. The site visitor is also welcome to register with us as a customer, from which they can create their own profile and make purchases using our secure online checkout facility which uses Stripe's payment gateway.

If you wish to make a test purchase, you can use the following [Stripe Dummy Card](https://stripe.com/docs/testing) details:

- Success Card Number: 4242 4242 4242 4242
- Expiry: 04/25
- CVC: 242
- ZIP: 42424

Any payments made using a valid debit/credit card will not be processed and the card will not be charged. No orders made will be fulfilled.

For full Admin access to Django Admin panel with relevant sign-in credentials: [Pallet Furniture Store Admin](https://django-pallet-furniture-a8821c2711e7.herokuapp.com/admin/)

## Table of Contents

- [Pallet Furniture Store](#pallet-furniture-store)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Customer Goals](#customer-goals)
  - [Business Goals](#business-goals)
- [UX/UI - User Experience/User Interface](#uxui---user-experienceuser-interface)
  - [Design Inspiration](#design-inspiration)
    - [Color Scheme](#color-scheme)   
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies](#agile-methodologies)
    - [MoSCoW Prioritization](#moscow-prioritization)
  - [Marketing](#marketing)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)  
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Defensive Design](#defensive-design)
- [Features](#features)
  - [User View - Guests/Account Holders](#user-view---guestsaccount-holders)
  - [CRUD Functionality](#crud-functionality)
  - [Features Showcase](#features-showcase)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project SetUp](#django-project-setup)
  - [Heroku Deployment](#heroku-deployment)
  - [Google Mail Setup](#google-mail-setup)
  - [AWS Config](#aws-config)
    - [Media Folder Setup](#media-folder-setup)
    - [Django AWS Connect](#django-aws-connect)
  - [Stripe Config](#stripe-config)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Overview
Pallet Furniture Store is an eco-friendly furniture store focusing on procuring the best in sustainable, long-life products. Users are invited to:

- View the store as Guests
- Register for an Account
- Submit bespoke requests to our team
- Browse products by category and price
- View, add and edit products in their bag
- As registered users, view past orders through their profile page
- Submit reviews letting us know their thoughts about our service
- Suscribe to our mailing list using mailchimp's facility in the site's footer

Pallet Furniture Store is accessible via all browsers with full responsiveness on different screen sizes. Its aim is to provide eye-catching , bespoke home and garden furnishings, whilst reducing waste nationally.

## Customer Goals

Customers are provided with an easy, intuitive shopping experience and are encouraged to avail of sustainable, eco-friendly home and garden furniture. It is hoped that customers will sign up/register an account with the Pallet Furniture Store and make purchases and send us their thoughts via our Service Review option. A sense of community is created with a mailing list subscription, which will inform the customers of new products, trends and articles related to the Pallet Furniture Store.

## Business Goals

Pallet Furniture Store provides easy Admin functionality for the business owner with an accessible, easy-use Admin Dashboard to manage the product details and information in our store. The additional frontend forms allows the business owner to make quick and easy changes. Further information regarding users and orders can be accessed via the Admin Dashboard stored within the Django Admin Panel.

Pallet Furniture Store seeks to build a strong base of regular shoppers who seek long-life, quality products made from high quality, natural materials. The newsletter, articles and carbon footprint features aim to attract those who have concerns for the rising environmental issues that our planet faces. Further marketing is made through the businesses social media channels, in particular their Facebook page which is accessible in the footer link.

# UX/UI - User Experience/User Interface

## Design Inspiration
From the beginning of the project, I knew that the colour palette would reflect the wooden pallet theme with shades of gold and yellow acting as the primary colour, in particular boostraps warning colour along with #E2AE3F and #b18600. The website is kept clean, with good flow, using plenty of white space to draw attention to the products and the website's mission in reducing the carbon footprints of its users.

A simple wooden pallet is used as a favicon branding logo. The logo depicts a simple wooden box made from wooden planks.

Only the necessary information is displayed so as to not increase the size of the website and its own carbon footprint.  I created a home page background image, displaying a close up view of stacked pallets at our store, with some contrasting colouring to facilitate the purchase behind the website deliverables.

![Home Page Background Image](documentation/readme_images/pallets.jpg)
*Image taken from Pexels images*

Feedback is continuously provided to the user via the website's header which displays whether the user is logged in and how many items are in their bag. Message 'toasts' are also visible upon user actions to display further information. Buttons are kept similar for continuity.

![Header Feedback](documentation/readme_images/toast.PNG)  
*Header feedback is kept clean and intuitive*

### Color Scheme

Variables were used within the CSS file to call colours as they were needed:
- #b18600; Gold
- #E2AE3F; Light gold
- #000; Black
- #555; Grey
- orange; 

The above colours were chosen to reflect colours found naturally within the theme of the homepage background image. 

![Site Shop Now Button](documentation/readme_images/show-now-button.PNG)  
*Pallet Furniture Store - Shop Now Button*

The hover effect uses a light and darker version of its colour when the mouse pointer is hovered over it by the user, which provides feedback that there is an action available in the feature/area.

This colour theme was used throughout the site in keeping with the pallet theme, whilst using black text for clear visual contrast and readability.

# Project Planning

## Strategy Plane
The primary objective was to create an e-commerce store that satisfied the assessment criteria of the Code Institute's Project 5: E-Commerce Module. The store must provide the expected functions of a responsive e-commerce store using Stripe as a payment system, user/guest views for authentication and store features along with some extra features of my choosing, Bespoke requests and Service reviews, and FAQ's.

The site's design and graphic assets were collected through various copyright-free image websites. Images were edited for the website to be cohesive. The home page background image was taken from Pexels Images. Bootstrap and Crispy Forms were used for the project's frontend to speed up the process and to keep the templates consistent. Further customisation to the buttons, forms, modals, toasts and user feedback processes were added to the project's CSS files. 

If a customer chooses to make a purchase then they are given consistent feedback through the use of 'toasts' messages and confirmation emails. The purchasing process is presented using Stripe payment handlers, obtained and setup using [Stripe's](https://stripe.com/docs) documentation and website.

### Site Goals

- Site provides enjoyable experience for shoppers.
- Customers are informed about the business purpose and our service provision via the About page and FAQ's Page.
- UX remains similar across screen sizes.
- CRUD functionalities work as intended with easy to use frontend forms.
- Scalable site to allow for extra features in the future.

## Agile Methodologies

The Pallet Furniture Store followed Agile planning methodologies to its completion. [GitHub Projects](https://github.com/users/petermcloughlin/projects/9) provided an ideal platform to create issues, boards and milestones for each of the project's Epics. Keeping focused on individual sections as I built the Pallet Furniture Store reduced the number of bugs and human errors.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for the Pallet Furniture Store, identifying and labeling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project.
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release.

## Marketing

An [Pallet Furniture Store Facebook Page](https://www.facebook.com/profile.php?id=61573319522718) was created to demonstrate promotion of the Pallet Furniture Store on social media. Posts informing customers of deals and new products would be made on the page with the hopes of drawing in more revenue. Facebook provides an easy, minimal-step process to allow business owners to promote their business, with additional paid 'boost' features to further promote and spread the reach of the posts. Pallet Furniture Store also offers a newsletter subscription service through MailChimp. The benefit of both of these services is that the customer is not forced to sign up to either and potentially worry that they will be spammed with an unnecessary amount of information. Pallet Furniture Store avoids this in order to keep its brand clean and uphold its eco-friendly efforts.

Within the head's meta tags of the base template are researched keywords and a description of Pallet Furniture Store's goal as a business. These keywords have been researched using[Wordtracker](https://www.wordtracker.com/) to ensure that both short-tail and long-tail keywords are included.

In addition to this, sitemap.xml and robots.txt files are included to increase the site's visibility. These files are essential for SEO (Search Engine Optimisation). The sitemap.xml was generated using [XML Sitemap](https://www.xml-sitemaps.com/) and included in the root folder of the project. A robots.txt file was created in the root folder to instruct search engine crawlers on how to access and crawl the site's pages.

![Pallet Furniture Store Facebook Business Page](documentation/readme_images/facebook-profile.PNG)
*Pallet Furniture Store Facebook Business Page*

## User Stories

### Visitor User Stories

I used the Useer Story Plan below to plan out the flow of development stages of the project.
[User Story Plan](documentation/Tests/TestPlan.xlsx)

These User Stories were followed using the Agile Development methodology within my project's Board, completing each user story , fulfilling each Epic goal.

[My Project Board](https://github.com/users/petermcloughlin/projects/9)

## Scope Plane

To focus on the learning of the Stripe API and webhook handlers that would ultimately drive the inner workings of the project, I kept my Pallet Furniture Store scope lower than my previous project, Bandon Dog Groomers. A working e-commerce store was essential so I initially planned to keep to the MVP to ensure that I would complete the project successfully.

Aside from the CRUD fuctionality and online shopping component build, I added my own extra functionalities - Bespoke requets page, Frequently Asked Questions(FAQ) and a Service Review form( which is only available to registered users).

Django's MVT framework allowed these features to be built quickly and addition of an Admin frontend panel for managing store products created a robust e-commerce site that could start taking orders.

Essential features were:
- User Accounts with AllAuth
- Payment system with Stripe
- Product inventory management - Full CRUD
- Shopping UX with Bag and Checkout processes - Full CRUD
- Site responsivity
- Business details to inform the user

## Structural Plane

Pallet Furniture Store is built using Bootstrap, with Code Institute's Boutique Ado e-commerce project as its foundation. However, I picked apart the structure and styling to fit my own vision and changed quite a bit of the code.  The Pallet Furniture Store icon was used as the Favicon.

Bootstrap allowed for easy transition between screen sizes as many ecommerce purchases are made using our mobiles, so this was a priority focus. Bootstrap components such as forms and an accordion section raised the spec of the project, to give it a professional finish.

## Skeleton & Surface Planes

### Wireframes

[Figma](https://www.figma.com) was used to create basic wireframes for Everneed. I had a vision of what the site would look like from the beginning so the planning process went smoothly. Figma allows easy creation of wireframes to the appropriate frame sizes for different screens. Addition of icons and extra design features is easy with their Plugins component which can connect to Flaticon for example.

<details open>
    <summary>Desktop/Tablet Home Page Wireframe</summary>  
    <img src="">  
</details>

<details>
    <summary>Mobile Home Page Wireframe</summary>  
    <img src="">  
</details>

### Database Schema

![Pallet Furniture Store Ecommerce ERC](documentation/erd/ERD.PNG)  
*Database Schema (ERD) for Pallet Furniture Store displaying relationships between feature components saved within the database*

[Lucidchart](https://www.lucidchart.com/pages/) was used to create the ERD(Entity Relationship Diagram) for Pallet Furniture Store. To satisfy the assessment criteria, multiple models were created to personalise the project. These include:
- **StoreProduct**: Store Products may be added by Admin with image and text fields within the Add/Edit Product forms.
- **CustomerOrder**: Displays the customer's personal, billing and cost information, inclusive of delivery cost.
- **BespokeRequest**: The Bespoke Request model takes simple values from the user to make bespoke requests for specific product requirements they might like for a new design.
- **FAQ**: The Frequently Asked Questions page was added with the customer in mind. This was a very useful tool, added to give the customer some extra reassurance before making their purchase.
- **ServiceReview**: This facility was added only for registered users who wish to leave a review of the service they receive from Pallet Furniture Store, to help with further developments of product creation, service and delivery.

### Defensive Design

Pallet Furniture Store was developed to ensure a reliable user experience. It's intention was to cause no frustrations for the users and to ensure they return to make further purchases.

- Django AllAuth for user registration/log in/log out
- Input validation and error messages provide feedback to the user to guide them towards the desired outcome. 
- Unregistered users are diverted to the Sign Up page from restricted access pages. 
- Authentication processes control edit/delete icons to reveal them to the Admin only, this is further secured through accessing of CRUD functionalities in the Admin Dashboard. 
- Deletion of data is confirmed through an additional modal, double-checking with the user.
- Error pages are displayed with 'Products' buttons to help users get back on track to the shopping experience. 
- Testing and validation of features completes the process.

**CSRF Tokens**

CSRF (Cross-Site Request Forgery) tokens are included in every form to help authenticate the request with the server when the form is submitted. Absence of these tokens can leave a site vulnerable to attackers who may steal a user's data.

# Features

## User View - Guests/Account Holders

| Feature   | Guest | Registered, Account Holder |
|-----------|-------------------|-----------------|
| Home Page | Visible           | Visible         |
| Profile  | Not Visible - 'Profile' option only appears for registered, logged-in users | Visible and full feature interaction available |
| All Products  | Visible - items can be viewed and added to Bag | Visible and full feature interaction available |
| Service Review   | Not Visible | Visible and full feature interaction available |
| Read   | Visible | Visible |
| Subscribe to Us (MailChimp) | Visible | Visible |
| Admin Dashboard | Not Visible | Only visible to Admin |

## CRUD Functionality

Customers have full CRUD functionality with their prospective purchases. They may edit their bag, add more items or remove all items. They may also edit their delivery details if they are registered, logged-in users. Everneed Admin have access to the Admin Dashboard which allow them full CRUD over Product Management and Article posting.

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Profile | On registration | Yes, delivery details and order history | Yes, update address | No, users are unable to delete their accounts, this is restricted to Admin |
| Bag | Yes, customers may add to their bag | Yes | Yes, items can be added/removed | Yes |
| Products | Yes, Admin only | Yes, all users | Yes, Admin only | Yes, Admin only |
| Articles | Yes, Admin only | Yes, all users | Yes, Admin only | Yes, Admin only |

## Features Showcase

**Header & Navigation - All Users**
Pallet Furniture Store's navbar is kept clean, with a simple dropdown menu for the 'All Products' section. 
- The Split dropdown options for both Home and Garden, keep the navigation categorised for searching
- The Account dropdown displays options for Profile for registered, logged in users and with a Leave a Review option in the navbar.
- The bag displays the number of items within it if the customer adds an item to it.

The collapsible navbar compacts these options into a neat burgar icon.

**Home Page - All Users**

The Pallet Fruniture Store Home Page invites the user in with a large background image, tajen from Pexels.com. An 'Shop Now' button brings the user straight to the 'All Products' page. 
Below this is the Mission section with a smooth scroll animation fade-in and underline when the user moves down the flow of the page. Here the customer can identify the business's core values.

A simple accordion section for business FAQ's follows this, answering a broad spectrum of possible customer questions.

<details open>
    <summary>Home Page Navbar - All Users</summary>  
    <img src="documentation/home_page/nav.PNG">  
</details>

<details>
    <summary>Home Page Background and Shop Now - All Users</summary>  
    <img src="documentation/home_page/home.PNG">  
</details>

<details>
    <summary>Home Page Footer - All Users</summary>  
    <img src="documentation/home_page/footer.PNG">  
</details>

<details>
    <summary>FAQ's- All Users</summary>  
    <img src="documentation/home_page/faq.PNG">  
</details>

**All Auth - All Users who wish to create an account**

Django AllAuth provides a comprehensive, customisable authentication system that keeps user data safe. If a customer wishes to register an account they may enter their username and email and password x 2 to ensure precision. Upon submitting the form the user will receive an email to validate their email and then sign in to Pallet Furniture Store. Similar to all form fields throughout the site, I have applied bootstrap styling to keep in line with Pallet Furniture Store's design. The log in page is similar to the register page with the log out page presenting the user with two buttons to continue the log out process or to return home.

Feedback is continually released to the user through toast messages to confirm successful registration, log in and log out.

AllAuth handles password reset by sending an email to the user with a link to change their password to something new.
<details open>
    <summary>Register - All Users</summary>  
    <img src="documentation/readme_images/sign-up.PNG">  
</details>

<details>
    <summary>Login - All Users</summary>  
    <img src="documentation/readme_images/login.PNG">  
</details>

<details>
    <summary>Log Out - All Users</summary>  
    <img src="documentation/readme_images/logout.PNG">  
</details>

**Account - Registered, logged in User**

The Account page for Pallet Furniture Store is kept simple, with only relevant information and functionality. The registered, logged in user may adjust their personal, delivery address to be autofilled into their checkout form when making a purchase. Previous purchases are displayed in the Order History, displayed by most recent date.

<details open>
    <summary>Account Toast - Registered, logged-in Users</summary>  
    <img src="documentation/Tests/confirm-login.PNG">  
</details>

<details>
    <summary>Account View - Registered, logged-in Users</summary>  
    <img src="documentation/readme_images/profile.PNG">  
</details>

**All Products - All Users**

Pallet Furniture Store sells a hand-made list of furniture products for both home and garden, built using refurbished used and un-used pallets.

The product list and product details pages are kept responsive and neat thanks to Bootstrap's grid system to collapse the rows into single columns. Products may be sorted according to price ascending, price descending and category using the dropdowns under All Products, Home and Garden.

Admin may access the Admin Dashboard to add/edit/delete any items within the database. Crispy Forms renders the adding/editing forms.No information is lost when viewing the website on mobile view. All screen sizes display the same information to give all users the same experience.

<details open>
    <summary>All Products Desktop - All Users</summary>  
    <img src="documentation/readme_images/all-products-desktop-user.PNG">  
</details>

<details>
    <summary>All Products Mobile - All Users</summary>  
    <img src="documentation/readme_images/all-products-mobile-user.PNG">  
</details>

<details>
    <summary>Product Detail Desktop - All Users</summary>  
    <img src="documentation/readme_images/product-details-desktop-user.PNG">  
</details>

<details>
    <summary>Product Detail Mobile - All Users</summary>  
    <img src="documentation/readme_images/product-details-mobile-user.PNG">  
</details>

<details>
    <summary>Admin Product List - Logged-In, Admin only</summary>  
    <img src="documentation/readme_images/all-products-desktop-admin.PNG">  
</details>
<details>
    <summary>Admin Product Details Mobile - Logged-In, Admin only</summary>  
    <img src="documentation/readme_images/all-products-mobile-admin.PNG">  
</details>


**Categories - All Users**

Pallet Futniture Store keeps it's shopping experience clean and easily accessible with six categories:
- Tables & Chairs
- Benches & Racks
- Stands
- Beds
- Coffee Tables
- Other

All split in Garden and Home under the navbar dropdowns.


**Bag - All Users**

Pallet Furniture Store's Shopping Bag feature is presented in a clean and clear format to correctly and quickly inform the user of their possible purchase choices. The customer has the option to change the amounts of the items that they wish to buy or to remove them completely from the bag. The customer is shown their running totals as well as their delivery charge and their carbon saved and carbon footprint total. When products are added/updated/removed to/from the bag, then a toast message displays to give the customer feedback on their most recent choice.

A clear message is shown if there are no items in the bag and a 'Keep Shopping' button redirects the user back to the 'All Products' page. A standard delivery of €10 is applied to all shopping bags which is reflected in the grand total price.

**Checkout - All Users**

The checkout process for Pallet Furniture Store is operated through the [Stripe](https://stripe.com/docs) API. As stated above -> If you wish to make a test purchase, you can use the following [Stripe Dummy Card](https://stripe.com/docs/testing) details:

- Success Card Number: 4242 4242 4242 4242
- Exp Date: 04/25
- CVN: 242
- Postcode: 42424 

Any payments made using a valid debit/credit card will not process and the card will not be charged. No orders made will be fulfilled.

When the customer has added items that they wish to purchase to their bag, they are given the option to proceed to 'Secure Checkout' to complete their order. This checkout form contains a personal, delivery/billing information form that will display previously entered details if the user is logged in and had previously ticked the box to save their details. The Stripe Payment form accepts the user's information and will inform them if they attempt to use an invalid card. Validation is also present in the delivery form area, to remind the user if they have not entered all of the relevant details.

The items the customer has chosen are visible on the right hand side of the webpage with their grand total for their order.

Once the Checkout form has been submitted, a loading spinner informs the user that their payment is processing. Stripe's webhook handlers make this process smooth as the payment may attempt 9 times before being unsuccessful overall. In the Developer's view in the Stripe Dashboard, developers can check the webhook and payment processes to confirm they are working correctly.

A confirmation email for the order is emailed to all customers. This details their spending amount and the date of their purchase. Their totals and items purchased are also visible in the checkout success page upon successful payment processing. If the user is logged in, they can view this order and all previous orders, if they were logged in at the time of purchase, in their profile view.

**Service Review - Registered, logged in Users only**
All registered user's will see an extra option in the navbar to Leave A Review where by they can sibmit their thoughts on the service provided to the Pallet Furniture Store.

**Footer - All Users**
Pallet Furniture Store's footer is brightly coloured with gold colour background to contrast against the site's important white space. Mail Chimp's newsletter subscription form for users to sign up for weekly emails lies at the centre below the interactive location map. Across from this are a list of links that aim to give the customer all of the information they would need about Pallet Furniture Store.

 A Facebook page for Pallet Furniture Store opens in a new tab using the facebook icon link, as does a Twitter page, Instagram, YouTube, Pintrest and LinkedIn.

At the bottom left are the Open Hours for the business and to the right of the map is the location address and contact details.

<details open>
    <summary>Footer - All Users</summary>  
    <img src="documentation/home_page/footer.PNG">  
</details>


## Future Features
Some features which, upon completion of this project, I would like to add in time will include the following;

- A section added to the about page or home page which could display a number of recently added positive reviews from customers who are registered with the Pallet Furntiure Store. 
- A customer boostrap carousel which suggested items to display to a logged in user, based on collated data and insights based on their previous purchases with the store.
- A mail campaign with special discounts and offers to registered customers on their birthdays, using their personal data, although this would require some extra data feeds collecting date's of brith's of registered customers.

These are some features which create a real sense of community and belonging for customers and are regularly used as marketing techniques by larger, well known online shopping platforms.

# Technologies & Languages Used

- HTML
- CSS
- Bootstrap
- JavaScript
- JQuery
- Python
- [Git](https://git-scm.com/) used for version control.
- [Github](https://www.github.com) used for online storage of codebase and Projects tool.
- [CodeAnywhere](https://app.codeanywhere.com) as an online, cloud-based IDE for development.
- [Figma](https://www.figma.com) for project design planning and wireframe creation.
- [Adobe Color](https://color.adobe.com) for colour theme creation and accessibility checkers.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Heroku](https://www.heroku.com) was used to host the 'everneed' application.

## Libraries & Frameworks

Libraries and frameworks used were dictated by the 'Boutique Ado' walkthrough from our course material with the Code Institute. This project will be upgraded on completion of the course to more recent packages to meet current standards and security packages.

- [Django v3.2](https://docs.djangoproject.com/en/4.2/releases/3.2/) 
- [AllAuth](https://django-allauth.readthedocs.io/) for user authentication and account management.
- [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) for template rendering.
- [Crispy Forms](https://pypi.org/project/crispy-bootstrap4/) for form rendering.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for AWS CRUD with Python scripts.
- [dj-database-url](https://pypi.org/project/dj-database-url/) for DATABASE_URL.
- [django-countries](https://pypi.org/project/django-countries/) for country field rendering in checkout form.
- [django-storages](https://django-storages.readthedocs.io/en/latest/) for handling static and media files.
- [gunicorn](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/gunicorn/) apure-Python WSGI server for UNIX.
- [oauthlib](https://pypi.org/project/oauthlib/) OAuth request-signing logic.
- [psycopg2](https://pypi.org/project/psycopg2/) s PostgreSQL database adapter for Python.
- [Stripe](https://stripe.com/en-ie) for processing Everneed's payment system.

## Tools & Programs
- [ImageCompressor](https://imagecompressor.com/) for compressing PNG/WEbp files
- [Convertio](https://convertio.co/) for file conversion to PNG, WEBP.
- [Tiny Png](https://tinypng.com/) for file size reduction.
- [Lucidchart](https://www.lucidchart.com/pages) for ERD (entity relationship diagram) creation.
- [Favicon](https://favicon.io/) for converting an icon into a favicon.
- [amiresponsive](https://ui.dev/amiresponsive) for screenshot of Everneed on different screen sizes.
- [LeafletJS](https://leafletjs.com/index.html) for the interactive location map in the footer
- [Mailchimp](https://mailchimp.com/) is used for marketing with their newsletter subscription service.


# Testing

- [Testing](#testing)  
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
  - [Manual Testing](#manual-testing)
    - [Responsiveness](#responsiveness)
    - [Test Plan Results](#test-plan-results)


## HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.


All HTML pages were validated and received a 'No errors or warning to show' for code that I had written, result as shown above.

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- |
| Home | 0 | 0 |
| Log In | 0 | 0 |
| Register | 0 | 0 |
| Account | 0 | 0 |
| Bespoke Request | 0 | 0 |
| FAQ | 0 | 0 |
| Admin Dashboard | 0 | 0 |
| Admin Product List | 0 | 0 |
| Admin Product Detail | 0 | 0 |
| Admin Add Product | ID error -> Errors/Warnings present as a result of Bootstraps form elements, not from the code that I have created. The name ID from the contact form html within the base.html is clashing with the name ID from the add product html. These ID elements are embedded within the Bootstrap forms and are inaccessible to me without breaking my code up and reconfiguring the code. I will reinvestigate and break into the code when my Diploma has been awarded to remove errors like these. [html validation duplicate id bootstrap forms](documentation/validations/html/HTML_Errors/add_product.PNG) | As before |
| Admin Edit Product | 1 - same as Admin Add Product | 0 |
| Admin Delete Product | 0 | 0 |
| All Products | 0 | 0 |
| User Product List | 0 | 0 |
| User Product Details | 0 | 0 |
| Bag - Products | 1 - same as Admin Add Product | 0 |
| Checkout | 0 | 1 |
| Profile | 0 | 0 |
| Forgot Password | 0 | 0 |
| Error 404 | 0 | 0 |
| Error 500 | 0  | 0 |

## Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by myself. No issues presented and line lengths were double checked. I have included some screenshots with the results below. 
#### Products
<details>
    <summary>Products - Forms.py</summary>  
    <img src="documentation/validations/products/forms.PNG">  
</details>
<details>
    <summary>Products - models.py</summary>  
    <img src="documentation/validations/products/models.PNG">  
</details>
<details>
    <summary>Products - urls.py</summary>  
    <img src="documentation/validations/products/urls.PNGG">  
</details>
<details>
    <summary>Products - views.py</summary>  
    <img src="documentation/validations/products/views.PNG">  
</details>
<details>
    <summary>Products - widgets.py</summary>  
    <img src="documentation/validations/products/widgets.PNG">  
</details>

#### Profile
<details>
    <summary>Profile - forms.py</summary>  
    <img src="documentation/validations/profiles/forms.PNG">  
</details>
<details>
    <summary>Profile - models.py</summary>  
    <img src="documentation/validations/profiles/models.PNG">  
</details>
<details>
    <summary>Profile - urls.py</summary>  
    <img src="documentation/validations/profiles/urls.PNG">  
</details>
<details>
    <summary>Profile - views.py</summary>  
    <img src="documentation/validations/profiles/views.PNG">  
</details>

#### Service Reviews
<details>
    <summary>Service Review - models.py</summary>  
    <img src="documentation/validations/service-review/models.PNG">  
</details>
<details>
    <summary>Service Review - views.py</summary>  
    <img src="documentation/validations/service-review/views.PNG">  
</details>

#### Bag
<details>
    <summary>Bag - contexts.py</summary>  
    <img src="documentation/validations/bag/contexts.PNG">  
</details>
<details>
    <summary>Bag - urls.py</summary>  
    <img src="documentation/validations/bag/urls.PNG">  
</details>
<details>
    <summary>Bag - views.py</summary>  
    <img src="documentation/validations/bag/views.PNG">  
</details>

#### Bespoke Requests
<details>
    <summary>Bespoke Requests - models.py</summary>  
    <img src="documentation/validations/bespokerequests/models.PNG">  
</details>
<details>
    <summary>Bespoke Requests - forms.py</summary>  
    <img src="documentation/validations/bespokerequests/forms.PNG">  
</details>
<details>
    <summary>Bespoke Requests - urls.py</summary>  
    <img src="documentation/validations/bespokerequests/urls.PNG">  
</details>
<details>
    <summary>Bespoke Requests - views.py</summary>  
    <img src="documentation/validations/bespokerequests/views.PNG">  
</details>

#### Checkout
<details>
    <summary>Checkout - models.py</summary>  
    <img src="documentation/validations/checkout/models.PNG">  
</details>
<details>
    <summary>Checkout - signals.py</summary>  
    <img src="documentation/validations/checkout/signals.PNG">  
</details>
<details>
    <summary>Checkout - forms.py</summary>  
    <img src="documentation/validations/checkout/forms.PNG">  
</details>
<details>
    <summary>Checkout - urls.py</summary>  
    <img src="documentation/validations/checkout/urls.PNG">  
</details>
<details>
    <summary>Checkout - views.py</summary>  
    <img src="documentation/validations/checkout/views.PNG">  
</details>
<details>
    <summary>Checkout - webhook_handler.py</summary>  
    <img src="documentation/validations/checkout/webhook_handler.PNG">  
</details>
<details>
    <summary>Checkout - webhooks.py</summary>  
    <img src="documentation/validations/checkout/webhooks.PNG">  
</details>

## CSS Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS files. External CSS for Bootstrap, provided by [CDN](https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css) was not tested.

To keep my document concise I have not included every screenshot of the CSS validations, as they are all the same, but the results are as follows.

| CSS File | Errors | Warnings |
| ---- | ------ | -------- |
| Checkout | 0 | 0 |
| Profiles | 0 | 0 |
| Base CSS | 0 | 0 |

### Lighthouse Scores

Lighthouse testing was carried out in Incognito mode to achieve the best result. Images used in the site's design were saved in png format, and compressed using [tinypng](https://tinypng.com/) and [Convertio](https://www.convertio.co) to offer the best chance for a decent performance score.

Results can be seen below;
<details>
    <summary>Home</summary>  
    <img src="documentation/validations/lighthouse/desktop/HomePage.PNG">  
</details>
<details>
    <summary>About</summary>  
    <img src="documentation/validations/lighthouse/desktop/About.PNG">  
</details>
<details>
    <summary>Bespoke Requests</summary>  
    <img src="documentation/validations/lighthouse/desktop/bespokerequest.PNG">  
</details>
<details>
    <summary>FAQ</summary>  
    <img src="documentation/validations/lighthouse/desktop/faq.PNG">  
</details>
<details>
    <summary>Service Review</summary>  
    <img src="documentation/validations/lighthouse/desktop/service-review.PNG">  
</details>
<details>
    <summary>Products</summary>  
    <img src="documentation/validations/lighthouse/desktop/Products.PNG">  
</details>
<details>
    <summary>Product Details</summary>  
    <img src="documentation/validations/lighthouse/desktop/ProductDetails.PNG">  
</details>
<details>
    <summary>Profile</summary>  
    <img src="documentation/validations/lighthouse/desktop/profile.PNG">  
</details>
<details>
    <summary>Bag</summary>  
    <img src="documentation/validations/lighthouse/desktop/bag.PNG">  
</details>
<details>
    <summary>Checkout</summary>  
    <img src="documentation/validations/lighthouse/desktop/checkout.PNG">  
</details>
<details>
    <summary>Checkout-Success</summary>  
    <img src="documentation/validations/lighthouse/desktop/checkout-success.PNG">  
</details>

## Manual Testing
For this project I used manual testing of the various components made up within the site.
This testing process included the following;
- Code validation
- Site Repsonsiveness Checks
- Functional Testing in line with user story goals and epics

Throughout the build of this project which was built using the Agile methodology of Software Develpoment Lifecycle, each compnent or function was manually tested to ensure the particular user story goal was achieved, before moving on to the next step.

I created a Test Plan, in line with the objectiives set out in each user story within each epic.

### Test Plan Results
[TestPlan](documentation/Tests/TestPlan.xlsx)

### Responsiveness
Upone completion of the project, I used the [am-i-responsive](https://ui.dev/amiresponsive) online tool to generate a multi device view of the site's home page.

<details>
    <summary>Pallet-Furniture-Store</summary>  
    <img src="documentation/validations/am-i-responsive/am-i-responsive.PNG">  
</details>

Using the Bootstrap framework allowed a more rapid development of a responsive website. Starting with mobile first, Pallet Furniture Store was created to ensure the customer has an unhindered, positive experience when shopping. Pallet Furniture Store was regularly tested during development using Dev Tools to check for display issues on iPhone, Samsung Galaxy devices, iPad/iPad Pro and laptop/desktop screen sizes. Once deployed to Heroku, Pallet Furniture Store was tested on real world devices. No major issues were detected, changes were made to the checkout view to remove the product image on smaller screens and only display important product information. There were no major differences between desktop and tablet views thanks to the Bootstrap Grid system of columns.


# Deployment

## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.

During the course of this project, I had to migrate my workspace from GitPod to a localised version of VS Code on my machine, from which I regularly commited any changes to my GitHub repository.

## Django Project SetUp

Install Django and supporting libraries:

- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2``` 
  
1. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
2. Create a new Django project in the terminal ```django-admin startproject everneed .```
3. Create a new app eg. ```python3 mangage.py startapp home```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'home',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLfromElephantSQL>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  
9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```
10. Set up the templates directory in **settings.py**:

- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in the top level of the project file in the IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn everneed.wsgi```
12. Make the necessary migrations again.

## Heroku Deployment

To start the deployment process, please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'.
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your:

   - **DATABASE_URL**:**postgres://...**
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   - **SECRET_KEY** and value  
   - **EMAIL_HOST_PASS** and value
   - **EMAIL_HOST_USER** and value
   - **STRIPE_PUBLIC_KEY** and value
   - **STRIPE_SECRET_KEY** and value
   - **STRIPE_WH_SECRET** and value
   - **CLOUDINARY_URL** and value
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
2. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
3. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
4. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
5. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
6.  Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project.

## Google Mail Setup

1. Setup a Gmail Account that will be used to hold and store the emails for your project.
2. Logged in, navigate to **Settings** -> **Other Google Account Settings** -> **Accounts** -> **Import** -> **Other Account Settings**
3. Activate 2-Step Verification
4. Once verified access **App Passwords** -> **Other** -> enter a name for the password, eg Everneed.
5. Click **Create** -> copy the 16 digit password that is generated.
6. Add EMAIL_HOST_PASS, EMAIL_HOST_USER variable, password and email address to your Heroku Config Vars

## Stripe Config

Stripe's API is used to handle Everneed's payment system. To setup follow the below steps:

1. Create and log in to a Stripe account.
2. In the Stripe Dashboard -> **Get your test API keys.**
3. Add your `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` to your env.py, connect to your settings.py using your environment variables and then enter them into your project's Heroku Config Vars.
4. Including Stripe's Webhooks creates a failsafe if a customer exits the page during payment authorisation. In Stripe's Dashboard -> **Developers** -> **Webhooks** -> **Add Endpoint**: 'herokuapp url/checkout/wh'
5.  Choose **Retrieve all events** -> **Add Endpoint**.
6.  Add new key **STRIPE_WH_SECRET** to env.py, settings.py and Heroku Config Vars as before.

# Credits

## Code

The following blogs/tutorials complimented my learning for this project, alongside the [Code Institute's](https://codeinstitute.net/ie/) Learning Content. The Portfolio Project 5 - Boutique Ado provided a foundation which I took apart and altered to fit my project's design

- [Django Docs](https://www.djangoproject.com/)
- [Bootstrap Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Code Institute's](https://github.com/Code-Institute-Org>) Blog/Boutique Ado walkthroughs
- MailChimp subscription facility [MailChimp](https://mailchimp.com/)
- LeafletJs Maps for footer [LeafletJS](https://leafletjs.com/reference.html)

## Media

- [Freepik](https://www.freepik.com) for images used within the site
- [Pexels](https://www.pexels.com/) for images used within the site
- [Chat GPT](https://www.chat.openai.com) was used to produce the content text.

## Acknowledgements

- A huge thanks to my family for their continued support during this project after many long nights and late evenings working towards the Diploma and the many cups of coffee sent my way. 
- Much gratitude is extended to mentor's Amy and Lewis for their expert guidance and advice during this Diploma, which gave me the confidence to make the most out of every project.
- I would like to pass on a special thank you to Tutor Support - especially three individuals, Rebecca , Roman and Oisin who were a huge help towards the final stages of this journey when tiredness crept in and I encountered a very specific issue with duplicate payments on Stripe. They all helped me only days before the end, to resolve this issue, with an eagle eye level of accuracy by Oisin at that 6.30pm clsoing time. So my graditute to them, under stressful circumstances cannot be thankful enough! Tutor Support are a serious level of help when you're in the depths of it.
- Thank you to my fellow students and Code Institute alumni for their guidance and support.
- From the time I began this course 12 months ago to this point in time , I can say that I feel that I have learned more from this course than I have done with any other previous third level course in Software Development.