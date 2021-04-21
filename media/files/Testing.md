# Testing

The testing of the FitClub site was conducted manually. This tesing document references the [User Stories](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/FitClub_User_Stories.pdf) file and unique ID. The unique story ID will be referenced when a specific user story is tested/verified. 

The testing is broken down firstly, seperated to different user types, then per app and finally page if the app has multiple pages/actions to test on that page. Comments on screen size testing will be made to show validation for smaller form factors. 

Testing steps are not repeated under both user types where the user stories are not unique to a user type (IDs 2-8). These are documented only under the anonymous user section. 

The following browsers were tested and devices simulated using the Mozilla Firefox dev tools; 

## Web browsers

- Mozilla FireFox version 87.0 (64-bit)
- Google Chrome version 89.0.4389.128 (Official Build) (64-bit)
- Microsoft Edge Version 90.0.818.42 (Official build) (64-bit)

## Devices

- Samsung Galaxy S9/S9+ Android 7.0
- iPhone 6/7/8 iOS11 
- iPhone 6/7/8 Plus iOS11
- iPhone X/XS iOS12
- iPad
- Kindle Fire HDX Linux

The followng user scenarios were tested :

## Anonymous User (AU)

### Home App

**User Story 1**

1. Landing Page:
    1. Got to home page
    2. Layout displays correctly centred on desktop
        - Layout displays correctly centred on tablet
        - Layout displays correctly centred on mobile
    3. Nav bar layout displays correctly as per Boostrap
        - Nav Bar reduces to burger icon and toggles correctly on tablet
        - Nav Bar reduces to burger icon and toggles correctly on mobile
    4. AU has active links to Products, Signup, Account and Bag only
        - All links test and work to redirect to correct page on all device sizes
    5. Content fades in on all screen sizes
    6. Push 'Play Video' button and model pops up with sales video centred, plays as expected
        - Model pops up centred on tablet and plays as expected
        - Model pops up centred on mobile and plays as expected
    7. Scroll down page, sections fade in/out as expected on all devices
    8. Footer displays correctly on all device sizes

2. Nav Bar:
    1. Nav bar remains active and links between pages correctly across all pages of the site
        - Tested on desktop
        - Tested on tablets 
        - Tested on mobile devices

3. Manual URL attempts:
    1. Maunally entering URLs to attempt to navigate the user to site content for RU
    2. Django @login_required decorator works to redirect users to login/signup page

### Products App

**User Story 2, 3, both AU & RU**

1. All Products:
    1. AU/RU clicks the products link
    2. AU/RU redirects to all products view
        - View displays all products on desktop devices in rows of 4
        - View displays all products on tablets in rows of 2
        - View displays all products on mobile devices in single rows 
    3. Clicking the individual products redirects to product details view on all screen sizes correctly
    4. AU/RU clicks the filter button for dropdown options
        - AU/RU clicks either option 'Hi/Lo, Lo/Hi'
        - Products refresh and filter to the selected filter

*Further development intended to improve filtering and add a search function*

**User Story 4, 5, both AU & RU**

2. Product details:
    1. AU/RU clicks the individual product from the all products view
    2. AU/RU redirects to individual products page
        - View displays all content centred on desktop devices
        - View displays all content centred on tablets
        - View displays all content centred on mobile devices 
    3. AU/RU click 'Keep Shopping' button
        - AU/RU redirects back to all products view
    4. AU/RU click 'Add to Bag'
        - Bag icon shakes and changes to active yellow colour
        - Bag total also updates with items total
        - Toast message pops up correctly
    5. If item has reviews
        - Reviews display correctly on;
            - Tablets
            - Mobile devices
    6. If RU has bought product already
        - Checks if RU has left a review
        - If RU has not reviewed, allows review form to be viewed, displays correctly on;
            - Tablets
            - Mobile devices
        - If RU has already left a review the form will not display a 2nd time


### Bag App

**User Story 6, both AU & RU**

1. Bag Page:
    1. AU/RU clicks on bag on icon on the nav bar
    2. AU/RU redirects to bag page and bag is in table format
        - Displays centred on tablet
        - Displays centred on mobile devices
    3. AU/RU clicks 'trash can' icon
        - Item is removed
        - page refreshes
        - toast message displays correctly
    4. AU/RU clicks 'Continue Shopping' button
        - Redirects back to all products view
    5. AU/RU clicks 'Secure Checkout'
        - Redirects to Checkout app

