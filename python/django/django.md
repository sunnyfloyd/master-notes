# Django

## Basics

- Create a project in a current directory: ```django-admin startproject project_name```.

- Run development server: ```python manage.py runserver [[server_IP:]port]```.

- Create new application structure in the current directory: ```python manage.py startapp app_name```.

- `python manage.py shell` to invoke Django shell.

- Basic view creation:

```python
# polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

- Create a URLconf in the application directory:

```python
# polls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

- The ```path()``` function is passed four arguments, two required: ```route``` and ```view```, and two optional: ```kwargs```, and ```name```:

  - ```route``` is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches. Patterns don’t search GET and POST parameters, or the domain name.

  - ```view``` - when Django finds a matching pattern, it calls the specified view function with an ```HttpRequest``` object as the first argument and any “captured” values from the route as keyword arguments.

  - ```kwargs``` - arbitrary keyword arguments can be passed in a dictionary to the target view.

  - ```name``` - naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

- To point the root URLconf at the application urls module:

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

- The ```include()``` function allows referencing other URLconfs. Whenever Django encounters ```include()```, it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

## Databases and Models

- By default, the databse configuration in Django uses SQLite. To use another database, install the appropriate database bindings and change the ```ENGINE``` and ```NAME``` keys in the ```DATABASES``` *default* item to match database connection settings. If not using SQLite as a database, additional settings such as ```USER```, ```PASSWORD```, and ```HOST``` must be added.

- ```python manage.py migrate``` command looks at the ```INSTALLED_APPS``` setting and creates any necessary database tables according to the database settings in *mysite/settings.py* file and the database migrations shipped with the app. `migrate` takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

- Models declaration:

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')  # human-readable field name is a first optional argument

    def __str__(self):  # overwritting default object representation
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # each choice is related to a single question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

- `on_delete=models.CASCADE` ensures that all records that reference deleted record from foreign table are also deleted.

- To include the app in the project, we need to add a reference to its configuration class in the ```INSTALLED_APPS``` setting. The ```PollsConfig``` class is in the *polls/apps.py* file, so its dotted path is `polls.apps.PollsConfig`:

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ...
]
```

- By running `python manage.py makemigrations polls`, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

- `python manage.py sqlmigrate polls 0001` to see SQL code that will be run by migration.

- `python manage.py check` to check for any issues with the project.

- Three-step guide to making model changes: changes to models -> `makemigrations` -> `migrate`. The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.

### ORM Methods

- Typical usage of Django ORM:

```python
from polls.models import Choice, Question  # model classes

Question.objects.all()  # returns all records of a table
q = Question(question_text="What's new?", pub_date=timezone.now())  # creates new record
q.save()  # saves (commits) an object into the database
q.id  # accessing object property
Question.objects.filter(id=1)  # using Django's database lookup using keyword argument
Question.objects.filter(question_text__startswith='What')
Question.objects.exclude(question_text__startswith='What')  # alternatively we can exclude items that meet given criteria
Question.objects.get(pk=1)  # Django provides a shortcut for primary-key exact lookups
# so there is no need to use 'first()' method, 'get' will also work if we know
# that value based on which we filter is unique and will return only one object
q.choice_set.all()  # returns all records on the 'many' side related to the object on 'one' side
c = q.choice_set.create(choice_text='Not much', votes=0)  # on 'one' side object creating a record on 'many' side
c.question
q.choice_set.count()  # using 'count' db function
Choice.objects.filter(question__pub_date__year=current_year)  # use double underscores to separate relationships
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()  # deleting single record
Question.objects.order_by('-pub_date')[:5]
Question.objects.filter(pub_date__lte=timezone.now())  # returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
Question.objects.create(question_text=question_text, pub_date=time)
```

- In order to avoid race conditions in Django ORM `F()` can be used:

```python
from django.db.models import F

reporter = Reporters.objects.get(name='Tintin')
reporter.stories_filed = F('stories_filed') + 1
reporter.save()  # addition is performed on DB side rather than in Python
```

- When we want to check whether a single object is present in `ManyToMany` field then just normal equality can be verified `field_name=object` instead of `field_name__in=[object]`.

- `ManyToManyField` can be defined on itself using `self`. This relationship can be made asymetrical which will allow to push reverse relation into a different model field:

```py
class User(AbstractUser):
    following = models.ManyToManyField(
        'self', symmetrical=False, blank=True, related_name='followers')
