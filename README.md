﻿# Gyaanbee-Assesment
## 1.React Native OTP Authentication App with FastAPI

A simple mobile application for OTP authentication using React Native and a FastAPI server for sending SMS with one-time passwords.

## React Native App

### Prerequisites

- Node.js and npm installed
- React Native development environment set up

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/anugrahprathap/Gyaanbee-Assesment.git
   cd react-native-otp-auth


2. **Install dependencies:**

```bash

npm install
```
3. **Running the App:**
*Start the React Native app:*

```bash

npx react-native run-android
```
*Make sure to run it on an Android emulator or a physical Android device.*

*Open the app on your device/emulator.*

## FastAPI Server
1.**Prerequisites**
-Python 3.6+
-FastAPI and other dependencies installed (use pip install -r requirements.txt)
2.**Running the Server**
*Navigate to the fastapi-server directory:*

```bash
cd fastapi-server
```
*Run the FastAPI server:*

```bash

uvicorn main:app --reload
````
*The server will be running at http://127.0.0.1:8000.*

## API Endpoints
1. **Send SMS with OTP**
*Endpoint: /send-sms
Method: POST*
Request Payload:
```json

{
  "to": "phone-number"
}
```
*Replace "phone-number" with the actual phone number.*
## Notes
The React Native app uses Axios for making HTTP requests to the FastAPI server.
The FastAPI server generates a 6-digit OTP using the pyotp library.






## 2. FastAPI Task Management API

A simple FastAPI web application for managing tasks with CRUD operations (Create, Read, Update, Delete). Tasks are stored in a SQLite database using SQLAlchemy.

## Features

- Create new tasks
- View tasks with optional completion status filter
- View a single task by ID
- Update the details of an existing task
- Delete a task by ID

## Getting Started

### Prerequisites

- Python 3.6+
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/anugrahprathap/Gyaanbee-Assesment.git
   cd fastapi-task-management
2. **Install dependencies:**

```bash
#!/bin/bash
pip install -r requirements.txt
```
3. **Running the Application:**
```bash
#!/bin/bashuvicorn main:app --reload

```
Open your browser and navigate to http://127.0.0.1:8000/docs to access the FastAPI Swagger documentation. Alternatively, you can use http://127.0.0.1:8000/redoc
for the ReDoc documentation.

## API Endpoints
   
1. **Create a new task:**
*Endpoint: /tasks/
Method: POST*

Request Payload:
```json
{
  "title": "Task Title",
  "description": "Task Description",
  "completed": false
}
```
2. **View tasks with completion status filter:**
*Endpoint: /tasks/
Method: GET
Query Parameters:
completed (optional): Filter tasks by completion status (true/false)
View a single task by ID
Endpoint: /tasks/{task_id}
Method: GET
Update task by ID
Endpoint: /tasks/{task_id}
Method: PUT*
Request Payload:
```json
{
  "title": "Updated Title",
  "description": "Updated Description",
  "completed": true
}
```
3. **Delete task by ID**
*Endpoint: /tasks/{task_id}
Method: DELETE*
Dependencies:
```bash
FastAPI
SQLAlchemy
Uvicorn
```