## Checkout App

**User Story 7, 8, AU & RU** 

1. Checkout / Checkout Success Page:
    1. AU/RU clicks on the 'Secure Checkout' from the bag app
    2. AU/RU redirects to checkout page
        - Displays details form / bag with correct bag items/amounts, side by side correctly on desktop
        - Displays details form / bag with correct bag items/amounts, side by side correctly on tablet
        - Displays details form / bag with correct bag items/amounts, centred on mobile devices
    3. Stripe Payment Intent webhook created Successfully
    4. AU/RU attempts to submit invalid form
        - Form error flashes
        - Required form fields highlight red
    5. AU/RU sumbits a valid form
        - submit button becomes inactive 
        - Stripe payment intent succeeded webhook
        - Stripe payment success webhook
    6. On payemnt success, AU/RU redirects to checkout success page
        - Displays unique order number, message, address and order items summary centred correctly on desktop
        - Displays unique order number, message, address and order items summary centred correctly on tablet
        - Displays unique order number, message, address and order items summary centred correctly on mobile devices
    7. Success page 'Forum button' links correctly
        - AU redirect to a login/signup page
        - RU that are logged in redirect to forums page


## Registered User (RU)

### Home App

**User Story 15**

1. Landing Page:
    1. Got to home page
    2. Dashboard Layout displays correctly centred on desktop
        - Layout displays correctly centred on tablet
        - Layout displays correctly centred on mobile
    3. Nav bar layout displays correctly as per Boostrap
        - Nav Bar reduces to burger icon and toggles correctly on tablet
        - Nav Bar reduces to burger icon and toggles correctly on mobile
    4. RU has active links to Products, Forum, Account and Bag only
        - All links test and work to redirect to correct page on all device sizes

*Further development planned to add more content to this dashboard*


### Profile App

**User Story 9, 10, 11** 

1. My Profile page:
    1. RU clicks the link to the 'My Account' icon, followed by dropdown link 'My Profile'
    2. RU redirects to My Profile page
        - Displays centred with address details and order history side by side on desktop 
        - Displays centred with address details and order history centred on tablets
        - Displays centred with address details and order history centred on mobiles
    3. RU sees prepopulated forms with address
    4. RU changes details in any/all form fields and submits
        - Page refreshes
        - Toast message displays correctly
        - Form is now repopulated with updated data

    *User profile images are currently disabled for production. Bug fixes are required now the media hosting has deployed to AWS S3. The Local development version has the ability to update user profile images* 

    5. RU clicks linked order numbers from history
        - RU redirects to a the same checkout success page
        - Order displays 
        - Toast message displays correctly
        - Nav button under order correctly displays 'Return to My Profile'
        - Button links correctly back to My Profile page


### Forum App

**User Story 12, 13, & 14**

1. Forum Page
    1. RU clicks the link to the forums page
    2. RU redirects to forum page
        - Page displays on desktop centred correctly
        - Page displays on tabelts centred correctly
        - Page displays on mobile devices correctly
    3. RU click link to Parent forum, Training or Eating Plans
    4. RU is directed to requested link

2. Topics Page
    1. RU is redirected from the parent forums link
    2. Topics are listed in creation date order
        - Table is populated and displays centred on desktop
        - Table is populated and displays centres on tablet
        - Table is populated and displays centred on mobile
    3. Create New Topic button is displayed underneath correctly
        - RU clicks 'Create New Topic' link
        - Link redirects to Create new topic form page
        - Page displays correctly, breadcrumb nav populates with the correct link
        - 

## Owner/Admin (OA)


## Known Issues/Bugs

1. Checkout display on mobile needs UX improvement
2. Footer My profile page on Kindle Fire HDX linux pushes from the bottom of the page
3. Payment_intent_Succeeded Webhook is failing, it was working pre-deployment. Time contraints have limited troubleshooting. 
4. Device views for Forum pages needs more UX improvement, just reducing the overal size isn't very user friendly