```

## Django Admin

- `python manage.py createsuperuser` creates a user who can login to the admin site.

## Views

- A **view** is a *type* of Web page in your Django application that generally serves a specific function and has a specific template. In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name). To get from a URL to a view, Django uses what are known as `URLconfs`. A `URLconf` maps URL patterns to views.

- Defining URL patterns:

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

- View needs to return a `HttpResponse` object.

- Project’s `TEMPLATES` setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whose `APP_DIRS` option is set to `True`. By convention `DjangoTemplates` looks for a *templates* subdirectory in each of the `INSTALLED_APPS`.

- Within the templates directory you have just created, create another directory called polls, and within that create a file called *index.html*. In other words, your template should be at *polls/templates/polls/index.html*. Because of how the *app_directories* template loader works as described above, you can refer to this template within Django as *polls/index.html*.

- Rendering a template with variable context (dictionary that maps template variable names to Python objects):

```python
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

- It’s a very common idiom to load a template, fill a context and return an `HttpResponse` object with the result of the rendered template. Django provides a shortcut for this:

```python
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

- The `render()` function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an `HttpResponse` object of the given template rendered with the given context.

- Raising a HTTP 404 error:

```python
from django.shortcuts import render

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

- Shortcut for getting an object or 404:

```python
from django.shortcuts import get_object_or_404

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

- The `get_object_or_404()` function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the `get()` function of the model’s manager. It raises `Http404` if the object doesn’t exist.

- There’s also a `get_list_or_404()` function, which works just as `get_object_or_404()` – except using `filter()` instead of `get()`. It raises `Http404` if the list is empty.

- If you need to use something similar to the `url` template tag in your code, Django provides the following function:

```py
# In URLConf
from news import views
path('archive/', views.archive, name='news-archive')

# using the named URL
reverse('news-archive')

# or by passing a callable object
# (This is discouraged because you can't reverse namespaced views this way.)
from news import views
reverse(views.archive)
```

- `request.POST` is a dictionary-like object that lets one access submitted data by key name. Django provides also `request.GET` method.

- Always return an `HttpResponseRedirect` after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.

### Generic Views

```py
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # This 'overwrites' default 'get_queryset' method in Question class.
        # It first take the normal output from `get_queryset` (Question.objects)
        # and then it filters it with provided criteria.
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
```

- Above example is using two generic views: ```ListView``` and ```DetailView```. Respectively, those two views abstract the concepts of “display a list of objects” and “display a detail page for a particular type of object.”

- Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.

- The DetailView generic view expects the primary key value captured from the URL to be called *pk* so changes in the `urlpatterns` are needed:

```py
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

- By default, the `DetailView` generic view uses a template called `<app name>/<model name>_detail.html`. In this case, it would use the template *polls/question_detail.html*. The `template_name` attribute is used to tell Django to use a specific template name instead of the autogenerated default template name.

- For `DetailView` the question variable is provided automatically – since we’re using a Django model (`Question`), Django is able to determine an appropriate name for the context variable. However, for `ListView`, the automatically generated context variable is `question_list`. To override this we provide the `context_object_name` attribute, specifying that we want to use `latest_question_list` instead.

## Templates

- The template system uses dot-lookup syntax to access variable attributes. In the example of `{{ question.question_text }}`, first Django does a dictionary lookup on the object question. Failing that, it tries an attribute lookup – which works, in this case. If attribute lookup had failed, it would’ve tried a list-index lookup.

```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

- If the name argument is defined in the `path()` functions in the `polls.urls` module, reliance on a specific URL paths defined in url configurations can be removed by using the `{% url %}` template tag.

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
<!-- instead of: -->
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

- To use the same view name in multiple apps namespace should be added to `URLconf`:

```python
# app/urls.py
app_name = 'polls'
```

- Then in templates URLs should be called like this:

```python
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

- `forloop.counter` indicates how many times the `for` tag has gone through its loop:

```html
{% for choice in question.choice_set.all %}
    {{ forloop.counter }}
{% endfor %}
```

- All POST forms that are targeted at internal URLs should use the `{% csrf_token %}` template tag.

## Testing

- It is a good idea to follow a discipline called *test-driven development*. It means that tests are created before any actual code is written. This might seem counter-intuitive, but in fact it’s similar to what most people will often do anyway: they describe a problem, then create some code to solve it. Test-driven development formalizes the problem in a Python test case.

- Redundancy in testing is good. Tests do not need to look aesthetically.

- `python manage.py test app_name` runs tests.

```py
import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

- Test flow in Django: *manage.py* test polls looked for tests in the *polls* application -> found a subclass of the `django.test.TestCase` class -> created a special database for the purpose of testing -> looked for test methods - ones whose names begin with *test*.

- Testing views:

```py
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        # gets view as a response from a server
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )
```

- The database is reset for each test method.

- Rules-of-thumb for testing:
  - a separate TestClass for each model or view
  - a separate test method for each set of conditions you want to test
  - test method names that describe their function.

- We can also create a `setUp` function that will be run before each testing method and prepare a mock objects within a test database:

```py
from django.test import TestCase
from .models import Flight, Airport, Passenger

