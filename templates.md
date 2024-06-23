# Templates
## Templates in Django

`Templates` are text-based documents or Python strings marked up using `Django Template Language` known as `DTL`. 

Django's template system is designed to separate the presentation of a web page from its content. Here's a detailed overview of Django templates with code examples:

### Key Features of Django Templates

1. **Separation of Concerns**: Templates focus on the presentation layer, while views and models handle the business logic and data.
2. **Template Language**: A Django template is a text file that can generate any text-based format (HTML, XML, CSV, etc.).
3. **Template Tags and Filters**: Django templates use tags and filters to provide dynamic behavior.

### Creating a Django Template

### 1. Define a Template

Templates are usually stored in a `templates` directory within your app or project. For example, create `index.html`:

`templates/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to {{ title }}</h1>
    <p>This is a simple example of a Django template.</p>

    <h2>Authors List</h2>
    <ul>
        {% for author in authors %}
            <li>{{ author }}</li>
        {% empty %}
            <li>No authors found.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### 2. Configure Template Directory

Ensure your settings.py is configured to find the templates directory.

`settings.py`
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 3. Create a View

Create a view that renders the template and passes context data.

`views.py`
```python
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Django Template Example',
        'authors': ['Author 1', 'Author 2', 'Author 3']
    }
    return render(request, 'index.html', context)
```

### 4. Map the View to a URL

Configure the URL to point to the view.

`urls.py`
```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
```

### Template Tags and Filters

Django templates use tags and filters to add logic and formatting.

#### Common Template Tags

- `{% for %}`: Loop over a sequence.
- `{% if %}`: Conditional statements.
- `{% block %}`: Define a block that child templates can override.
- `{% extends %}`: Inherit from another template.

#### Common Template Filters

- `{{ variable|length }}`: Return the length of the variable.
- `{{ variable|upper }}`: Convert the variable to uppercase.
- `{{ variable|date:"D d M Y" }}`: Format a date.

### Example with Tags and Filters

Here's an enhanced example using more tags and filters:

`templates/author_list.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Authors</title>
</head>
<body>
    <h1>Authors List</h1>
    <ul>
        {% for author in authors %}
            <li>{{ author.name|upper }} - Joined on {{ author.join_date|date:"D d M Y" }}</li>
        {% empty %}
            <li>No authors found.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### View with Enhanced Context

`views.py`
```python
from django.shortcuts import render

def author_list(request):
    authors = [
        {'name': 'Author 1', 'join_date': '2023-01-01'},
        {'name': 'Author 2', 'join_date': '2023-02-15'},
        {'name': 'Author 3', 'join_date': '2023-03-22'},
    ]
    return render(request, 'author_list.html', {'authors': authors})
```

### Using Template Inheritance

Django supports template inheritance, allowing you to create a base template and extend it in other templates.

`templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Site</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about/">About</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 My Site</p>
    </footer>
</body>
</html>
```

`templates/index.html`
```html
{% extends "base.html" %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
    <h2>Welcome to My Site</h2>
    <p>This is the home page.</p>
{% endblock %}
```

### Conclusion

Django templates provide a powerful way to separate content from presentation, use reusable components, and add dynamic behavior to your web pages. By using template tags, filters, and inheritance, you can create flexible and maintainable templates for your Django applications.
