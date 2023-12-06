# Express API with SQLite Database - User CRUD Operations

This project demonstrates a basic REST API using Express and Node.js, implementing CRUD operations for a "User" resource and connecting to an SQLite database using Sequelize as the ORM.

## Getting Started
### Prerequisites
Make sure you have following installed

- Node.js
- npm (Node Package Manager)

### Installation
1. Clone this repository
```bash
git clone https://github.com/nhatquang99/homebase-challenge.git
```
2. Navigate to the project directory
```bash
cd express
```
3. Install dependencies
```bash
yarn 
```
4. Run project
```bash
node index.js
```

## API Endpoints

### Get All Users

* Endpoint: `users`
* Method: GET

### Get User Detail
* Endpoint: `users/:id`
* Method: GET

### Create User
* Endpoint: `users`
* Method: POST
* Body: 
  - username: string
  - email: string

### Update User
* Endpoint: `users/:id`
* Method: PUT
* Body: 
  - username: string

### Delete User
* Endpoint: `users/:id`
* Method: DELETE




