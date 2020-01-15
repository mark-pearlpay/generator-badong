# Sample Docker Django App

## How to run locally for development:

1. Install `python3.7` and `python3-pip`
2. Install `docker`
3. Install `docker-compose` with `pip3 install docker-compose`
4. Clone this repository: `git clone git@github.com:PearlEngineering/django-onion-test.git`
5. Go into the repository directory: `cd django-onion-test`
6. Run: `docker-compose -p django_onion up --build -d` to spin up the mysql and django containers
7. Run: `docker exec django_api python3.7 manage.py migrate` to run the django database migration scripts
8. Run: `docker exec -it django_api python3.7 manage.py createsuperuser` then follow the commandline prompts to create a django admin user:

   `Username (leave blank to use 'root'): <enter username>`

   `Email address: <enter email_address>`

   `Password: <enter password>`
 
   `Password (again): <enter password>`
 
   `Superuser created successfully.`
9. In your preferred browser, go to `localhost:8080/admin` for the django admin webapp
10. In your preferred browser, go to `localhost:8080/videos` for the sample djangorestframework UI
11. In postman or curl, `GET localhost:8080/videos` to retrieve the list of videos 
12. To kill the docker containers, Run: `docker-compose -p django_onion down`