# Owlint Technical Test API 

## CommentsGate API version: "1.0.0"

Last commit before the date and time limits of the challenge here : https://github.com/nojoven/CommentsGate/commit/bf06aed1886d9c14dd5120ec575e00324fa780aa

This API processes comments.

- The URL is http://localhost/target/**targetId**/comments
- A GET request returns the comments of a target object.
- A POST request is used to save a new comment in the database. 
The API will also send each new comment to another service.

Actual valid environment variables are not present in this repository.

### Contact: laurent@owlint.fr

## Important
Please add environment variables /config/.env


## Getting started without Docker:

- Install the database on the host of the container
- Activate the virtualenv
- In CommentsGate/app/, run the following command:
  **uvicorn main:app --reload**

## Getting started using Docker:
- Install and configure a postgresql database on the host of the container
- docker build -t owlapi .
- docker run -d --env-file ./config/.env -p 8000:8000 --name test owlapi

## Getting started using docker-compose:
docker-compose --env-file ./config/.env up -d --build
