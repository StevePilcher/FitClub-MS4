# Testing

The testing of the FitClub site was conducted manually. This tesing document references the [User Stories](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/FitClub_User_Stories.pdf) file and unique ID. The unique story ID will be referenced when a specific user story is tested/verified. 

The testing is broken down firstly, seperated to different user types, then per app and finally page if the app has multiple pages/actions to test on that page. Comments on screen size testing will be made to show validation for smaller form factors. 

Testing steps are not repeated under both user types where te user stories are not unique to a user type (IDs 2-8). These are documented only under the anonymous user section. 

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

### Products App

**User Story 2, 3 both AU & RU**

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

**User Story 4, 5 both AU & RU**

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

**User Story 6, 7 both AU & RU**

1. Bag Page:
    1. AU/RU clicks on bag on icon on the nav bar
    2. AU/RU redirects to bag page
        - Displays
        -

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





## Owner/Admin (OA)



In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.





## Known bugs

