# Models

## Models in Django
A `Model` is a 
 - Definitive source of information about your data. 
 - It contains essential fields and behaviors of data you are storing. 
 - Generally each model maps to a single database table.
  
![alt text](/assets/image-12.png)

![alt text](/assets/image-13.png)

## Models Realtionship

In Django, relationships between models are defined using special fields that create database relationships. The main types of relationships are:

1. **One-to-One**
2. **One-to-Many (ForeignKey)**
3. **Many-to-Many**

Here's an overview of each relationship type with code examples:

### 1. One-to-One Relationship

A one-to-one relationship is where one record in a model is associated with one and only one record in another model.

**Example: User Profile**

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
```

In this example:
- `Profile` has a one-to-one relationship with the `User` model.
- The `on_delete=models.CASCADE` ensures that when a `User` is deleted, the related `Profile` is also deleted.

### 2. One-to-Many Relationship (ForeignKey)

A one-to-many relationship is where one record in a model can be related to multiple records in another model. This is implemented using a `ForeignKey`.

**Example: Author and Books**

```python
# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

In this example:
- `Book` has a foreign key to `Author`, indicating that each book is written by one author.
- The `on_delete=models.CASCADE` ensures that when an `Author` is deleted, all related `Book` instances are also deleted.

### 3. Many-to-Many Relationship

A many-to-many relationship is where multiple records in one model can be related to multiple records in another model. This is implemented using a `ManyToManyField`.

**Example: Students and Courses**

```python
# models.py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
```

In this example:
- `Student` has a many-to-many relationship with `Course`, indicating that a student can enroll in multiple courses and a course can have multiple students.

### Using Relationships

#### One-to-One Relationship Usage

```python
# Creating a User and Profile
user = User.objects.create(username='john')
profile = Profile.objects.create(user=user, bio='Hello, I am John!', birth_date='1990-01-01')

# Accessing related data
print(profile.user.username)  # Output: john
print(user.profile.bio)       # Output: Hello, I am John!
```

#### One-to-Many Relationship Usage

```python
# Creating an Author and Books
author = Author.objects.create(name='George Orwell')
book1 = Book.objects.create(title='1984', author=author, published_date='1949-06-08')
book2 = Book.objects.create(title='Animal Farm', author=author, published_date='1945-08-17')

# Accessing related data
print(author.book_set.all())  # Output: <QuerySet [<Book: 1984>, <Book: Animal Farm>]>
print(book1.author.name)      # Output: George Orwell
```

#### Many-to-Many Relationship Usage

```python
# Creating Students and Courses
course1 = Course.objects.create(name='Math 101')
course2 = Course.objects.create(name='History 101')

student = Student.objects.create(name='Alice')
student.courses.add(course1, course2)

# Accessing related data
print(student.courses.all())      # Output: <QuerySet [<Course: Math 101>, <Course: History 101>]>
print(course1.student_set.all())  # Output: <QuerySet [<Student: Alice>]>
```

#### Summary

- **One-to-One**: Each record in one model is linked to one and only one record in another model.
- **One-to-Many (ForeignKey)**: Each record in one model can be linked to multiple records in another model.
- **Many-to-Many**: Multiple records in one model can be linked to multiple records in another model.

These relationships allow you to structure your data efficiently and retrieve related objects easily in Django.

## Database Migrations

In Django, database migrations are a way of propagating changes you make to your models (e.g., adding a field, deleting a model) into your database schema. The process involves two main commands: `makemigrations` and `migrate`. Here’s what each command does:

![alt text](/assets/image-14.png)

### `makemigrations`

The `makemigrations` command is responsible for creating new migration files based on the changes you have made to your models.

1. **Detect Changes**: It detects changes made to the models by comparing the current state of the models with the state stored in the last set of migrations.
2. **Create Migration Files**: It creates migration files that represent these changes. These files are Python scripts that define the operations needed to apply the changes to the database schema.

**Example Usage**:

```sh
python manage.py makemigrations
```

**Example Output**:

```python
Migrations for 'myapp':
  myapp/migrations/0002_auto_20230101_1234.py
    - Add field birth_date to profile
```

### `migrate`

