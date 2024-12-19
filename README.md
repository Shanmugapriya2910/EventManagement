# Event Management API

This project is an Event Management API built using Django. It enables users to create, read, update, and delete events.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete operations on events.

## Technologies Used
- **Django**
- **Django REST Framework**
- **Postgresql**

## Installation

### Requirements
- Python 3.9
- Django
- Django REST Framework
- Postgresql

### Setup Steps
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

2. Navigate into the project directory:
   ```bash
   cd <project-directory>
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. The application will be running at `http://127.0.0.1:8000/`.

## API Endpoints

- **GET /api/events/**: Retrieve a list of all events.
- **POST /api/events/**: Create a new event.
- **GET /api/events/1/**: Retrieve a specific event by its ID.
- **PUT /api/events/1/**: Update an existing event.
- **DELETE /api/events/1/**: Delete an event.

## Project Structure

```bash
EventManagement/
├── EventManager/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── EventManagement/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── manage.py
```

## API Endpoints

1. **Create an Event (POST)**

   **URL:** `http://127.0.0.1:8000/api/events/`
   
   **Method:** `POST`
 
   **Request Body:**
   ```json
   {
     "name": "Music Concert",
     "description": "A live music concert.",
     "start_date": "2024-12-25T18:00:00Z",
     "end_date": "2024-12-25T22:00:00Z",
     "location": "City Stadium"
   }
   ```

2. **Get All Events (GET)**

   **URL:** `http://127.0.0.1:8000/api/events/`
   
   **Method:** `GET`

   **Request Body:**
   ```json
   [
     {
       "id": 1,
       "name": "Music Concert",
       "description": "A live music concert.",
       "start_date": "2024-12-25T18:00:00Z",
       "end_date": "2024-12-25T22:00:00Z",
       "location": "City Stadium"
     },

3. **Get Event by ID (GET)**

   **URL:** `http://127.0.0.1:8000/api/events/1/`
   
   **Method:** `GET`

   **Request Body:**
   ```json
   {
     "id": 1,
     "name": "Music Concert",
     "description": "A live music concert.",
     "start_date": "2024-12-25T18:00:00Z",
     "end_date": "2024-12-25T22:00:00Z",
     "location": "City Stadium"
   }
   ```
   
4. **Update Event by ID (PUT)**

   **URL:** `http://127.0.0.1:8000/api/events/1/`
   
   **Method:** `PUT`
   
   **Request Body:**
   ```json
   {
     "name": "Updated Music Concert",
     "description": "A new description of the live music concert.",
     "start_date": "2024-12-25T19:00:00Z",
     "end_date": "2024-12-25T23:00:00Z",
     "location": "New City Stadium"
   }
   ```

5. **Delete Event by ID (DELETE)**

   **URL:** `http://127.0.0.1:8000/api/events/1/`
   
   **Method:** `DELETE`
   
   **Example Response:**
   ```json
   {
     "message": "Event deleted successfully"
   }
   ```

## Instructions

1. **Creating an Event:**
   To create an event, send a `POST` request to `http://127.0.0.1:8000/api/events/` with the event details in the body. 

2. **Getting All Events:**
   To retrieve a list of all events, send a `GET` request to `http://127.0.0.1:8000/api/events/`.

3. **Getting an Event by ID:**
   To retrieve the details of an event, send a `GET` request to `http://127.0.0.1:8000/api/events/{id}/` where `{id}` is the ID of the event.

4. **Updating an Event by ID:**
   To update an event, send a `PUT` request to `http://127.0.0.1:8000/api/events/{id}/` with the updated event details.

5. **Deleting an Event by ID:**
   To delete an event, send a `DELETE` request to `http://127.0.0.1:8000/api/events/{id}/` where `{id}` is the ID of the event to delete.

   

  


















