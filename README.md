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
    - [Sprints](#sprints)
  - [Marketing](#marketing)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - Home View \& User Account](#epic---home-view--user-account)
    - [Epic - Products](#epic---products)
    - [Epic - Basket Management \& Purchasing](#epic---basket-management--purchasing)
    - [Epic - Wishlist](#epic---wishlist)
    - [Epic - Newsletter](#epic---newsletter)
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
  - [Future Features](#future-features)
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