The `migrate` command is responsible for applying the migrations to your database, thereby updating the database schema to reflect the changes made to the models.

1. **Read Migration Files**: It reads the migration files created by `makemigrations`.
2. **Apply Changes**: It applies the changes defined in the migration files to the database in the correct order, ensuring that the schema is updated properly.

**Example Usage**:

```sh
python manage.py migrate
```

**Example Output**:

```py
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions
Running migrations:
  Applying myapp.0002_auto_20230101_1234... OK
```

### Workflow

1. **Modify Models**: You make changes to your models, such as adding a new field or creating a new model.
2. **Create Migrations**: You run `python manage.py makemigrations` to create migration files that capture the changes.
3. **Apply Migrations**: You run `python manage.py migrate` to apply the changes to the database schema.

### Detailed Example

#### Step 1: Modify Models

```python
# models.py
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)  # Added field
```

#### Step 2: Create Migrations

```sh
python manage.py makemigrations
```

This will generate a new migration file in the `migrations` directory of your app.

#### Step 3: Apply Migrations

```sh
python manage.py migrate
```

This will apply the changes defined in the migration file to your database.

### Summary

- **`makemigrations`**:
  - Detects changes in the models.
  - Creates migration files that describe the changes.

- **`migrate`**:
  - Reads the migration files.
  - Applies the changes to the database schema.

These two commands are essential for managing database schema changes in a Django project, ensuring that your database structure is always in sync with your model definitions.


## Django Admin Interface `( Inbuilt Admin Panel By Django )`
Django Admin is a powerful and customizable interface for managing your project's models.

In Django, you register your models in the `admin.py` file of your app to make them available in the Django admin interface. This allows you to manage your models (e.g., add, edit, delete records) through a user-friendly web interface provided by Django.

### Setting Up Django Admin
**1. Create A Superuser**

A superuser has all permission and can manage all aspects of the application. To create a superuser, run the following command in your terminal

    python manage.py createsuperuser

You will be prompted to enter a username, email, and password. After you complete these prompts, a superuser will be created.

![alt text](/assets/image-15.png)


### When to Register Your Models

1. **After Creating a New Model**: Once you've defined a new model in your `models.py` file and applied the corresponding migrations to create the database table, you should register the model in `admin.py` if you want to manage it via the admin interface.

2. **When You Want Admin Interface Functionality**: If you need the ability to manage instances of your model (view, add, change, delete) using Django's admin interface, you'll need to register the model.

### How to Register Your Models

You register your models in the `admin.py` file of your app. Here’s how to do it:

1. **Basic Registration**:
   Simply import your model and use `admin.site.register` to register it.

   ```python
   # admin.py
   from django.contrib import admin
   from .models import YourModel

   admin.site.register(YourModel)
   ```

2. **Customizing the Admin Interface**:
   If you want to customize how your model is displayed in the admin interface, you can use a `ModelAdmin` class.

   ```python
   # admin.py
   from django.contrib import admin
   from .models import YourModel

   class YourModelAdmin(admin.ModelAdmin):
       list_display = ('field1', 'field2', 'field3')  # Fields to display in the list view
       search_fields = ('field1', 'field2')          # Fields to search in the list view
       list_filter = ('field1', 'field2')            # Fields to filter in the list view

   admin.site.register(YourModel, YourModelAdmin)
   ```

### Example

Let's say you have a `Book` model and an `Author` model. Here’s how you might register them in the `admin.py` file:

#### Define Models

