# ms_blog
Microservices Blogging Platform v1.3.0
---
## Project Overview
The Microservices Blogging Platform is a blogging platform using microservices built from a monorepo. 

This blogging platform supports authentication and authorization for user actions. Users are able post new articles consisting of a title, description, and collection of keywords. Users are also able to leave comments on the articles, and able to vote on articles through up-votes or down-votes.
---
## Quality Control Badges
---
## Build instructions
1. Install the software listed in ms_blog/SBOM.md
2. Start a Postgres database:
* Navigate to ms_blog/src/article/database
* Run: 
```bash
docker compose up
```
3. Navigate to ms_blog/src/article/service and run:
```bash
run: docker build -t docker-article-svc .
```
4. Start up MongoDB:
```Console
cd ms_blog/src/userauthentication
docker compose up -d
```
5. Install packages and activate the Pipenv shell:
```Console
cd ms_blog/src/userauthentication
pipenv sync
pipenv shell
```
6. Start up FastAPI Server:
```Console
uvicorn app.server.app:app --host localhost --port 8000 --reload
```
7. Go to (http://localhost:8000/docs#/) to test the API using swagger.
---
## Test instructions
1. Run the Build instructions
2. Navigate to ms_blog/src/article/database
3. To run the unit tests, run: 
```bash
go test *.go
```
---
## API documentation
There is no public API at the moment
