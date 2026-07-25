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


# 📅 Day 4 - Django Templates

## 🎯 Objective

Learn how Django uses templates to display HTML pages and understand how `render()` connects views with templates.

---

## 📚 Topics Covered

* What is a Django Template?
* Difference between `render()` and `HttpResponse`
* Template folder structure
* Creating HTML templates
* Rendering HTML pages using `render()`
* Creating multiple pages (Home, About, Services, Contact)
* Understanding the complete request flow in Django

---

## 🧠 Concepts Learned

### What is a Django Template?

A Django template is an HTML file that is used to display web pages. Instead of writing HTML inside Python code, Django separates the presentation layer into templates, making the project cleaner and easier to maintain.

### Why use `render()` instead of `HttpResponse`?

* `HttpResponse` returns plain text or HTML directly from Python.
* `render()` loads an HTML template, combines it with data (if provided), and returns the final webpage.
* `render()` is the standard way to build web pages in Django.

### Template Folder Structure

```text
home/
├── templates/
│   └── home/
│       ├── index.html
│       ├── about.html
│       ├── services.html
│       └── contact.html
```

Keeping templates inside the application folder prevents filename conflicts and keeps the project organized.

---

## 🔄 Django Request Flow

```text
Browser
   │
   ▼
config/urls.py
   │
   ▼
home/urls.py
   │
   ▼
views.py
   │
   ▼
render()
   │
   ▼
HTML Template
   │
   ▼
Browser
```

---

## 💻 Practical Work

* Created `index.html`
* Created `about.html`
* Created `services.html`
* Created `contact.html`
* Used `render()` to display HTML pages.
* Connected URLs with their corresponding views.
* Navigated between pages using a simple navigation bar.

---

## 📝 Commands Used

```bash
python manage.py runserver
```

---

## 🎓 Outcome

Today I learned how Django renders HTML templates using the `render()` function. I understood the relationship between URLs, views, and templates, and created multiple pages for my Django project using proper template organization.

---

