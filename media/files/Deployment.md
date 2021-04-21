# Deployment 

This document details the steps and neccessary actions required to deploy a copy of this code locally and on your own production server. Firstly deploying the code. 

## Deployed Version

The following sites are required to be able to successfully host a working copy of this project. You will need active verified accounts.

Before continuing, link to each of these platforms and signup, then verify for a free account.

- [Heroku](https://www.heroku.com/) 
    - for hosting server and PostGres DB 
- [Amazon Web Services](https://aws.amazon.com/) 
    - for static and Media file hosting
- [Stripe Payments](https://stripe.com) 
    - for the payments system
- [GitHub](https://github.com/)
    - for repository hosting and git.
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    - To generate a django secret key, item **6** in the config vars table
- [Gmail](https://accounts.google.com)
    - Gmail Accounts for sending emails


This table details the key value pairs that are required in Heroku config vars. You will retrieve these from the above sites. Each pair and it's associated value location will be detailed in the step by step guide.

| ID | Key  | Value  |
|---|---|---|
| 1 | AWS_ACCESS_KEY_ID | <*from your user CSV file created on AWS*> |
| 2 | AWS_SECRET_ACCESS_KEY | <*from your user CSV file created on AWS*> |
| 3 | DATABASE_URL | <*Step 2 - Heroku DB URL automatically populated*> |
| 4 | EMAIL_HOST_PASS | <*step 5 - Gmail, 6*> |
| 5 | EMAIL_HOST_USER | <*youremail@gmail.com*> |
| 6 | SECRET_KEY | <*Generated using Django Secret Key Generator*> |
| 7 | STRIPE_PUBLIC_KEY | <*Step 4 - Stripe, 4*>  |
| 8 | STRIPE_SECRET_KEY | <*Step 4 - Stripe, 4*> |
| 9 | STRIPE_WH_KEY | <*Step 4 - Stripe, 2.5*> |
| 10 | USE_AWS | <*True*> |


### Step 1 - GitHub

Next, you can clone a copy of this code through GitHub.

The deployed version is off of the master branch from this project on GitHub [here](https://github.com/StevePilcher/FitClub-MS4)

#### Cloning this Project

To clone this project, follow these steps;

1. Follow the [link](https://github.com/StevePilcher/FitClub-MS4)
2. Click the **'Use this template'** button
3. User will be redirected to a create repository from template page
4. Fill in the name of the repository you want to create
5. Choose public or private
6. Click the green **Create repository from template** button


### Step 2 - Heroku

#### Deploying to Heroku

To deploy the project on Heroku yourself, follow these steps; 

1. Login to your [Heroku](https://id.heroku.com/login) account
2. Click the button **New** , with further dropdown **create new app**
3. Create the app with a unique name and selecting the region closest to you, Europe or USA, click the **Create App** button
4. CLick the **Resources** tab
5. In the add-ons search box, search for **Heroku Postgres** and click
6. Select **Hobby Dev - Free** and click provision
    - This attaches the Postgres DB to your project and populates the config var for DATABASE_URL automatically
7. Click the **Deploy** tab
8. The Deployment Method is recommended to be connected to GitHub. In the deployment method, click the GitHub logo
9. Sign in and search for your cloned project/branch
10. Once complete, scroll down and enable automatic deploys, this will keep the deployed version updated with every commit to the selected branch in Github.  
11. Your site will now deploy but will still need further steps to fully implement it fully.


Now your app has been created you will need to edit the ALLOWED_HOSTS variable in the settings.py file for you cloned project on line *30*; 

1. Replace ALLOWED_HOSTS = ['spilcher-fitclub-ms4.herokuapp.com', 'localhost']
    - with ALLOWED_HOSTS = ['*your-project-name*.herokuapp.com', 'localhost']

To edit your Heroku config vars follow these steps; 

1. Click the **Settings** tab
2. Scroll down and click **Reveal Config Vars** 
3. This settings menu allows you to set your secret keys and other sensitive info so it's hidden from public view
4. Config Vars should be entered as per the table at the top of this document.  

*You will need to return to these config values and edit whilst following the further steps below*

### Step 3 - AWS

To step an AWS S3 bucket, follow the steps below.

1. Login to your AWS account
2. Under the **My Account** click **AWS Management Console**
3. In the search bar, search S3 and click
4. You'll redirect to the buckets management page, click **Create Bucket**
5. When naming your new bucket it is recommended to name it the same as your Heroku app name. 
6. Select the region closest to you
7. Make sure **Block all public access** is unchecked
8. Acknowledge the bucket will be public
9. Click **Create Bucket**
10. You are now redirected back to the buckets list

Edit settings on your New Bucket

1. Click your created bucket from the list
2. On the **Properties** tab
3. Click **Static Web Hosting Edit** and check *Use this bucket to host a website*
4. Fill in the index and error values with the default placeholders and click **save**
5. On the **Permissions** tab
6. Scroll to the **Cross-origin resource sharing (CORS)** and click *edit*
7. Open [this](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/AWS_CORS_Config.txt) CORS file and paste in and save changes
8. Next on the Permissions tab, click on *edit* on **Bucket Policy**
9. Select **Policy Generator** and a new Amazon tab will pop out
10. Create a policy as follows;
    - Step 1 
        - S3 Bucket Policy
    - Step 2
        - Effect = allows
        - Principal = *
        - AWS Servive = Amazon S3
        - Actions = GetObject
        - ARN = *ARN Number (Located on permissions tab)*
11. Click **Add Statement**, then **Generate Policy**
12. Copy the Policy generated in the modal and paste back in the **Bucket Policy** on the **Add Permissions** tab
13. Edit the policy to allow access to all files by; 
    - add a '/*' to the end of ARN
14. Save the Policy
15. Click on the **Edit access control list (ACL)** 
    - check the box Everyone(pulic access) list/Objects

We now need to create a group/user to access this bucket/policy; 

1. Go back to the services
2. Under the **My Account** click **AWS Management Console**
3. In the search bar, search IAM and select 

Create a User Group
1. Select **User Groups** from left menu 
2. Click **Create Group**
3. Name the new group that makes sense to your project name
4. Click **Create Group**

Create Policy for Group
1. Select **Policies** from left menu
2. Click **Create Policy**
3. Select **JSON** tab 
4. Select **Import managed policy**
5. Search for 'S3'
    - select 'AmazonS3FullAccess' policy
    - Import
6. To only allow full access to your new bucket
    - Copy the ARN from the permissions tab of your S3 bucket
    - Edit the resources with your ARN to match [this](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/S3_Policy_Example.txt)
    - Click **Review Policy**
    - Name it and give it a description
    - Click **Create Policy**

Now assign the policy to the group; 

1. Select **Users Groups** from left menu
2. Select the group you just created
3. Click **Attach Policy**
    - Search the policy you just created
    - Select it 
    - Click **Attached policy**

Create a User to assign to the Group; 
1. Select **Users** from left menu
2. Click **Create User**
    - name the user
    - check programmatic access
3. Click **Next**
4. Check the group you just created
5. Click through the remaining tabs to **Create User**
6. Download and save this .CVS file. It's **Very Important**
    - This CSV file contains config vars for Heroku, enter them in the config vars as follows;
    - AWS_ACCESS_KEY_ID = Access key ID from csv file
    - AWS_SECRET_ACCESS_KEY = Secret access key form csv file

### Step 4 - Stripe 

Follow these steps to find your Stripe keys required for Heroku Config Vars

1. Loging to your Stripe account
2. Once signed in you'll arrive at your Stripe dashboard
3. Look on the lefthand dashboard menu for **developers/API keys**
4. Here you will find 2 stripe keys, Items 7 & 8 for heroku config vars.
    - Publishable Key = STRIPE_PUBLIC_KEY
    - Secret Key = STRIPE_SECRET_KEY
5. Copy and paste these in to Heroku config vars.

Create a webhook address and get the webhook variable; 

1. Under the same menu, click **Webhook** link
2. Click **Add Endpoint**
3. The address will be;
    - https:/*your-heroku-app-name.herokuapp.com*/checkout/wh/
    - **Add**
4. Under the 'Signing Secret' reveal key 
    - STRIPE_WH_KEY = Signing Secret Key
5. Enter the signing secret key in to Heroku config vars


### Step 5 - Gmail

Follow these steps to setup a gmail account to automate with this project

1. Login in to your created Gmail account
2. Go to the **account** settings in the top right corner, cog icon
3. Click **Accounts and Import**
    - Other google account settings
    - Go to the securty tab on the left hand menu
    - Click **2 Step Verification**
    - Click **Get Started**
    - Select the Verification method, your preference
    - Complete the 2 Step Verification
4. Now back to the Security tab
    - App passwords will now have appeared as an option
    - Click and verify passwords
5. On the App password screen; 
    - Select App = Mail
    - Device Type = Custom, name it Django
    - Click **Accept** 
6. A popup will give you another key; 
    - EMAIL_HOST_PASS = Popup password

Lastly your last heroku config var will be your created gmail account. 

1. EMAIL_HOST_USER = *youremail@gmail.com*
    

## Local development

The project branch **Local** was split form the master for a locally run development version. This version will need to follow the 3 steps below. 

To run a local copy of this code you will need 3 stripe keys. This will need to be entered in to your IDE. Refer to the your IDE softwares docmentation to see where to enter these values. 


#### ID Config Vars
| ID | Key  | Value  |
|---|---|---|
| 6 | SECRET_KEY | <*Generated using Django Secret Key Generator*> |
| 7 | STRIPE_PUBLIC_KEY | <*Step 2 - Stripe, 4*>  |
| 8 | STRIPE_SECRET_KEY | <*Step 2 - Stripe, 4*> |
| 9 | STRIPE_WH_KEY | <*Step 2 - Stripe, 2.5*> |


### Step 1 - GitHub

Next, you can clone a copy of this code through GitHub.

The development version is off of the local branch from this project on GitHub [here](https://github.com/StevePilcher/FitClub-MS4)

#### Cloning this Project

To clone this project, follow these steps;

1. Follow the [link](https://github.com/StevePilcher/FitClub-MS4)
2. Click the **'Use this template'** button
3. User will be redirected to a create repository from template page
4. Fill in the name of the repository you want to create
5. Choose public or private
6. Click the green **Create repository from template** button


### Step 2 - Stripe 

The 3 Config vars that are required to make the project locally are from Stripe. Follow these steps to find your config vars from Stripe.

Follow these steps to find your Stripe keys required for IDE Config Vars.

1. Loging to your Stripe account
2. Once signed in you'll arrive at your Stripe dashboard
3. Look on the lefthand dashboard menu for **developers/API keys**
4. Here you will find 2 stripe keys, Items 7 & 8 for heroku config vars.
    - Publishable Key = STRIPE_PUBLIC_KEY
    - Secret Key = STRIPE_SECRET_KEY
5. Copy and paste these in to Heroku config vars.

Create a webhook address and get the webhook variable; 

1. Under the same menu, click **Webhook** link
2. Click **Add Endpoint**
3. The address will be;
    - https:/*your-heroku-app-name.herokuapp.com*/checkout/wh/
    - **Add**
4. Under the 'Signing Secret' reveal key 
    - STRIPE_WH_KEY = Signing Secret Key
5. Enter the signing secret key in to Heroku config vars

### Step 3 

Now your app has been created you will need to edit the SECRET_KEY variable in the settings.py file for a generatored Django secret key, you can use the site listed at the top of this document; 

1. Replace SECRET_KEY = ''
    - with SECRET_KEY = '*your generated django secret key*'
