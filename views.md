# Views 
## Views in Django

![alt text](/assets/image.png)

`Views` take a request and return a response.

The `views` play a pivotal role in Django's MVT architecture. On one side, Django's URL dispatcher invokes a corresponding view function that matches the URL pattern.

On the other side, the `view` interacts with both `model` and `template` layers.

Django supports several types of views to handle various aspects of web requests and responses. Here are the main types of views in Django with examples:

1. **Function-Based Views (FBV)**
2. **Class-Based Views (CBV)**
3. **Generic Class-Based Views (GCBV)**

### 1. Functions Based Views

   **View rendering template (App)**
   ```python
    from django.shortcuts import render

    def myview(request):

        if request.method=='GET':
        # perform read or delete operation on the model. 

        if request.method=='POST':
        # perform insert or update operation on the model. 
        context={} # dict containing data to be sent to the client. 
    
    return render(request,'mytemplate.html',context)
   ```
   
   Creating a `view function` is not enough to make `request` and `response` work. `View function` needs to be `mapped` to a `Url`, so when the `request` to the `url` is made, the `view function` gets called.

   ***Routing*** : This process of mapping url with view function is known as routing.

   **Url Mapping (App)**
   ```python
   from django.urls import path
   from . import views

   urlpatterns=[
      path('', views.myview ),
   ]
   ```
   Since the `web browser` is the `client` of your web application, the `response` should be in html format as a `web page`, called a `web template`.

   The Django view loads the template web page, insert certain context data at the placeholders marked with tags, and return it as the response.


### 2. Class-Based Views (CBV)

Class-based views provide a more object-oriented approach to handling requests. They allow you to reuse common patterns and can be more powerful and flexible than function-based views.

**Example of a Class-Based View:**

```python
# views.py
from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, world! This is a class-based view.")
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
```

### 3. Generic Class-Based Views (GCBV)

Generic class-based views are built-in views provided by Django to perform common tasks. They are highly reusable and follow DRY (Don't Repeat Yourself) principles. Some common generic views are `TemplateView`, `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`.

**Example of a Generic ListView and DetailView:**

First, create a simple `Book` model.

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

Django's generic class-based views (GCBVs) like `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView` help you quickly implement common patterns for views. Here’s how they work and how you can use them in your project:

#### 1. ListView

`ListView` displays a list of objects from the database. It’s used to show multiple instances of a model in a single view.

**Example:**

```python
# views.py
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'  # Default is 'object_list'
```

**Template: `book_list.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Book List</title>
</head>
<body>
    <h1>Book List</h1>
    <ul>
        {% for book in books %}
            <li><a href="{% url 'book_detail' book.pk %}">{{ book.title }}</a> by {{ book.author }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
]
```

#### 2. DetailView

`DetailView` displays a single object from the database. It’s used to show the details of one instance of a model.

The Url pattern for a `DetailView` includes a parameter key (`pk`) which is used to retrieve the specific object from the database.

`<int:pk>/` is a path converter that captures the primary key of the book from the URL and passes it to the view as an integer.

**Example:**

```python
# views.py
from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'  # Default is 'object'
```

**Template: `book_detail.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ book.title }}</title>
</head>
<body>
    <h1>{{ book.title }}</h1>
    <p>Author: {{ book.author }}</p>
    <p>Published Date: {{ book.published_date }}</p>
</body>
</html>
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
```

#### 3. CreateView

`CreateView` allows users to create a new instance of a model via a form.

**Example:**

```python
# views.py
from django.views.generic import CreateView
from .models import Book
from django.urls import reverse_lazy

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date']
    success_url = reverse_lazy('book_list')
```

**Template: `book_form.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Add a new book</title>
</head>
<body>
    <h1>Add a new book</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import BookCreateView

urlpatterns = [
    path('books/new/', BookCreateView.as_view(), name='book_create'),
]
```

#### 4. UpdateView

`UpdateView` allows users to update an existing instance of a model via a form.

**Example:**

```python
# views.py
from django.views.generic import UpdateView
from .models import Book
from django.urls import reverse_lazy

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date']
    success_url = reverse_lazy('book_list')
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import BookUpdateView

urlpatterns = [
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
]
```

#### 5. DeleteView

`DeleteView` allows users to delete an existing instance of a model.

**Example:**

```python
# views.py
from django.views.generic import DeleteView
from .models import Book
from django.urls import reverse_lazy

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
```

**Template: `book_confirm_delete.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Delete Book</title>
</head>
<body>
    <h1>Are you sure you want to delete "{{ book.title }}"?</h1>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, delete</button>
    </form>
    <a href="{% url 'book_list' %}">Cancel</a>
</body>
</html>
```

**URL Configuration:**

```python
# urls.py
from django.urls import path
from .views import BookDeleteView

urlpatterns = [
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
```

#### Summary

- **ListView**: Used to display a list of objects.
- **DetailView**: Used to display a single object in detail.
- **CreateView**: Used to create a new object.
- **UpdateView**: Used to update an existing object.
- **DeleteView**: Used to delete an existing object.

These generic views help to reduce boilerplate code and provide a consistent way to handle common tasks in web applications.



### Summary

- **Function-Based Views (FBV)** are simple functions that handle requests and return responses.
- **Class-Based Views (CBV)** are more flexible and reusable, providing an object-oriented approach.
- **Generic Class-Based Views (GCBV)** are built-in views for common tasks, promoting reuse and reducing boilerplate code.

Each type of view has its use cases, and you can choose the one that best fits the needs of your project.