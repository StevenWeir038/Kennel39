# Deployment

This project was a first attempt at deploying to *Heroku* and was done as early as possible to avoid undue stress closer to the submission deadline.

Full disclosure, it took a few iterations to get it working and was a little muddled.  A great deal was learned from the process.

It is assumed the user knows how to create a repository on Github.
The linked repo template from the [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template) was used to start the project.

To create a deployed a skeleton application on *Heroku* using Github/Gitpod IDE the folowing steps were observed:

1. Install Django 3.2 (LTS) with required packages
2. Create a new Django project
3. Set up project to use a relational database (PostgreSQL) and Cloudinary (for persistent file storage)
4. Deploy empty project to Heroku

## Install Django 3.2 (LTS) with required packages.

*Django*, a full stack framework will support this project.

To install, type *pip3 install Django==3.2* into the Gitpod terminal.

![01](docs/readme/local_deployment/01-django3.2-install.png "01")

Install gunicorn (web server) by typing *pip3 install gunicorn*.

![02](docs/readme/local_deployment/02-gunicorn-install.png "02")

Install the dj_database_url library for postgreSQL by typing *pip3 install dj_database_url*, then install the psycopg2 library for postgreSQL by typing *pip3 install psycopg2*.

![03](docs/readme/local_deployment/03-dj_database_url-install.png "03")

![04](docs/readme/local_deployment/04-psycopg2-install.png "04")

Install Cloudinary by typing *pip3 install dj3-cloudinary-storage*. 

![05](docs/readme/local_deployment/05-cloudinary-install.png "05")

Now create a requirements.txt file in the main directory. 

In the terminal, type *pip3 freeze --local > requirements.txt*.  This file tells Heroku what packages are needed to run the deployed application.  Follow this step each time a new package is installed in Gitpod.

![06](docs/readme/local_deployment/06-requirements-cli.png "06")

![07](docs/readme/local_deployment/07-requirements-directory.png "07")

## Create a new Django project.

To create a new *project* called *main* type the following to the terminal, `django-admin startproject main .`
This will create new folder called `main` and a `manage.py` file in the root directory. (First deployment I called main *django_kennel* or *kennel39*. Bottom line, create the new project first.

![08](docs/readme/local_deployment/08-create-django-project-cli.png "08")

![09](docs/readme/local_deployment/09-create-django-project-directory.png "09")

Now create an app called `home` within the project. Type *python3 manage.py startapp home* (NB. Project apps should be differentiated by functionality. This app will act as the homepage. First runtrhough I used *accounts* instead of home.

![10](docs/readme/local_deployment/10-create-app-accounts-cli.png "10")

![11](docs/readme/local_deployment/11-create-app-accounts-directory.png "11")

Open the `settings.py` file in the `main` **project** folder and add the newly created *home* app to the bottom of the Installed Apps list.  Remember to add a comma to the end even though it's the last list entry. First attempt I used *accounts*. Use *home* instead.

![12](docs/readme/local_deployment/12-add-app-to-settings.png "12")

In the terminal, type *python3 manage.py migrate* to update the database schema used by Django.  

![13](docs/readme/local_deployment/13-migrate-database.png "13")

In the terminal, type *python3 manage.py runserver* to verify local deployment.  A message to open a page in the browser pops up using *port 8000*.

If Gitpod has a glitch and doesn't provide this popup, copy the url in the browser then paste into a new tab.  Add *8000-*. immediately after *https://*.

![14](docs/readme/local_deployment/14-local-deploy-success.png "14")