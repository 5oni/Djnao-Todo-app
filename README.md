# Django-Todo
A simple todo app built with django  Topics bootstrap django django-framework html-css django-project

![Screenshot (148)](https://user-images.githubusercontent.com/75757260/110046362-e1eb4200-7d71-11eb-9f77-ab8a35ee12cc.png)


Setup
To get this repository, run the following command inside your git enabled terminal


`$ git@github.com:5oni/Django-Todo.git`

You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

`$ python manage.py makemigrations`

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command

`$ python manage.py migrate`

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

`$ python manage.py createsuperuser`

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

`$ python manage.py runserver`

Once the server is hosted, head over to http://127.0.0.1:8000/ for the App.


