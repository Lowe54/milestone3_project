# Milestone Project 3 for Fullstack Web Developer Course


 
## UX
 


### User stories



## Features

### Existing Features


### Features Left to Implement

-   Schema Validation of Allergins field
    -   This was initially included, however due to time constraints and fustration I removed it in order to get the application as a whole working, otherwise each time a record was added or updated, it threw a 'Document failed Validation' error.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [HTML5](https://www.w3.org/standards/webdesign/htmlcss)
    - **HTML5** is the basic building language of all websites, it allows for structure 
- [CSS3](https://www.w3.org/standards/webdesign/htmlcss#whatcss)
    - **CSS 3** is used to describe web pages, via color, font and other styling. In the project it is used for styling the elements on the page.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [FontAwesome](https://fontawesome.com/)
    - The project uses the free version of **FontAwesome** in order to add extra icons to the site
- [SASS](http://sass-lang.com/) 
    - **SASS** was used to add extra functionality to CSS, it allows for nested statements to be used, which in turn made the files easier to read.
- [JQuery TE](http://jqueryte.com/)
    - A lightweight jquery text editor used to enable WYSIWYG (What you see is what you get) functionality on the recipie form

## Testing

### Code Validation

The table below shows the various validators used and there results

| Language being tested  	| Validator Used                       	| Result 	| Notes                                                                                   	|
|------------------------	|--------------------------------------	|--------	|-----------------------------------------------------------------------------------------	|
| HTML                   	| https://validator.w3.org/            	| PASS   	| https://validator.w3.org/nu/?doc=https%3A%2F%2Flowe54.github.io%2Fmilestone2_project%2F 	|
| CSS                    	| https://jigsaw.w3.org/css-validator/ 	| PASS   	| |

### Automated Testing


### Manual Testing


### How it Displays

## Deployment

The site is available to view via [here](https://lowe541-milestone3-project.herokuapp.com/)

There are multiple steps to deployment, which are detailed below

### MongoDB
[SecurityTab]: readme_images/mongodb/Security.png
[NewUserLoc]:  readme_images/mongodb/Security_Add_New_User.png
[IPWhitelist]: readme_images/mongodb/IP_Whitelist.png
[IPPopup]: readme_images/mongodb/IP_Popup.png
***
The site utilises MongoDB, a document store based database management system.

In order to set it up so that it can be used by the web application, follow the steps below

**NOTE**: The steps below assume that you have already created an account on MongoDB Atlas and know how to set up a Project and Cluster.
If you do not, please follow the steps outlines in [https://docs.atlas.mongodb.com/getting-started/](https://docs.atlas.mongodb.com/getting-started/)

1) Click on the 'security' tab

![SecurityTab]

2) In the 'MongoDB Users' section, click on 'Add User'

![NewUserLoc]

3) In the popup that appears, enter a username and password for the new user, leave the permissions as 'Read and Write to any database'

4) Next click on the 'IP Whitelist' option and then click on the 'Add IP address'

![IPWhitelist]

5) In the popup that appears, click on 'allow access from anywhere' button, otherwise the database will only be accessible from certain IP addresses, then click on 'confirm'

![IPPopup]

The collections are now ready to be created.

#### Creating the collections
[connectionButton]: readme_images/mongodb/connectButton.png
[connectionoption]: readme_images/mongodb/Connect_Option.png
[terminalCopy]: readme_images/mongodb/terminal.png
Create a connection to the mongo shell, this is done by clicking on the connect button, then clicking on the 'Connect with the Mongo Shell'

![connectionButton]

![connectionoption]

Follow the instructions given if you do not have the shell installed, otherwise, click on the copy button next to the terminal command, and then paste it into a terminal program of your choice

![terminalCopy]

Once you have entered the password for the user set up in step 3, copy and paste the text held in [mongodb_create_recipies_collection.txt](readme_files/mongodb_create_recipies_collection.txt)

### Github
*** 
#### Github Deployment
- In a terminal, the git repository was initiated via the `git init` command
- The repository was linked to a .git file on github via
    - `git remote add origin https://github.com/Lowe54/milestone3_project.git`
    - `git push -u origin master`
    
- After each change, the following commands were used to push the changes to the git repository
    - `git add *` - This adds all changed files to staging
    - `git commit -m "MESSAGE HERE"` - Commits the work with a brief message as to what has changed
    - `git push` - This pushes the work to the git repository, after entering your github username and password


#### Github Cloning
- In order to clone the github repository, type the following command in a terminal
    - `git clone https://github.com/Lowe54/milestone3_project`
- If you wish to change the default directory to where the project is checked out to, use the following command 
    - `git clone https://github.com/Lowe54/milestone3_project *FolderName*`


#### Extra Steps

This project in windows runs on a virtual environment, in order to generate this, different commands need to be used depending on the version of python running on your operating system. The flask documentation gives detailed steps on this, and can be found at [http://flask.pocoo.org/docs/1.0/installation/#virtual-environments](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments)


Once your virtual environment has been activated, enter `pip install -r requirements.txt`, this will then install all requirements needed, then enter `flask run`, this will start the development server.

**Note** : If the requirements.txt file needs to be re-generated, enter `pip freeze --local > requirements.txt`


### Heroku Deployment
[AppOverview]: readme_images/heroku/app_overview.png
[AppCreate]: readme_images/heroku/app_create.png
[AppAutoDeploy]: readme_images/heroku/app_automatic_deploy.png
[AppManualDeploy]: readme_images/heroku/app-manual-deployment.png
[AppSettingsLink]: readme_images/heroku/app_Settings_link.png
[AppConfigVars]: readme_images/heroku/app_config_var_button.png
***
1) If you already have an heroku account, please go to step 4 after signing in
2) Go to [https://signup.heroku.com/](https://signup.heroku.com/)
3) Fill out the registration form
4) Once on the app overview (See below), click on 'New -> Create new app'
![AppOverview]
5) Enter an app-name and choose the region, then click on 'Create App'
![AppCreate]
6) Now choose the deployment method, there are 3 options
    a) Heroku CLI (Command Line Interface)
    b) GitHub Deployment
    c) Container Registry (Docker)

For option 'a', follow the instructions given, for 'b', you will be asked to link to a github account and for 'c', again follow the instructions given.

For this project, I went with the github deployment for simplicity, as it only meant one push per deployment.

Once linked, You can enable automatic deploys based off a branch
![AppAutoDeploy]
Or perform a manual deployment
![AppManualDeploy]


In order for the app to run however, certain environment variables need to be set.

From the application overview page, click on 'Settings'

![AppSettingsLink]

Then click on 'Reveal Config Vars'

![AppConfigVars]

You need to add the following 4 variables:
-   IP -> This is the IP, set it to 0.0.0.0
-   PORT -> Can be any value you want, I set it to 5000
-   SECRET_KEY -> Random string
-   PASSWORD -> Your MongoDB password for the user set up, not your password to login to Mongo Atlas

### Style Changing
***

The styles of this site are in SASS (.scss) format, in order to change the styles you will need to enter the following command into a terminal.

If you get an `command not recognised` error, please follow the steps [here](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#using_sass)

` sass --watch static/sass/:static/css`

## Credits

### Content

[https://allergytraining.food.gov.uk/english/rules-and-legislation/](https://allergytraining.food.gov.uk/english/rules-and-legislation/) for providing the 14 allergin options present in the application

### Acknowledgements

