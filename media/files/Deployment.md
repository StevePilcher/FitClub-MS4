# Deployment 

This document details the steps and neccessary actions required to deploy a copy of this code locally and on your own production server. Firstly deploying the code. 

## Deployed Version

The following sites are required to be able to successfully host a working copy of this project. You will need active verified accounts.

Before continuing, link to each of these platforms and signup, then verify for a free account.

[Heroku](https://www.heroku.com/) - for hosting server and PostGres DB 
[Amazon Web Services](https://aws.amazon.com/) for static and Media file hosting
[Stripe Payments](https://stripe.com) for the payments system
[GitHub](https://github.com/) for repository hosting and git.


This table details the key value pairs that are required in Heroku config vars. You will retrieve these from the above sites. Each pair and it's associated value location will be detailed in the step by step guide.

| ID | Key  | Value  |
|---|---|---|
| 1 | AWS_ACCESS_KEY_ID | <*from your AWS dashboard*> |
| 2 | AWS_SECRET_ACCESS_KEY | <**> |
| 3 | DATABASE_URL | <*Heroku DB URL*> |
| 4 | EMAIL_HOST_PASS | <**> |
| 5 | EMAIL_HOST_USER | <**> |
| 6 | SECRET_KEY | <**> |
| 7 | STRIPE_PUBLIC_KEY | <**>  |
| 8 | STRIPE_SECRET_KEY | <**> |
| 9 | STRIPE_WH_KEY | <**> |
| 10 | USE_AWS | <*True*> |


### Step 1 - GitHub

Next, you can clone a copy of this code through GitHub.

The deployed version is off of the master branch from this project on GitHub [here](https://github.com/StevePilcher/FitClub-MS4)

#### Cloning this Project

1. Follow the [link](https://github.com/StevePilcher/FitClub-MS4)
2. Click the **'Use this template'** button
3. User will be redirected to a create repository from template page
4. Fill in the name of the repository you want to create
5. Choose public or private
6. Click the green **Create repository from template** button


### Step 2 - Stripe 

1. Follow the [link](https://stripe.com) to Stripe
2. Once signed in you'll arrive at your Stripe dashboard
3. 








In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

