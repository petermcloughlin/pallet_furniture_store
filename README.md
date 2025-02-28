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
    - [Elephant SQL](#elephant-sql)
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
| All Products  | Visible - items can be viewed and added to Bag, Wishlist function not available | Visible and full feature interaction available |
| Service Review   | Not Visible | Visible and full feature interaction available |
| Read   | Visible | Visible |
| Subcribe to Us (MailChimp) | Visible | Visible |
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
Pallet Furniture Store's footer is brightly coloured with the default forest green colour to contrast against the site's important white space. Mail Chimp's newsletter subscription form for users to sign up for weekly emails lies at the centre below the interactive location map. Across from this are a list of links that aim to give the customer all of the information they would need about Pallet Furniture Store.

 A Facebook page for Pallet Furniture Store opens in a new tab using the facebook icon link, as does a Twitter page, Instagram, YouTube, Pintrest and LinkedIn.

At the bottom left are the Open Hours for the business and to the right of the map is the location address and contact details.

<details open>
    <summary>Footer - All Users</summary>  
    <img src="documentation/home_page/footer.PNG">  
</details>

