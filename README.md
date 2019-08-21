# Milestone Project 3 for Fullstack Web Developer Course

This project is designed to be a online recipie store / cookbook that anyone can contribute to. It is intended for people who would enjoy sharing recipies, rating them based off how much they have enjoyed them.

It contains a text based search off each recipie title, and has a fully built pagination when more than 10 recipies are listed
 
## UX
 
I decided to keep a neutral colour scheme for the project, as it made the results etc.. look streamlined

In terms of the navigation of the site, instead of having multiple sidebars, all the neccessary links were added to one main navbar at the top, this allows access to the add a recipie page, results page via a search button, statistics page and a link back to the index page.

This gives the user access to all the main pages without having to scroll down the current page.


### Mockups

#### Home page
[Homepage]: readme_images/mockups/index_page.png
![Homepage]

#### Recipie Page
[Recipiepage]: readme_images/mockups/recipie_view.png

![Recipiepage]
#### Results Page
[ResultsPage]: readme_images/mockups/results_page.png

![ResultsPage]
#### Add / Edit Form
[Form]: readme_images/mockups/results_page.png

![Form]
#### Statistics page
[StatisticsPage]: readme_images/mockups/statistics_page.png

![StatisticsPage]
### Differences between mockups and live site

#### General

The search bar was moved to the right hand side of the navbar as a inline form, this was made since there was no sense in having a tiny one field form taking up 75% / 80% of the page. It also allowed it to be more easily displayed on mobile devices.

#### Homepage

I dropped the planned carousel / tab layout in favor of a series of cards showing the most liked recipies. The links in the sidebar were moved to the main navbar, in order to allow them to be shown on mobile view across all pages

#### Form page

Since there was no need for a sidebar, and all potential links were moved to the navbar (See the general section above for reasoning for this change). The form section instead went 100% width but was centralised on the page.

#### Results page

The country of origin field was not implemented, therefore I shifted the allergin information to where this information would have been displayed, and instead added a 'View more information' button in the bottom left of the result hit.

#### Recipie page

The planned sidebar was switched over to the right hand side of the page, with the like/dislike buttons being moved above the recipie actions button.

The ingredients / instructions / implements was changed to be a tab set below the description

#### Statistics page

The planned sidebar was removed since the main links appear in the navbar, instead the graph section appears across the whole page.

### User stories

| User story # | What am I looking for                                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1            | I am user who is looking for a place to share my family recipie                                                                                  |
| 2            | I am a user who is looking for a recipie, but am allergic to fish                                                                                |
| 3            | I am a food critic who likes to browse public cookbooks and rate the recipies listed                                                             |
| 4            | I am a member of the public who wants to find pasta recipies                                                                                     |
| 5            | I am a member of the public who is interested in finding certain recipie, but not those that contain eggs and mustard, as I am allergic to those |


## Features

### Existing Features
- Results filtering
    - The project includes a custom made allergin filter, which allows for multiple allergins to be excluded from the result set. This could be expanded on to include other fields, but due to time constraints this was ommited (See Features left to implement section)
- Custom pagination
    - The project includes a pagination which takes effect once more than 10 recipies are displayed.
- Flash messaging
    - A success/error message is displayed to the user when they add/update a recipie, in addition if they try to access a recipie that does not exist, an error message will be displayed.

### Features Left to Implement

-   Schema Validation of Allergins field
    -   This was initially included, however due to time constraints and fustration I removed it in order to get the application as a whole working, otherwise each time a record was added or updated, it threw a 'Document failed Validation' error.
-   More graphs on the statstics page
    - Considering the fact that a created date and updated date is stored within the database and written to the 'collection.json' file, there is ample scope to add a created per month graph.
-   More filters
    - There is room to add extra filters to the results, for example a list of pre-sent implements, which would replace the 'recipie_implements' field, as the filter would not be able to support free text in it's current state.
    - In addition, there is scope to add the 'type of meal' and 'difficulty' fields as filters.
-   Image storage
    - Since heroku has no native support for image upload/storage **

