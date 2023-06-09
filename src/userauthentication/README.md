# User Authentication Microservice
This Microservice provides User Authentication and Authorization to the Blogging Platform. 
#
### TODO: 
- Add useful and intuitive API endpoints 
- Implement update functionality to CRUD API for user data
- Implement unittesting for CRUD operations
- Update documentation and directory heirachy for readability
- Implement Authentication and Authorization using JWTs (JSON Web Tokens)
- Containerize the microservice with Kubernetes
#
Currently the API is set up to read, add, and delete user data from MongoDB. 

### User Schema:
```Json
{
  "_id": { "$oid": "##########"},
  "username": "string",
  "password": "string",
  "email": "string@example.com"
}
```

### To Run:

Start up MongoDB:
```Console
cd ms_blog/src/userauthentication
docker compose up -d
```
Install packages and activate the Pipenv shell:
```Console
cd ms_blog/src/userauthentication
pipenv sync
pipenv shell
```
Start up FastAPI Server:
```Console
uvicorn app.server.app:app --host localhost --port 8000 --reload
```
Go to (http://localhost:8000/docs#/) to test the API using swagger.





