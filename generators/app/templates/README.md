# Sample Docker Django App

## Pre-Requisites:
- Python3.7
- Docker
- Docker Compose
- Virtual environment `pip3 install virtualenv`

## Serve API Locally:
	
- Start Containers:
	```ssh
	$ docker-compose -p <%= name %> up --build -d
	```

- Run migrations:
	```ssh
	$ docker exec <%= name %>_api python3.7 manage.py migrate
	```

- Create django admin user:
	```ssh
	$ docker exec -it <%= name %>_api python3.7 manage.py createsuperuser
	Username (leave blank to use 'root'): root
	Email address: test@test.com
	Password:
	Password (again):
	```

- Browse local django instance via `localhost:8080/admin`

## Running tests:
- Activate virtual environment:
	```ssh
	$ virtualenv venv # Create virtual environment if does not exist
	$ source venv/bin/activate
	```

- Install dependencies
	```ssh
	$ pip install -r tests/requirements.txt
	```

- Run tests
	```ssh
	$ pytest
	```