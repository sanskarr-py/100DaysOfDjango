# Day 01 - Django Setup

## What I Learned

- What Django is
- How to create a virtual environment
- How to install Django
- How to create a Django project
- Project structure
- Running the development server

## Commands Used

```bash
py -m venv .venv
.\.venv\Scripts\Activate
pip install django
django-admin startproject config core
python manage.py runserver
```

## Outcome

Successfully created my first Django project and ran the development server.

## Day 2

### Topics Learned
- Django Project vs App
- Creating an app
- URL routing
- Views
- HttpResponse

### Commands Used

python manage.py startapp home
python manage.py runserver

### Outcome

Successfully created my first Django app and displayed a custom webpage.

# Day 3 - URLs and Views in Django

## Topics Learned

* What `urls.py` is and why it is used.
* How URL routing works in Django.
* What `views.py` is and its role in handling requests.
* How a view processes a request and returns a response.
* How the main `config/urls.py` delegates requests to the `home` app using `include()`.
* Why each Django app should have its own `urls.py` file to keep the project organized.

## Key Concepts

### `config/urls.py`

The main URL configuration for the entire Django project. It receives incoming requests and forwards them to the appropriate app.

### `home/urls.py`

Contains the URL patterns specific to the `home` app. This keeps each app independent and easier to maintain.

### `views.py`

A view is a Python function that receives an HTTP request, performs the required logic, and returns an HTTP response or renders an HTML template.

### Request Flow

```
Browser
   ↓
config/urls.py
   ↓
home/urls.py
   ↓
views.py
   ↓
HTML Template / HttpResponse
   ↓
Browser
```

## Outcome

Today I understood how Django routes requests from the main project to an app, how views handle those requests, and how URLs and views work together to display web pages.
