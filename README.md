# Task API

## Overview

This is a FastAPI-based project for managing tasks. It provides a RESTful API for creating, reading, updating, and deleting tasks.

## Features

- Create a new task
- Retrieve all tasks with pagination support
- Retrieve a specific task by ID
- Update an existing task
- Delete a task
- Consistent API response structure using a generic response model

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:

   - Create a `.env` file in the root directory of your project.
   - Add the following content to the `.env` file:
     ```env
     DATABASE_URL=<your-database-connection-url>
     ```
   - Alternatively, use the provided `.env.example` file as a template.

5. Set up the database:

   - Update your database connection details in the `.env` file.
   - The project uses SQLAlchemy for ORM and expects a database to be configured.

6. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

7. Access the API documentation:
   - Open your browser and go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

### Task Endpoints

#### 1. Create Task

- **URL:** `/tasks/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "title": "Task Title",
    "description": "Task Description"
  }
  ```
- **Response:**
  ```json
  {
    "ok": true,
    "message": "task created successfully",
    "data": {
      "id": 1,
      "title": "Task Title",
      "description": "Task Description"
    }
  }
  ```

#### 2. Retrieve All Tasks

- **URL:** `/tasks/`
- **Method:** `GET`
- **Query Parameters:**
  - `skip` (default: 0)
  - `limit` (default: 100)
- **Response:**
  ```json
  {
    "ok": true,
    "message": "tasks retrieved successfully",
    "data": [
      {
        "id": 1,
        "title": "Task Title",
        "description": "Task Description"
      }
    ]
  }
  ```

#### 3. Retrieve Task by ID

- **URL:** `/tasks/{task_id}`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "ok": true,
    "message": "task retrieved successfully",
    "data": {
      "id": 1,
      "title": "Task Title",
      "description": "Task Description"
    }
  }
  ```

#### 4. Update Task

- **URL:** `/tasks/{task_id}`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "title": "Updated Task Title",
    "description": "Updated Task Description"
  }
  ```
- **Response:**
  ```json
  {
    "ok": true,
    "message": "task updated successfully",
    "data": {
      "id": 1,
      "title": "Updated Task Title",
      "description": "Updated Task Description"
    }
  }
  ```

#### 5. Delete Task

- **URL:** `/tasks/{task_id}`
- **Method:** `DELETE`
- **Response:**
  ```json
  {
    "ok": true,
    "message": "task deleted successfully",
    "data": {
      "id": 1
    }
  }
  ```

## Project Structure

```
app/
├── __init__.py
├── models.py          # SQLAlchemy models
├── schemas.py         # Pydantic schemas
├── database.py        # Database configuration
main.py                # FastAPI application entry point
requirements.txt       # Dependencies
```

## Dependencies

- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## License

This project is licensed under the MIT License.
