# she-codes-crowdfunding-api-project-KarthikaVC
she-codes-crowdfunding-api-project-KarthikaVC created by GitHub Classroom

Grad ED -To raise funds for students who are little low on funds and need financial support in doing their University Education.

## Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password
- [X] First Name
- [X] Last Name


### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create
  - [X] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [ ] Limit who can retrieve - Found this while I was grabbing the screenshots for submission. I need some more time to implement this feature.
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete

### Implement relevant status codes

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

### Handle failed requests gracefully 

- [X] 404 response returns JSON rather than text

### Use token authentication

- [X] impliment /api-token-auth/

## Additional features

- [X] Search Functionality for projects

To add a filter option to search based on supporters. 

- [ ] Share Functionality to friends via message or email.

{{ description of feature 2 }}

- [ ] To stop funding once the goal is attained.

{{ description of feature 3 }}

### External libraries used

- [X] django-filter


## Part A Submission

- [X] A link to the deployed project.
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- [X] Your refined API specification and Database Schema.

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
--url http://localhost:8000/users/ \
--header 'Authorization: Token 6ab20069897010a2b6e04bb4a3cd27e1a49a9292' \ --header 'Content-Type: application/json' \
--data '{
"username": "Insomnia_User", "email": "insomnia@example.com",
"password": "Testuser_123", "first_name": "FInsomnia", "last_name": "LInsomnia"
}'
```



2. Sign in User

Generate Token
```shell
curl --request POST \
--url http://localhost:8000/api-token-auth/ \ --header 'Content-Type: application/json' \ --data '{
"username":"Insomnia_User",
"password": "Testuser_123"
}'
```

3. Create Project

```shell
curl --request POST \
--url http://localhost:8000/projects/ \
--header 'Authorization: Token 08d62cb7d30d46fb3c4af0f511a16102dba4f0e3' \ --header 'Content-Type: application/json' \
--data '{
"title": "Donation for Student B Education - Insomnia Testing for USer created by insomnia",
"description": "Collecting funds for college student B",
"goal": 2000,
"image": "https://cfstatic.give.do/b443c864-8bd7-4490-9374-9f70aa9ca699.webp", "is_open": true,
"date_created": "2023-01-29T10:46:30.333Z"
}'
```

4. Create Pledge 

```shell
curl --request POST \
--url http://localhost:8000/pledges/createPledge \
--header 'Authorization: Token 6ab20069897010a2b6e04bb4a3cd27e1a49a9292' \ --header 'Content-Type: application/json' \
--data '{
"amount": 1607,
"comment": "Adding pledges For Sunny with $1607 for project 14 ",
"anonymous": true, "project": 14
}'
```

5. Edit profile 
```shell
curl --request PUT \
--url http://localhost:8000/users/update_Profile/46/ \
--header 'Authorization: Token 08d62cb7d30d46fb3c4af0f511a16102dba4f0e3' \ --header 'Content-Type: application/json' \
--data '{
"username": "Insomnia_User1", "email": "insomnia1@example.com", "first_name": "FInsomniaEdit",
"last_name": "LInsomniaEdit" }'
```

6. Change Password 
```shell
curl --request PUT \
--url http://localhost:8000/users/change_Pwd/46/ \
--header 'Authorization: Token 08d62cb7d30d46fb3c4af0f511a16102dba4f0e3' \ --header 'Content-Type: application/json' \
--data '{
"old_password" :"Testuser_123",
"new_password": "Testuser_1234" }'
```

7. PUT - Edit a project 
```shell
curl --request PUT \
--url http://localhost:8000/projects/19/ \
--header 'Authorization: Token 08d62cb7d30d46fb3c4af0f511a16102dba4f0e3' \ --header 'Content-Type: application/json' \
--data '{
"id": 19,
"title": "Donation for Student B Education - Insomnia Testing for User created by insomnia",
"description": "Collecting funds for college student B",
"goal": 2000,
"image": "https://cfstatic.give.do/b443c864-8bd7-4490-9374-9f70aa9ca699.webp", "is_open": true,
"date_created": "2023-01-29T10:45:40.761000Z",
"owner": 46,
"total": null
}'
```

8. PUT - Edit a pledge 
```shell
curl --request PUT \
--url http://localhost:8000/pledges/editPledge/21 \
--header 'Authorization: Token 6ab20069897010a2b6e04bb4a3cd27e1a49a9292' \ --header 'Content-Type: application/json' \
--data '{
"amount" : "1000",
"comment": " Updated Comment for Project 14", "anonymous" :false,
"project":14
}'
```
