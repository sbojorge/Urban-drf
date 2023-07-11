# Urban-drf
## Project goal

This Back-End API will be used to store and CRUD functionality of my content sharing platform "Urbantrips".

------

## Technologies used

The API was built using Django and the Django Rest Framework.

Below you can find the complete list of the libraries used for the development of this project:

* Django
* Django-cloudinary-storage: This Django package was used to provide Cloudinary storage for media (images and videos).
* Django-countries: Used for providing a country field in the Profile model.
* Django Rest Framework: For building the WEB API.
* Django-TinyMCE: Used for adding a widget to render the TextField fields as a TinyMCE editor.
* Gunicorn: Used to run Django on Heroku.
* dj_database_url: A Django utility for using the DATABASE_URL environment variable.
* Pillow: This Python library was used for image processing.
* Python-magic: This Python interface was used for uploaded video validation.
* Psycopg2: Used for connecting Python with PostgreSQL.

------

## Database structure

The entity relationship diagram was built using Lucidchart (when finished export the ERD and paste it here).

------

## Project management

The project was developed using the Kanban Agile management methodology and the MoSCoW prioritisation technique.

It was put in place using different functionalities in GitHub: 
* Issues, for EPICS and user stories;

An epic covers the development of an existing feature in the API.

User stories were linked to the epic to keep track of the progress with the tasks.

In order to better organise the flow of the work to do, I also created an epic for the set up and final deployment of the project.

* Milestone (without due date), for the product backlog;

Ready-for-development epics were stored in the product backlog before starting a sprint.

* Milestone (WITH due date), for each iteration;

I worked 1 epic x sprint.
User stories that couldn't be completed were placed back in the product backlog and on "No status" category of the project for eventually being included in a next sprint.

* Project, for the Kanban board.

Epics were assigned to the "To-do" status and move to "In progress" or "Done" status as the tasks in the user stories were completed.

![Agile](/static/images/agile/picture_1.png)

### Epics and user stories

![Epic_1](/static/images/agile/picture_2.png)

![Epic_2](/static/images/agile/picture_3.png)

![Epic_3](/static/images/agile/picture_4.png)


## Deployment
The application was early deployed following these steps:

* Create an external database on ElephantSQL
* In the IDE, prepare environment:
    
    In env.py:
 
    -   create file and add it to .gitignore
    -   add the environment variables: secret key, cloudinary url, dev and database url
    
    In settings.py:

    -   update the secret key section
    -   connect the external database to the workspace by updating the database section and running migrations
    -   configure Django to use Cloudinary (add Cloudinary to the 'Installed apps' and setup the default storage, url and media)
    -   set the allowed host 
        
* Create an application on Heroku and prepare the configuration variables on it
    -   secret key
    -   database url
    -   cloudinary url
    -   disable collectstatic

* Create and prepare a procfile
* Connect the repository to the Heroku app and deploy branch

The application successfully deployed an empty project:

![deployed app](/static/images/deployment/picture_1.png)

------

## Credits
### Media
* Images for the default profile, default image post and default video post come from [Iconduck](https://iconduck.com/).

###  Documentation
* The explanation about the libraries used in this project comes from [PyPI](https://pypi.org/).

### Code
* The IsOwnerOrReadOnly class comes from [Custom Permissions Examples](https://www.django-rest-framework.org/api-guide/permissions/#api-reference).
* The video extension validation in the Post model was inspired on [Django Media Files](https://www.youtube.com/watch?v=UcUm82jWeKc)