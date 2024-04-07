## Django notification system 

### Features
- Django DRFS
- Python 3.10
- PostgresSQL
- Docker
- Signal
- Pub/Sub Pattern


### Setup Docker
Install docker 
[Install Docker](https://docs.docker.com/engine/install/)


 build the docker containers. Open your terminal and write:
```bash
$ docker-compose up --build
```
run the migrations
```bash
$ docker-compose run app  python manage.py migrate
```
run the seed command to create user data and notifications
```bash
$ docker-compose run app  python manage.py seed_data
```


### Setup Application

the application will run on:  
http://localhost:8000/api/notifications
and for list users
http://localhost:8000/api/users

To run the frontend:
https://github.com/edy477/notificationapp 