## Technologies Used

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
- [d3.js](https://d3js.org/) and [dc.js](https://dc-js.github.io/dc.js/docs/html/index.html)
    - Used to implement the graphs in the [statistics page](https://lowe541-milestone3-project.herokuapp.com/stats)

## Testing

### User story testing

| User story # | What am I looking for                                                                                                                            | How was this achieved?                                                                                  |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| 1            | I am user who is looking for a place to share my family recipie                                                                                  | By Clicking on the 'Add a new recipie' link in the navbar                                               |
| 2            | I am a user who is looking for a recipie, but am allergic to fish                                                                                | By clicking on 'Search', then selecting the 'fish' option in the allergin filter.                       |
| 3            | I am a food critic who likes to browse public cookbooks and rate the recipies listed                                                             | By clicking on 'Search', then viewing a recipie details, there is a like/dislike button in each recipie |
| 4            | I am a member of the public who wants to find pasta recipies                                                                                     | Enter 'Pasta' in the search bar, then click on 'search'                                                 |
| 5            | I am a member of the public who is interested in finding certain recipie, but not those that contain eggs and mustard, as I am allergic to those | By clicking on 'Search', then selecting the 'eggs' and 'mustard' options in the allergin filter.        |


### Code Validation

The table below shows the various validators used and there results

| Language being tested | Validator Used                       | Result          | Notes                                                                                                                                                              | Link to validation result                                                                                                                                                                                            |
|-----------------------|--------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTML                  | https://validator.w3.org/            | See table below | All main pages tested (See link table below)                                                                                                                       | See Table                                                                                                                                                                                                            |
| CSS                   | https://jigsaw.w3.org/css-validator/ | PASS            | Not all of main.css was tested, see [tested_css.txt](Tested CSS .txt) for the code that was tested. This is due to it incorperating part of bootstrap's grid files | Link to validator - https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flowe541-milestone3-project.herokuapp.com%2Fstatic%2Fcss%2Fmain.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en |
| Javascript            | https://jshint.com/                  | PASS            | See screenshot below for annotations etc..                                                                                                                         | See Screenshot                                                                                                                                                                                                       |
| Python                | http://pep8online.com                | PASS            | See Screenshot below                                                                                                                                               |                                                                                                                                                                                                                      |
#### HTML Validation Results

| Page Name    | Site Link                                                                                | Validation Result | Validation Link                                                                                                                   |
|--------------|------------------------------------------------------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Home         | https://lowe541-milestone3-project.herokuapp.com                                         | PASS              | https://validator.w3.org/nu/?doc=https%3A%2F%2Flowe541-milestone3-project.herokuapp.com                                           |
| Results      | https://lowe541-milestone3-project.herokuapp.com/results/?qt=                            | PASS              | https://validator.w3.org/nu/?doc=https%3A%2F%2Flowe541-milestone3-project.herokuapp.com%2Fresults%2F%3Fqt%3D                      |
| Recipie View | https://lowe541-milestone3-project.herokuapp.com/recipie?id=5d347f824a83d5055757582d     | PASS              | https://validator.w3.org/nu/?doc=https%3A%2F%2Flowe541-milestone3-project.herokuapp.com%2Frecipie%3Fid%3D5d0ea50beb1c1f61c1fea203 |
| Recipie form | https://lowe541-milestone3-project.herokuapp.com/form?id=5d347f824a83d5055757582d&edit=1 | PASS              | https://validator.w3.org/nu/?doc=https%3A%2F%2Flowe541-milestone3-project.herokuapp.com%2Fform                                    |
| Statistics   | https://lowe541-milestone3-project.herokuapp.com/stats                                   | PASS              | https://validator.w3.org/nu/?doc=https%3A%2F%2Flowe541-milestone3-project.herokuapp.com%2Fstats                                   |

#### JsLint Result
[JSLint_Results]: readme_images/testing/JSLINT_Results.png


![JSLint_Results]

#### Python PEP8 Check
[Python_Result]: readme_images/testing/PEP8_online_check.png
![Python_Result]
### Automated Testing

Automated testing is in place for the form submission page. It checks to see if the expected type is what the current type is. i.e is the recipie_title a string?

It updates the testresults.txt file each time a record is added or updated with the test results.

[Test Results txt file](/testresults.txt)

### Manual Testing

| Test Number | Test area                          | What is being tested                                                                                                    | What should happen                                                                             | What actually happened                                                                | Actions to take (If applicable) |
|-------------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------|
| 1           | Navigation                         | Clicking on the 'Add a recipie button'                                                                                  | User should be sent to the add a recipie page                                                  | User sent to add recipie form                                                         | N/A                             |
| 2           | Navigation                         | Clicking on the 'Statistics page' button in the navbar                                                                  | User should be sent to the statistics page                                                     | User sent to statistics page                                                          | N/A                             |
| 3           | Navigation                         | Clicking on the 'Search' button without entering a search term                                                          | User should be sent to the search page                                                         | User sent to search page                                                              | N/A                             |
| 4           | Navigation                         | From the results page, user clicks on the 'Home page' button in the navbar                                              | User should be sent to the home page                                                           | User sent to home page                                                                | N/A                             |
| 5           | Navigation - Home page specific    | Clicking on the 'View recipie' button for one of the most liked recipies                                                | User should be sent to the recipie page of the clicked button                                  | User sent to selected recipie                                                         | N/A                             |
| 6           | Navigation - Results page specific | Clicking on the 'View Full Information' button on a result hit                                                          | User should be sent to the recipie page of the clicked button                                  | User sent to selected recipie                                                         | N/A                             |
| 7           | Results                            | Enter 'Pasta' as a search term from the home page                                                                       | User sent to results page, Results should only show recipies with 'Pasta' as part of the title | Results only containing 'Pasta' shown                                                 | N/A                             |
| 8           | Results                            | Enter 'Fish' as a search term from the results page, with no previous search term being entered                         | Results page should refresh, only showing results for recipie titles containing 'Fish'         | Results only containing 'Fish' shown                                                  | N/A                             |
| 9           | Results                            | Enter 'Pasta' as a search term from the results page, with 'Fish' being the previous term searched for                  | Results page should refresh, only showing results for recipie titles containing 'Pasta'        | Results only containing 'Pasta' shown                                                 | N/A                             |
| 10          | Results - Filtering                | Filter 'Fish' from the results set by clicking on 'Fish', then filter my results                                        | No recipies that contain 'Fish' as an allergin should appear                                   | No recipies that list 'Fish' as an allergin are shown                                 | N/A                             |
| 11          | Results - Filtering                | Filter 'Fish' and 'Eggs' from the results set by clicking on the options in the allergin filter, then filter my results | No recipies that contain 'Fish' or 'Eggs' as an allergin should appear                         | No recipies that list 'Fish' or 'Eggs' as an allergin are shown                       | N/A                             |
| 12          | Recipie View - Add Like            | Clicking on the 'like' button within the recipie                                                                        | Like counter should increase by 1                                                              | Like counter increased by 1                                                           | N/A                             |
| 13          | Recipie View - Add Dislike         | Clicking on the 'dislike' button within the recipie                                                                     | Dislike counter should increase by 1                                                           | Dislike counter increased by 1                                                        | N/A                             |
| 14          | Recipie View                       | Clicking on 'Edit Recipie'                                                                                              | User should be taken to the edit recipie form, with the recipie details already filled out     | User taken to form with the details pre-populated                                     | N/A                             |
| 15          | Recipie View                       | Clicking on 'Delete Recipie'                                                                                            | Recipie should be deleted, user sent to index page with a confirmation message                 | Recipie deleted, user sent to index page with a 'Record successfully deleted' message | N/A                             |
| 16          | Add/Edit Form                      | Adding a new recipie                                                                                                    | User should be redirected to the results page with a confirmation message                      | User sent to results page with a  'Recipie added' image                               | N/A                             |
| 17          | Add/Edit Form                      | Editing a recipie                                                                                                       | User should be redirected to the results page with a confirmation message                      | User sent to results page with a  'Recipie updated' message                           | N/A                             |
| 18          | Statistics                         | Clicking on the 'Easy' column in the 2nd chart                                                                          | Both charts should filter to only show recipies listed as 'Easy'                               | Chart Filtered                                                                        | N/A                             |
| 19          | Statistics                         | Clicking on the 'reset' button                                                                                          | Both charts should be reset to default                                                         | Chart Reset                                                                           | N/A                             |

### How it Displays

#### Desktop

##### Home

##### Results

##### Recipie add/edit form

##### Recipie View

##### Statistics

#### Mobile

##### Home

##### Results

##### Recipie add/edit form

##### Recipie View

##### Statistics

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

The styles of this site are in SASS (.scss/.sass) format, in order to change the styles you will need to enter the following command into a terminal.

If you get an `command not recognised` error, please follow the steps [here](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#using_sass)

` sass --watch static/sass/:static/css`

## Credits

### Content

[https://allergytraining.food.gov.uk/english/rules-and-legislation/](https://allergytraining.food.gov.uk/english/rules-and-legislation/) for providing the 14 allergin options present in the application

[Easy Meatballs recipie - Betty Crocker](https://www.bettycrocker.com/recipes/easy-meatballs/2959910f-1b27-438a-9085-d40b1950db20) for the meatball image

[Fish and Chips - Wikipedia](https://en.wikipedia.org/wiki/Fish_and_chips) for the fish and chips image
### Acknowledgements

