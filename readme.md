# FullStack-Development (Django)

## Introduction To Django Web Framework

## Django
- Django is an open-source web development framework written in Python.
- Django follows MVT([Model](/models.md)-[View](/views.md)-[Templates](/templates.md)) pattern
- Django provides features such as `Templates`, `Libraries`, and `APIs`.
- Django is popular because of its ease of scalability.
- Django is a `Full-Stack` framework, but developers can use it to create `backend` systems and connect them with any frontend framework like `React`, `Angular`, `Vue`, etc., through `API`.
  
  ![alt text](/assets/image-2.png)

## Django Project Setup In VSCode
1. **Python Interpreter**: First, you need a Python interpreter. Select it from the `Command Palette` in VSCode.
  
  ![alt text](/assets/image-1.png)

2. **Create a Virtual Environment**:
   - Use the following command:
     ```sh
     python -m venv .venv
     ```
   - `.venv` is the folder name where the virtual environment is created. You can name this folder anything you like.
   - Python recommends using a virtual environment to build Python applications.
   - A `Virtual Environment` is an isolated environment that has its own copy of the interpreter and libraries to avoid conflicts with the global Python installation.

3. **Activate the Virtual Environment**:
   - Use the following command:
     ```sh
     .venv\Scripts\activate
     ```

4. **Install the Django Framework**:
   - Use the following command:
     ```sh
     pip install Django
     ```
   - To deactivate the virtual environment, simply use:
     ```sh
     deactivate
     ```

## Project and Apps
### Project & Apps
- In Django, a `Project` represents an entire web application.
- An `App` is a sub-module of a project.
- A `Project` can have multiple `Apps`.
  
  ![alt text](/assets/image-3.png)

- A Django `Project` is a Python package that includes the configuration for the database, various sub-modules known as `Apps`, and other settings specific to Django.

## Steps to Create a Django Project and App

### 1. Install Django
First, ensure you have Django installed. You can install it using `pip`:
```sh
pip install django
```

### 2. Create a Django Project
To create a new Django project, use the `django-admin` command followed by `startproject` and your project name. For example, to create a project named `myproject`:
```sh
django-admin startproject myproject
```

This will create a directory structure like this:
```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
```
![alt text](/assets/image-4.png)

### 3. Navigate to Your Project Directory
Change into the project directory:
```sh
cd myproject
```

### 4. Create a Django App
Inside your project directory, create a new Django app using the `manage.py` script. For example, to create an app named `myapp`:
```sh
python manage.py startapp myapp
```

This will create a directory structure like this:
```
myapp/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    migrations/
        __init__.py
```
![alt text](/assets/image-5.png)

### 5. Register the App in the Project
To make Django recognize the app, you need to add it to the `INSTALLED_APPS` list in your project's `settings.py` file.

Open `myproject/settings.py` and add `'myapp',` to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```
![alt text](/assets/image-6.png)

### 6. Run Migrations
Django manages the databases operations with the ORM techniques.
ORM, or Object-Relational Mapping, is a programming technique used to interact with a database using an object-oriented paradigm. In the context of Django, ORM allows developers to work with databases using Python classes and objects rather than writing raw SQL queries.

#### What is ORM?

1. **Definition**:
   - **Object-Relational Mapping (ORM)** is a method of mapping a database schema to an object-oriented model. It allows developers to manipulate database entries as if they were regular Python objects.

2. **How ORM Works in Django**:
   - Django ORM translates Python code into SQL queries. It provides a high-level abstraction over the database that lets you interact with it using Python instead of SQL.
   - You define your database schema as Python classes (called models), and Django handles the SQL behind the scenes to create and manage the database tables.

3. **Advantages of Using ORM**:
   - **Simplicity**: ORM abstracts the database operations, making it easier for developers to interact with the database.
   - **Portability**: The same ORM code can work with different databases (e.g., SQLite, PostgreSQL, MySQL) without modification.
   - **Security**: ORM helps prevent SQL injection attacks by using parameterized queries.

#### Example of ORM in Django

#### Defining a Model in App

In Django, you define your database schema using models. Here is an example of a simple model representing a `Book`:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

#### Creating a Migration

After defining your models, you need to create and apply migrations to generate the corresponding database tables. This is how Django manages the database schema.

1. **Create Migrations**:
   ```sh
   python manage.py makemigrations
   ```

2. **Apply Migrations**:
   ```sh
   python manage.py migrate
   ```
The above two commands should be run whenever a new model is created or any change is done in existing model.
![alt text](/assets/image-9.png)
#### Using the ORM

Once the migrations are applied, you can use the ORM to create, retrieve, update, and delete records in the database.

0. **Open the Django Shell**
   ```sh
   python manage.py shell
   ```
1. **Create a Record**:
   ```python
   from myapp.models import Book
   book = Book(title="Django for Beginners", author="John Doe", published_date="2023-01-01")
   book.save()
   ```

2. **Retrieve Records**:
   ```python
   all_books = Book.objects.all()
   book = Book.objects.get(id=1)
   ```

3. **Update a Record**:
   ```python
   book = Book.objects.get(id=1)
   book.title = "Advanced Django"
   book.save()
   ```

4. **Delete a Record**:
   ```python
   book = Book.objects.get(id=1)
   book.delete()
   ```
5. **Exit from the shell**
   ```sh 
   exit() 
   ``` 
![alt text](/assets/image-8.png)

### 7. Create a View
Define a simple view in `myapp/views.py`. For example:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! This is my home page.")
```

