# Articles Microservice
---
The Articles Microservice is a Golang application for transporting articles between the Microservices Blogging Platform UI and the Articles database.
---
## Installation
No additional installation steps are necessary.
---
## Usage
The following steps require the usage of a command line terminal.

1. Begin by starting a Postgres database:
* Navigate to ms_blog/src/article/database
* Run: 
```bash
docker compose up
```
2. To run the application, navigate to ms_blog/src/article/service
2. a. To install a containerized version of the application, 
```bash
run: docker build -t docker-article-svc .
```
2. b. To run independently, run: 
```bash
go run main
```
2. c. To run the unit tests, run: 
```bash
go test *.go
```
