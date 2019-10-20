## Development and testing environments

  - Docker Compose (1.24.1, build 4667896b)
  - Docker  (1.13.1, build 092cba3)
  - Python docker image (python:3.7-alpine)
  - PostgreSQL docker image (postgres:11-alpine)


## How to run

Make sure that docker-compose and docker are installed on your system. Clone the repository and then change directory to the cloned repository.

Run the web application

```sh
docker-compose up -d web
```

Run the database migrations

```sh
docker-compose exec web python manage.py migrate
```

## API URL

- [http://localhost:8000/api/users/](http://localhost:8000/api/users/)

## Upload URL

- [http://localhost:8000/upload/](http://localhost:8000/upload/)


## How to run tests

Run the tests

```sh
docker-compose up test
```