### 8. Map the View to a URL
Create a URL configuration for your app. In `myapp`, create a file named `urls.py` and add:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Then, include this URL configuration in your project’s `urls.py` file (`myproject/urls.py`):
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### 9. Run the Development Server
Start the development server to see your project in action:
```sh
python manage.py runserver
```

Open a web browser and go to `http://127.0.0.1:8000/`. You should see the message "Hello, world! This is my home page."

![alt text](/assets/image-7.png)

## MVT Architecture
The MVT (Model-View-Template) architecture is the design pattern used by Django to build web applications. It is a variation of the MVC (Model-View-Controller) pattern tailored to suit the needs of web development with Django. Here’s an overview of each component in the MVT architecture:

![alt text](/assets/image-11.png)

### MVT Components

1. **Model**:
   - The **Model** is the data access layer. It defines the structure of the database, including the tables and their relationships, as well as the methods to interact with the data.
   - In Django, models are defined as Python classes, which Django's ORM (Object-Relational Mapping) then translates into database tables.
   - Example:
     ```python
     from django.db import models

     class Book(models.Model):
         title = models.CharField(max_length=200)
         author = models.CharField(max_length=100)
         published_date = models.DateField()
     ```

2. **View**:
   - The **View** is the business logic layer. It processes user requests, interacts with the model to retrieve data, and determines what data to send back to the user.
   - Views in Django are Python functions or classes that receive web requests and return web responses.
   - Example:
     ```python
     from django.shortcuts import render
     from .models import Book

     def book(request):
         books = Book.objects.all()
         return render(request, 'book.html', {'books': books})
     ```

3. **Template**:
   - The **Template** is the presentation layer. It defines how the data received from the view should be displayed to the user.
   - Templates in Django are HTML files with Django Template Language (DTL) which allows for dynamic content insertion.
   - Example (`home.html`):
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>Home Page</title>
     </head>
     <body>
         <h1>Book List</h1>
         <ul>
             {% for book in books %}
                 <li>{{ book.title }} by {{ book.author }}</li>
             {% endfor %}
         </ul>
     </body>
     </html>
     ```

### How MVT Works Together

1. **Request**:
   - A user sends a request to the Django application by entering a URL in the browser.

2. **URL Routing**:
   - Django uses URLconf to map the URL to a specific view. The `urls.py` file contains these mappings.
   - Example (`urls.py`):
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.home, name='home'),
     ]
     ```

3. **View Processing**:
   - The view function associated with the URL is called. This view processes the request, interacts with the model to get data, and passes the data to the template.
   - Example view (`views.py`):
     ```python
     def home(request):
         books = Book.objects.all()
         return render(request, 'home.html', {'books': books})
     ```

4. **Template Rendering**:
   - The template receives the data from the view and renders it into HTML to be sent back to the user.
   - Example template (`home.html`):
     ```html
     <ul>
         {% for book in books %}
             <li>{{ book.title }} by {{ book.author }}</li>
         {% endfor %}
     </ul>
     ```

5. **Response**:
   - The rendered HTML is sent back to the user’s browser as a response, which displays the data in a web page.
  
  ![alt text](/assets/image-10.png)

### Summary

The MVT architecture in Django allows for a clear separation of concerns:
- **Model**: Manages the data and database interactions.
- **View**: Contains the business logic and handles user requests.
- **Template**: Defines the presentation and how data is displayed to the user.

This structure helps in organizing code, making it more maintainable and scalable.

