# Urban-drf

## Project goal

This Back-End API will be used to storing and handling CRUD functionality of the content sharing platform [Urbantrip](https://github.com/sbojorge/urbantrip).

---

## Project management

The project was developed using the Kanban Agile management methodology and the MoSCoW prioritisation technique.

It was put in place using different functionalities in GitHub:

- Issues, for EPICS and user stories;

An epic covers the development of an existing feature in the API.

User stories were linked to the epic to keep track of the progress with the tasks.

In order to better organise the flow of the work to do, I also created an epic for the set up and final deployment of the project.

- Milestone (without due date), for the product backlog;

Ready-for-development epics were stored in the product backlog before starting a sprint.

- Milestone (WITH due date), for each iteration;

I worked 1 epic x sprint.
User stories that couldn't be completed were placed back in the product backlog and on "No status" category of the project for eventually being included in a next sprint.

- Project, for the Kanban board.<br> You can access the project [here](https://github.com/users/sbojorge/projects/12).
This project holds epics of 2 repositories: Urban-drf (the backend repo) and Urbantrip (the frontend repo).

Epics were assigned to the "To-do" status and move to "In progress" or "Done" status as the tasks in the user stories were completed.

![Agile](/static/images/agile/picture_1.png)

### Epics and user stories

![Epic_1](/static/images/agile/picture_2.png)

![Epic_2](/static/images/agile/picture_3.png)

![Epic_3](/static/images/agile/picture_4.png)

![Epic_4](/static/images/agile/picture_5.png)

!---

## Database structure

The user model is at the center of the structure and it's the starting point of 4 tables:
- Profile
- Post
- Service and
- Contact

4 more tables complete the schema:
- Followers, in-hand with Profile
- Like and Comment, relying on Post and
- Review, with the Service table.

![db](/static/images/erd/picture_1.png)

---

## Technologies used

The API was built using Django and the Django Rest Framework.

Below you can find the complete list of the libraries used for the development of this project:

- Django
- Django-cloudinary-storage: This Django package was used to provide Cloudinary storage for media (images and videos).
- Django-countries: Used for providing a country field in the Profile model.
- Django-phonenumber-field: Used to validate, pretty print and convert phone numbers.
- Django Rest Framework: For building the WEB API.
- Django-filter: Used for applying filters based on a specific condition.
- Gunicorn: Used to run Django on Heroku.
- dj_database_url: A Django utility for using the DATABASE_URL environment variable.
- Pillow: This Python library was used for image processing.
- Python-magic: This Python interface was used for uploaded video validation.
- Psycopg2: Used for connecting Python with PostgreSQL.

---

## Testing

Follow this link for the documentation related to [tests](/TESTING.md)

## Deployment

### Early deployement

A first deployment was made following these steps:

- Create an external database on ElephantSQL
- In the IDE, prepare environment:

  In env.py:

  - create file and add it to .gitignore
  - add the environment variables: secret key, cloudinary url, dev and database url

  In settings.py:

  - update the secret key section
  - connect the external database to the workspace by updating the database section and running migrations
  - configure Django to use Cloudinary (add Cloudinary to the 'Installed apps' and setup the default storage, url and media)
  - set the allowed host

- Create an application on Heroku and prepare the configuration variables on it

  - secret key
  - database url
  - cloudinary url
  - disable collectstatic

- Create and prepare a procfile
- Connect the repository to the Heroku app and deploy branch

The application successfully deployed an empty project:

![deployed app](/static/images/deployment/picture_1.png)

### Final deployment

The application was set to production following this steps:

- Add this line in the Procfile: release: python manage.py makemigrations && python manage.py migrate

In settings.py:

- Install django-cors-headers and add it to the INSTALLED_APPS
- Add corsheaders middleware at the top of the MIDDLEWARE
- Set the ALLOWED_ORIGINS for the network requests made to the server
- Enable sending cookies in cross-origin requests for user's authentication functionality
- Set the DEBUG value to False

### Forking

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

### Cloning

Cloning is used to create a local copy of the repository created in GitHub.
Both, the local copy and the remote are syncronized.

- Navigate to the GitHub Repository you want to clone.

- Above the list of files, click Code.

There are 3 possibilities for copying the URL of the repository: HTTPS, SSH key and GitHub CLI.
I'll develop the one that I use.

- Click the HTTPS tab and copy the URL.

- On your machine, open your text editor, go to the Command palette and click on Git Clone.

- Past the URL, hit enter and choose a folder to save the repository.   

---

## Credits

### Media

- Default images come from [Iconduck](https://iconduck.com/).

### Documentation

- The explanation about the libraries used in this project comes from [PyPI](https://pypi.org/).

### Code

- The IsOwnerOrReadOnly class comes from [Custom Permissions Examples](https://www.django-rest-framework.org/api-guide/permissions/#api-reference).
- The video extension validation in the Post model was inspired on [Django Media Files](https://www.youtube.com/watch?v=UcUm82jWeKc)
- Advised by my mentor, the implementation of the average calculation was inspired from [How to calculate average of some field in Django models and sent it to rest API](https://django.fun/en/qa/16172/)