class FlightTestCase(TestCase):

    def setUp(self):

        # Create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # Create flights.
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())
```

### Client Testing

- Django testing allows us to access views' context:

```py
from django.test import Client, TestCase
from django.db.models import Max

class FlightTestCase(TestCase):

    def test_index(self):

        # Set up client to make requests
        c = Client()

        # Send get request to index page and store response
        response = c.get("/flights/")

        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

        # Make sure three flights are returned in the context (as per setUp method)
        self.assertEqual(response.context["flights"].count(), 3)

    def test_valid_flight_page(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_flight_page(self):
        max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]
        c = Client()
        response = c.get(f"/flights/{max_id + 1}")
        self.assertEqual(response.status_code, 404)
```

### Testing Frontend with Selenium

- Basic operations with Selenium:

```py
import os
import pathlib
import unittest

from selenium import webdriver

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome()

# Standard outline of testing class
class WebpageTests(unittest.TestCase):

    def test_title(self):
        """Make sure title is correct"""
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        """Make sure header updated to 1 after 1 click of increase button"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

if __name__ == "__main__":
    unittest.main()
```

## Static Files

- Django’s `STATICFILES_FINDERS` setting contains a list of finders that know how to discover static files from various sources. One of the defaults is `AppDirectoriesFinder` which looks for a *static* subdirectory in each of the `INSTALLED_APPS`.

## Admin Panel Customization

- If there is a need to customize how the admin form looks and works it can be done by telling Django the options you want when you register the object:

```py
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']  # reordering the fields on the edit form

admin.site.register(Question, QuestionAdmin)
```

- Above workflow applies to all the changes in admin options for a model: create a model admin class -> pass it as the second argument to `admin.site.register()`.

## Forms

- Creating a new form is based on the `forms.Form` class:

```python
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')
    priority = forms.IntegerField(label='Priority', min_value=1, max_value=10)
```

- Server-side validation can be implemented by verifying request method and then populating the form instance with data from the request:

```python
from django.http import HttpResponseRedirect
from django.url import reverse

tasks = []

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)  # populates form with data from POST
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            return HtttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {
                'form': form
            })  # returning incorrectly populated form instead of a blank one

    return render(request, 'tasks/add.html', {
        'form': NewTaskForm()
    })
```

## Session Management

- Data can be stored in client session (first `python manage.py migrate` needs to be run to create all of the default tables inside a Django database):

```python
def add(request):
    if 'tasks' not in request.session:
        request.session['tasks'] += [task]
```

## React + Django (Architecture and Deployment)

### Frontend and Backend Architectures

There are 4 main architectures that can be applied to separete frontend and backend:

1. Running the frontend and the backend on distinct origins (frontend: app.example.com. tha makes cross-origin API requests to api.example.com). Most Single-Page Apps (SPA) use this architecture.

2. Making the backend serve static files for the frontend. This is Django’s default behavior in development: `runserver` serves static assets with a WSGI middleware provided by the staticfiles app. WhiteNoise provides a production-ready implementation of that behavior.

3. Making the frontend proxy API requests to the backend. Traditional production deployments of Django use this architecture. With Apache and mod_wsgi, Apache serves static files and proxies other requests to mod_wsgi. With nginx and a WSGI server such as gunicorn, uWSGI, or waitress, nginx serves static files and proxies other requests to the application server.

4. Dispatching frontend and backend requests with a reverse proxy. This setup is less common. It happens when a CDN (e.g. CloudFront) serves static assets from an object storage (e.g. S3) and forwards other requests to an application server. For practical purposes, it doesn’t matter very much how static files are served, so options 3 and 4 are equivalent.

- 1 - is called a **single page app model** and 2, 3, 4 are called **hybrid app models**.

- The “single page app” model requires setting up CORS because the frontend and the backend run on separate domains. This is easily achieved with [django-cors-headers](https://github.com/adamchainz/django-cors-headers) and the following settings::

```python
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ['https://app.example.com']
```

- It’s hard to quantify how client-side rendering affects search ranking compared to traditional server-side rendering but it’s almost certainly a loss. Experiments show that the crawl frequency is lower. Regular HTML pages are a safer bet for the time being when SEO is a concern.

### Authentication

- There are two mainstream mechanisms for authenticating users: **cookies** and **JWTs**.

- By default, Django’s user authentication system relies on cookie-based sessions.

- Since JWTs are managed at the application level, each application must implement storage, expiry and renewal of JWTs. This is a significant, security-sensitive responsibility.