```python
# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

#### Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

#### Register Models

```python
# admin.py
from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('published_date',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
```

In this example:
- The `Author` model is registered with a custom `AuthorAdmin` class to customize its admin interface.
- The `Book` model is registered with a custom `BookAdmin` class, which includes configurations for list display, search fields, and filters.
  
#### Accessing Django Admin

Run the development server: 

```sh
 python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/admin` in your web browser. Log in with the superuser credentials you created earlier. 

![alt text](/assets/image-16.png)

You should see the registered models in the admin interface.
Here `Book` is  the registered model.

![alt text](/assets/image-17.png)

### Summary

- **When to Register**: Register your models in `admin.py` after creating them and applying migrations if you want to manage them via the Django admin interface.
- **How to Register**: Use `admin.site.register` to register models, and optionally create a `ModelAdmin` class to customize the admin interface.
- **Example**: The provided example shows the basic and customized registration of models to make them manageable through the Django admin interface.


## Django Form

### Django Form Overview

Django forms are Python classes that define the fields and behavior of an HTML form. They encapsulate data validation, security measures (like CSRF protection), and rendering html. Django forms can be created using Python classes (`forms.Form`) or by leveraging models (`forms.ModelForm`).



## Types of Django Forms

### 1. Basic Form
- Used for creating forms without tying them to any model.
- Requires explicit definition of form fields.
- If you want to save data in the database, create a model as well.

#### Example

#### Create a Model

`models.py`
```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
```

#### Create a Form

`forms.py`
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
```

#### Create a Template to Render the Form

`contact_form.html`
```html
<!-- contact_form.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        <label for="id_name">Your Name:</label>
        {{ form.name }}
        <br><br>
        <label for="id_email">Your Email:</label>
        {{ form.email }}
        <br><br>
        <label for="id_message">Your Message:</label><br>
        {{ form.message }}
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

#### Create a View

`views.py`
```python
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact  # Import the model where you want to save the data

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Create a new Contact object and save it in the database
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            
            # Redirect after successful form submission
            return redirect('success_page')
    else:
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})
```

#### Summary

This example shows how to create a basic Django form, handle form submissions in a view, and save form data to the database. By following this pattern, you can build more complex forms and handle various types of user input in your Django applications.

### 2. Model Form


This project demonstrates the use of Django's `ModelForm` to create forms that are directly tied to a database model. This approach reduces redundancy and ensures consistency between the model and the form.

## Types of Django Forms

### 2. ModelForm
- Used for creating forms directly tied to a model.
- Automatically includes form fields that match the model fields.
- Simplifies saving data to the database.

### Example

#### Create a Model

`models.py`
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

#### Create a ModelForm

`forms.py`
```python
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
```

#### Create a Template to Render the Form

`add_book.html`
```html
<!-- add_book.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Add a New Book</title>
</head>
<body>
    <h1>Add a New Book</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

#### Create a View

`views.py`
```python
from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Adjust this to wherever you want to redirect after saving
    else:
        form = BookForm()
    
    return render(request, 'add_book.html', {'form': form})
```

### Explanation

1. **ModelForm**:
   - **`forms.ModelForm`**: This defines a form class in Django that is directly tied to a model.
   - **`class Meta`**: This inner class is used to specify the model to which the form is tied and the fields to include in the form.

2. **Template**:
   - **`{{ form.as_p }}`**: This renders the form fields as HTML `<p>` elements.

3. **View**:
   - Handles form submission and validation.
   - Saves the form data to the database if the form is valid.

#### Summary

This example shows how to create a `ModelForm` in Django, handle form submissions in a view, and save form data to the database. Using `ModelForm` reduces redundancy and ensures consistency between the model and the form, making it easier to maintain your code. By following this pattern, you can efficiently create and handle forms that are tightly coupled with your Django models.

## Database Configuration
- **SQLite** is the default database used in Django projects.
- **Advantages of SQLite**:
  - Zero configuration needed.
  - Suitable for small projects or rapid prototyping.
  - Does not run as a server process.
  - No need for additional configuration files.

### When to Use More Scalable Databases
- **Need for scalable databases**: As projects grow or move to production, a more robust database might be needed.
- **Commonly used databases with Django**:
  - PostgreSQL
  - MySQL
  - MariaDB
  - Oracle
  - SQLite

### Configuring MySQL in Django
- **Database Connection Parameters**:
  - Address of the MySQL database.
  - Port number.
  - Database name.
  - Database driver (MySQL client).
- **Installation**: MySQL client needs to be installed.
  ```sh
  pip3 install mysqlclient
  ```
  Change the config in databases in `settings.py`
  ```python
  DATABASES = {
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'k21bp',   # database name
        'USER': 'root',   
        'PASSWORD': '@Sachin3214mysql',   # database password
        'HOST': '127.0.0.1',   
        'PORT': '3306',   
        'OPTIONS': {   
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"   
        }   
     }  
  }
  ```

  
  