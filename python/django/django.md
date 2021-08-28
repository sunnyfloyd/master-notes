# Django

## Table of Contents

- [Django](#django)
  - [Table of Contents](#table-of-contents)
  - [Sources](#sources)
  - [Basics](#basics)
  - [Models](#models)
    - [Creating Model Managers](#creating-model-managers)
  - [Databases and ORMs](#databases-and-orms)
    - [ORM Methods](#orm-methods)
      - [QuerySet API](#queryset-api)
        - [annotate](#annotate)
        - [values_list](#values_list)
  - [Admin Panel and Customization](#admin-panel-and-customization)
  - [Views](#views)
    - [URLs](#urls)
    - [Templates](#templates)
      - [Custom Template Tags](#custom-template-tags)
      - [Filters](#filters)
      - [Custom Template Filters](#custom-template-filters)
      - [Pagination](#pagination)
    - [Generic Views](#generic-views)
      - [Generic Views (from Django tutorial)](#generic-views-from-django-tutorial)
  - [Templates](#templates-1)
  - [Testing](#testing)
    - [Client Testing](#client-testing)
    - [Testing Frontend with Selenium](#testing-frontend-with-selenium)
  - [Forms](#forms)
    - [Form Class Forms](#form-class-forms)
    - [ModelForm Class Forms](#modelform-class-forms)
  - [Session Management](#session-management)
  - [Static Files](#static-files)
  - [Utilities](#utilities)
    - [Sending Emails](#sending-emails)
    - [Absolute URI](#absolute-uri)
    - [Taggit](#taggit)
    - [Sitemaps](#sitemaps)
    - [Content Feed (RSS)](#content-feed-rss)
  - [This is a post formatted with markdown](#this-is-a-post-formatted-with-markdown)
- [Application definition](#application-definition)

## Sources

- [Django Official Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- [CS50 Harvard Course](https://cs50.harvard.edu/web/2020/weeks/3/)
- [Django 3 By Example - Third Edition](https://learning.oreilly.com/library/view/django-3-by/9781838981952/)

## Basics

- Create a project in a current directory: ```django-admin startproject project_name```.

- Run development server: ```python manage.py runserver [[server_IP:]port]```.

- You can run the Django development server on a custom host and port or tell Django to load a specific settings file, as follows: `python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings`.

- Create new application structure in the current directory: ```python manage.py startapp app_name```.

- To include the app in the project, we need to add a reference to its configuration class in the ```INSTALLED_APPS``` setting. The ```PollsConfig``` class is in the *polls/apps.py* file, so its dotted path is `polls.apps.PollsConfig`. The `PollsConfig` class is your application configuration. When added to the `INSTALLED_APPS` Django knows that your application is active for this project and will be able to load its models.

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ...
]
```

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

## Models

- [Models API reference](https://docs.djangoproject.com/en/3.0/ref/models/)

- **Model** is a Python class that subclasses `django.db.models.Model` in which each attribute represents a database field. Django will create a table for each model defined in the `models.py` file. When you create a model, Django will provide you with a practical API to query objects in the database easily.

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

- `on_delete=models.CASCADE` ensures that all records that reference deleted record from foreign table are also deleted. The behaviour can be altered based on the passed argument like `models.PROTECT`. [Full list of arguments that can be passed to `on_delete`](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete).

- If you do not define the `related_name` attribute in relationship model fields, Django will use the name of the model in lowercase, followed by _set (that is, modelname_set) to name the relationship of the related object to the object of the model, where this relationship has been defined.

- `auto_now_add` and `auto_now` are mutually exclusive: former one adds a date to the field during object creation, whereas the latter updates it every time the `save()` method is called.

- Model class can also include `Meta` class that might alter some default behaviours like default ordering or default table name:

```py
class Post (models.Model)
    ...

    class Meta:
        db_table = 'table_name'  # default name is converted from camel case to snake case
        ordering = ('-publish',)
```

- Django creates a primary key automatically for each model, but you can also override this by specifying primary_key=True in one of your model fields. The default primary key is an id column, which consists of an integer that is incremented automatically. This column corresponds to the id field that is automatically added to your models.

### Creating Model Managers

- `objects` is the default manager of every model that retrieves all objects in the database. However, you can also define custom managers for your models. There are **two ways to add or customize managers** for your models:
  - add extra manager methods to an existing manager: `Post.objects.my_manager()`
  - create a new manager by modifying the initial `QuerySet` that the manager returns: `Post.my_manager.all()`:

```py
# creating a new manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')

class Post(models.Model):
    # ...
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
```

- The first manager declared in a model becomes the default manager. You can use the `Meta` attribute `default_manager_name` to specify a different default manager. If no manager is defined in the model, Django automatically creates the `objects` default manager for it. If you declare any managers for your model but you want to keep the `objects` manager as well, you have to add it explicitly to your model.

- The `get_queryset()` method of a manager returns the `QuerySet` that will be executed.

## Databases and ORMs

- By running `python manage.py makemigrations polls`, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

- ```python manage.py migrate``` command looks at the ```INSTALLED_APPS``` setting and creates any necessary database tables according to the database settings in *mysite/settings.py* file and the database migrations shipped with the app. `migrate` takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

- `python manage.py sqlmigrate polls 0001` to see SQL code that will be run by migration.

- `python manage.py check` to check for any issues with the project.

- Three-step guide to making model changes: changes to models -> `makemigrations` -> `migrate`. The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.

- By default, the databse configuration in Django uses SQLite. To use another database, install the appropriate database bindings and change the ```ENGINE``` and ```NAME``` keys in the ```DATABASES``` *default* item to match database connection settings. If not using SQLite as a database, additional settings such as ```USER```, ```PASSWORD```, and ```HOST``` must be added.

### ORM Methods

- Examples of Django ORM methods:

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
Post.objects.filter(publish__year=2020, author__username='admin')
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()  # deleting single record
Question.objects.order_by('-pub_date')[:5]
Question.objects.filter(pub_date__lte=timezone.now())  # returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
Question.objects.create(question_text=question_text, pub_date=time)
```

- The changes you make to the object are not persisted to the database until you call the `save()` method. This is due to the fact that object creation first happens in the memory. You can also create the object and persist it into the database in a single operation using the `create()` method: `Post.objects.create(title='post title')`.

- Each Django model has at least one manager, and the default manager is called **objects**. You get a `QuerySet` object using your model manager. To retrieve all objects from a table, you just use the `all()` method on the default objects manager.

- Django `QuerySets` are **lazy**, which means they are only evaluated when they are forced to be. `QuerySets` are only evaluated in the following cases:

  - The first time you iterate over them
  - When you slice them, for instance, `Post.objects.all()[:3]`
  - When you pickle or cache them
  - When you call `repr()` or `len()` on them
  - When you explicitly call `list()` on them
  - When you test them in a statement, such as `bool()`, `or`, `and`, or `if`.


- To filter a `QuerySet`, you can use the `filter()` method of the manager.

- Queries with field lookup methods are built using two underscores, for example, `publish__year`, but the same notation is also used for accessing fields of related models, such as `author__username`.

```py
Post.objects.filter(publish__year=2020, author__username='admin')
Post.objects.filter(publish__year=2020) \
            .filter(author__username='admin'
```

- You can exclude certain results from your QuerySet using the `exclude()` method of the manager. For example, you can retrieve all posts published in 2020 whose titles don't start with *Why*: `Post.objects.filter(publish__year=2020).exclude(title__startswith='Why')`.

- If you want to delete an object, you can do it from the object instance using the `delete()` method.

- Shortcut for getting an object or 404:

```python
from django.shortcuts import get_object_or_404

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

- The `get_object_or_404()` function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the `get()` function of the model’s manager. It raises `Http404` if the object doesn’t exist.

- There’s also a `get_list_or_404()` function, which works just as `get_object_or_404()` – except using `filter()` instead of `get()`. It raises `Http404` if the list is empty.

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

#### QuerySet API

##### annotate

- [Aggregation functions in Django](https://docs.djangoproject.com/en/3.0/topics/db/aggregation/)

- Per-object summaries can be generated using the `annotate()` clause. When an `annotate()` clause is specified, each object in the QuerySet will be annotated with the specified values. It basically means to run certain aggreagation function (like `Count()`) for specified field from the QuerySet (object) and return a new QuerySet with additional field.

- As with `aggregate()`, the name for the annotation is automatically derived from the name of the aggregate function and the name of the field being aggregated. You can override this default name by providing an alias when you specify the annotation.

- Unlike `aggregate()`, `annotate()` is not a terminal clause. The output of the `annotate()` clause is a QuerySet; this QuerySet can be modified using any other QuerySet operation, including `filter()`, `order_by()`, or even additional calls to `annotate()`.

```py
# Build an annotated queryset
from django.db.models import Count
q = Book.objects.annotate(Count('authors'))
# Interrogate the first object in the queryset
q[0]
# <Book: The Definitive Guide to Django>
q[0].authors__count
# 2
# Interrogate the second object in the queryset
q[1]
# <Book: Practical Django Projects>
q[1].authors__count
#1

q = Book.objects.annotate(num_authors=Count('authors'))
q[0].num_authors
# 2
q[1].num_authors
# 1
```

##### values_list

- This is similar to `values()` except that instead of returning dictionaries, it returns tuples when iterated over. Each tuple contains the value from the respective field or expression passed into the `values_list()` call — so the first item is the first field, etc. You can pass `flat=True` to it to get single values such as `[1, 2, 3, ...]` instead of one-tuples such as `[(1,), (2,), (3,) ...]`:

```py
Entry.objects.values_list('id', 'headline')
# <QuerySet [(1, 'First entry'), ...]>
from django.db.models.functions import Lower
Entry.objects.values_list('id', Lower('headline'))
# <QuerySet [(1, 'first entry'), ...]>
```

- If returned value is a flat list it can be then used further in look up methods:

```py
post_tags_ids = post.tags.values_list('id', flat=True)
# <QuerySet [2, 3, 6, 7, 8, 9]>
similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                .exclude(id=post.id)
```

## Admin Panel and Customization

- `python manage.py createsuperuser` creates a user who can login to the admin site.

- Registering django models in admin module:

```python
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```

- If there is a need to customize how the admin form looks and works it can be done by telling Django the options you want when you register the object:

```py
from django.contrib import admin
from .models import Post

@admin.register(Post)  # replaces admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
```

- Above workflow applies to all the changes in admin options for a model: create a model admin class -> pass it as the second argument to `admin.site.register()`.

## Views

- A **view** is a *type* of Web page in your Django application that generally serves a specific function and has a specific template. In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name). To get from a URL to a view, Django uses what are known as `URLconfs`. A `URLconf` maps URL patterns to views.

- View needs to return a `HttpResponse` object.

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

- If you need to use something similar to the `url` template tag in your code, Django provides the following `reverse` function:

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

- The `reverse_lazy()` utility function is a lazily evaluated version of `reverse()`. It allows you to use a URL reversal before the project's URL configuration is loaded.

- `request.POST` is a dictionary-like object that lets one access submitted data by key name. Django provides also `request.GET` method.

- Always return an `HttpResponseRedirect` after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.

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

### URLs

- You use angle brackets to capture the values from the URL. Any value specified in the URL pattern as `<parameter>` is captured as a string. You use path converters, such as `<int:year>`, to specifically match and return an integer. [All path converters in Django docs](https://docs.djangoproject.com/en/3.0/topics/http/urls/#path-converters).

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

- If using `path()` and converters isn't sufficient, you can use `re_path()` instead to define complex URL patterns with [Python regular expressions](https://docs.djangoproject.com/en/3.0/ref/urls/#django.urls.re_path).

- Including the URL patterns of the application in the main URL patterns of the project:

```py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
```

- Each application should define its own namespace via `app_name` variable inside `urls.py`. Thanks to it, application URLs can be accessed with `namespace:view_name` syntax. [URL utility function in Django docs](https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces).

- A **canonical URL** is the preferred URL for a resource. You may have different pages in your site where you display given objects, but there is a single URL that you use as the main URL for a model object. The convention in Django is to add a `get_absolute_url()` method to the model that returns the canonical URL for the object:

```py
from django.urls import reverse
class Post(models.Model):
    # ...
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])

# In template we can then use:
{% for post in posts %}
    <h2>
    <a href="{{ post.get_absolute_url }}">
        {{ post.title }}
    </a>
{% endfor %}
```

### Templates

- [Django docs on templates](https://docs.djangoproject.com/en/3.0/ref/templates/language/).

- [Django built-in template tags and filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)

- Django has a powerful template language that allows you to specify how data is displayed. It is based on template tags, template variables, and template filters:

    - Template tags control the rendering of the template and look like `{% tag %}`
    - Template variables get replaced with values when the template is rendered look like `{{ variable }}`
    - Template filters allow you to modify variables for display and look like `|filter }}`.
    - 
- Django template language doesn't use parentheses for calling methods.

- Project’s `TEMPLATES` setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whose `APP_DIRS` option is set to `True`. By convention `DjangoTemplates` looks for a *templates* subdirectory in each of the `INSTALLED_APPS`.

- Within the templates directory you have just created, create another directory called polls, and within that create a file called *index.html*. In other words, your template should be at *polls/templates/polls/index.html*. Because of how the *app_directories* template loader works as described above, you can refer to this template within Django as *polls/index.html*.

- The `{% with %}` tag allows you to assign a value to a new variable that will be available to be used until the `{% endwith %}` tag. The `{% with %}` template tag is useful for avoiding hitting the database or accessing expensive methods multiple times.

- To store the result in a custom variable use the `as` argument followed by the variable name: `{% template_tag_function as variable_name %}`.

#### Custom Template Tags

- [Custom template tags in Django](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)

- Creating custom tags is useful when we do not want to bloat the view's context with variables that might be used across different views.

- Django provides the following helper functions that allow you to create your own template tags in an easy manner:

  - `simple_tag`: Processes the data and returns a string
  - `inclusion_tag`: Processes the data and returns a rendered template

- Template tags must live inside Django applications.

- Flow for creating new template tags:

  - create new package within the application by adding new folder with *__init__.py* in it
  - create new python file with meaningful name that will later be used to access custom tags
  - add code to the created python file:

```py
from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()
```

- Django uses the function's name as the tag name, but custom name can be defined with `@register.simple_tag(name='my_tag')`.

- Before using custom template tags, you have to make them available for the template using the `{% load file_name %}` tag.

- **Inclusion tags** registration includes path to the template that will be renders: `@register.inclusion_tag('path/to/html_file.html')`. Inclusion tags have to return a dictionary of values instead of a simple value - it will be used as the context to render the specified template. The template tag can also allow to specify an argument (that can also be optioanl): {% show_latest_posts 3 %}.

#### Filters

- [Built-in template filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-filter-reference)

- Filters can be used outside of the templates as well. Default filters can be imported from `django.template.defaultfilters`.

- Django has a variety of built-in template filters that allow you to alter variables in templates. These are Python functions that take one or two parameters, the value of the variable that the filter is applied to, and an optional argument. They return a value that can be displayed or treated by another filter. A filter looks like `{{ variable|my_filter }}`. Filters with an argument look like `{{ variable|my_filter:"foo" }}`.

- You can apply as many filters as you like to a variable, for example, `{{ variable|filter1|filter2 }}`, and each of them will be applied to the output generated by the preceding filter.

- Example of template filters:

  - `truncatewords` truncates the value to the number of words specified
  - `linebreaks` converts the output into HTML line breaks
  - `pluralize` displays a plural suffix for the given word
  - `join` works the same as the Python string `join()` method concatenating elements from iterable

#### Custom Template Filters

- You register template filters in the same way as template tags:

```py
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
```

#### Pagination

- Django has a built-in pagination class that allows you to manage paginated data easily:

```py
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                   {'page': page,
                    'posts': posts})
```

- This is how pagination works:

    - You instantiate the `Paginator` class with the number of objects that you want to display on each page.
    - You get the page `GET` parameter, which indicates the current page number.
    - You obtain the objects for the desired page by calling the `page()` method of Paginator.
    - If the page parameter is not an integer, you retrieve the first page of results. If this parameter is a number higher than the last page of results, you retrieve the last page.
    - You pass the page number and retrieved objects to the template.

- Template application of Django pagination:

```py
<div class="pagination">
  <span class="step-links">
    {% if page.has_previous %}
      <a href="?page={{ page.previous_page_number }}">Previous</a>
    {% endif %}
    <span class="current">
      Page {{ page.number }} of {{ page.paginator.num_pages }}.
    </span>
    {% if page.has_next %}
      <a href="?page={{ page.next_page_number }}">Next</a>
    {% endif %}
  </span>
</div>
```

- Since the `Page` object you are passing to the template is called `posts`, you include the pagination template in the post list template, passing the parameters to render it correctly. You can follow this method to reuse your pagination template in the paginated views of different models:

```py
# `posts` object will be accessible in pagination snippet via `page` variable/argument
{% include "pagination.html" with page=posts %}
```

### Generic Views

- **Class-based** views are an alternative way to implement views as Python objects instead of functions. Since a view is a callable that takes a web request and returns a web response, you can also define your views as class methods. Django provides base view classes for this. All of them inherit from the View class, which handles HTTP method dispatching and other common functionalities.

- Class-based views offer advantages over function-based views for some use cases. They have the following features:

    - Organizing code related to HTTP methods, such as `GET`, `POST`, or `PUT`, in separate methods, instead of using conditional branching
    - Using multiple inheritance to create reusable view classes (also known as *mixins*)

- Class-based view is analogous to the previous `post_list` view. In the code below you are telling `ListView` to do the following things:

    - Use a specific QuerySet instead of retrieving all objects. Instead of defining a `queryset` attribute, you could have specified `model = Post` and Django would have built the generic `Post.objects.all()` QuerySet for you.
    - Use the context variable posts for the query results. The default variable is `object_list` if you don't specify any `context_object_name`.
    - Paginate the result, displaying three objects per page.
    - Use a custom template to render the page. If you don't set a default template, ListView will use blog/post_list.html.

```py
# views.py
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# urls.py
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
]

# list.html
{% include "pagination.html" with page=page_obj %}
```

#### Generic Views (from Django tutorial)

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

## Forms

Django comes with two base classes to build forms:

  - Form: Allows you to build standard forms
  - ModelForm: Allows you to build forms tied to model instances

- Forms can reside anywhere in your Django project. The convention is to place them inside a *forms.py* file for each application.

- [List of available form fields](https://docs.djangoproject.com/en/3.0/ref/forms/fields/)

### Form Class Forms

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

- You can see a list of validation errors by accessing `form.errors`.

- If the form is valid, you retrieve the validated data by accessing `form.cleaned_data`. If your form data does not validate, `cleaned_data` will contain only the valid fields.

- To put a form inside a template tou tell Django to render its fields in HTML paragraph `<p>` elements with the `as_p` method. You can also render the form as an unordered list with `as_ul` or as an HTML table with `as_table`. If you want to render each field, you can iterate through the fields, instead of using `{{ form.as_p }}`.

```HTML
<form method="post">
    {{ form.as_p }}
    {% csrf_token %}
    <input type="submit" value="Send e-mail">
</form>

<!-- iterating through form fields instead -->
{% for field in form %}
  <div>
    {{ field.errors }}
    {{ field.label_tag }} {{ field }}
  </div>
{% endfor %}
```

- The `{% csrf_token %}` template tag introduces a hidden field with an autogenerated token to avoid cross-site request forgery (CSRF) attacks. These attacks consist of a malicious website or program performing an unwanted action for a user on your site. By default, **Django checks for the CSRF token in all POST requests**. Remember to include the csrf_token tag in all forms that are submitted via POST.

### ModelForm Class Forms

- To create a form from a model, you just need to indicate which model to use to build the form in the `Meta` class of the form. Django introspects the model and builds the form dynamically for you.

- Each model field type has a corresponding default form field type. The way that you define your model fields is taken into account for form validation. By default, Django builds a form field for each field contained in the model. However, you can explicitly tell the framework which fields you want to include in your form using a `fields` list, or define which fields you want to exclude using an `exclude` list of fields:

```py
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
```

- `save()` method in `ModelForm` class creates an instance of the model that the form is linked to and saves it to the database. If you call it using `commit=False`, you create the model instance, but don't save it to the database yet. This comes in handy when you want to modify the object before finally saving it, which is what you will do next. The `save()` method is available for ModelForm but not for `Form` instances, since they are not linked to any model.

## Session Management

- Data can be stored in client session (first `python manage.py migrate` needs to be run to create all of the default tables inside a Django database):

```python
def add(request):
    if 'tasks' not in request.session:
        request.session['tasks'] += [task]
```

## Static Files

- Django’s `STATICFILES_FINDERS` setting contains a list of finders that know how to discover static files from various sources. One of the defaults is `AppDirectoriesFinder` which looks for a *static* subdirectory in each of the `INSTALLED_APPS`.

## Utilities

### Sending Emails

- To send emails with Django you need to define the configuration of an external SMTP server by adding the following settings to the *settings.py* file of your project:

  - `EMAIL_HOST`: The SMTP server host; the default is localhost
  - `EMAIL_PORT`: The SMTP port; the default is 25
  - `EMAIL_HOST_USER`: The username for the SMTP server
  - `EMAIL_HOST_PASSWORD`: The password for the SMTP server
  - `EMAIL_USE_TLS`: Whether to use a Transport Layer Security (TLS) secure connection
  - `EMAIL_USE_SSL`: Whether to use an implicit TLS secure connection

- If you can't use an SMTP server, you can tell Django to write emails to the console by adding the following setting to the *settings.py* file:

```py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

- The following sample configuration is valid for sending emails via Gmail servers using a Google account. Additionaly [captha might need to be disabled](https://accounts.google.com/displayunlockcaptcha) and [access for less secure applications needs to be enabled](https://myaccount.google.com/lesssecureapps):

```py
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

- `send_mail()` function takes the subject, message, sender, and list of recipients as required arguments. By setting the optional argument fail_silently=False, you are telling it to raise an exception if the email couldn't be sent correctly. If the output you see is 1, then your email was successfully sent.

### Absolute URI

- `HttpRequest.build_absolute_uri` returns the absolute URI form of location. If no location is provided, the location will be set to `request.get_full_path()`. If the location is already an absolute URI, it will not be altered. Otherwise the absolute URI is built using the server variables available in this request. For example:

```py
request.build_absolute_uri()
# 'https://example.com/music/bands/the_beatles/?print=true'
request.build_absolute_uri('/bands/')
# 'https://example.com/bands/'
request.build_absolute_uri('https://example2.com/bands/')
# 'https://example2.com/bands/'
```

### Taggit

- [**Django Taggit**](https://github.com/jazzband/django-taggit) provides tagging functionality into Django Models.

### Sitemaps

- [Sitemap Framework](https://docs.djangoproject.com/en/3.0/ref/contrib/sitemaps/)

- Django comes with a sitemap framework, which allows you to generate sitemaps for your site dynamically. A sitemap is an XML file that tells search engines the pages of your website, their relevance, and how frequently they are updated. Using a sitemap will make your site more visible in search engine rankings: sitemaps help crawlers to index your website's content.

- The Django sitemap framework depends on `django.contrib.sites`, which allows you to associate objects to particular websites that are running with your project. This comes in handy when you want to run multiple sites using a single Django project. To install the sitemap framework, you will need to activate both the `sites` and the `sitemap` applications in your project.

- In *settings.py* add below and run `python manage.py migrate`:

```py
SITE_ID = 1
# Application definition
INSTALLED_APPS = [
    # ...
    'django.contrib.sites',
    'django.contrib.sitemaps',
]
```

- You create a custom sitemap by inheriting the `Sitemap` class of the `sitemaps` module. The `changefreq` and `priority` attributes indicate the change frequency of your post pages and their relevance in your website (the maximum value is 1).

- The `items()` method returns the QuerySet of objects to include in this sitemap. By default, Django calls the `get_absolute_url()` method on each object to retrieve its URL. If you want to specify the URL for each object, you can add a `location` method to your sitemap class.

- The `lastmod` method receives each object returned by items() and returns the last time the object was modified.
- 
- Above can be done inside desired application within the *sitemaps.py* file. This code basically indicates method for retrieving all objects that should constitute a sitemap and on each `get_absolute_url()` method is called to obtain valid URL:

```py
from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Post.published.all()
    def lastmod(self, obj):
        return obj.updated
```

- Finally, add your sitemap URL by editing the main *urls.py* file of your project and add the sitemap. Add the required imports and define a dictionary of sitemaps.  Define a URL pattern that matches *sitemap.xml* and uses the `sitemap` view. The sitemaps dictionary is passed to the `sitemap` view.:

```py
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [
    ...
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
```

- Domain name for the sitemap can be modified via Django admin panel.

### Content Feed (RSS)

- [Syndication Feed Framework](https://docs.djangoproject.com/en/3.0/ref/contrib/syndication/)

- Django has a built-in syndication feed framework that you can use to dynamically generate RSS or Atom feeds in a similar manner to creating sitemaps using the site's framework. A web feed is a data format (usually XML) that provides users with the most recently updated content. Users will be able to subscribe to your feed using a feed aggregator (software that is used to read feeds and get new content notifications).

- Inside *feeds.py* in the application directory:

```py
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
```


3
Extending Your Blog Application

The previous chapter went through the basics of forms and the creation of a comment system. You also learned how to send emails with Django, and you implemented a tagging system by integrating a third-party application with your project. In this chapter, you will extend your blog application with some other popular features used on blogging platforms. You will also learn about other components and functionalities with Django.

The chapter will cover the following points:

    Creating custom template tags and filters: You will learn how to build your own template tags and template filters to exploit the capabilities of Django templates.
    Adding a sitemap and post feed: You will learn how to use the sitemaps framework and syndication framework that come with Django.
    Implementing full-text search with PostgreSQL: Search is a very popular feature for blogs. You will learn how to implement an advanced search engine for your blog application.

Creating custom template tags and filters

Django offers a variety of built-in template tags, such as {% if %} or {% block %}. You used different template tags in Chapter 1, Building a Blog Application, and Chapter 2, Enhancing Your Blog with Advanced Features. You can find a complete reference of built-in template tags and filters at https://docs.djangoproject.com/en/3.0/ref/templates/builtins/.

Django also allows you to create your own template tags to perform custom actions. Custom template tags come in very handy when you need to add a functionality to your templates that is not covered by the core set of Django template tags. This could be a tag to perform a QuerySet or any server-side processing that you want to reuse across templates. For example, you could build a template tag to display the list of latest posts published on your blog. You can include this list in the sidebar of the blog for multiple pages, regardless of the view.
Custom template tags

Django provides the following helper functions that allow you to create your own template tags in an easy manner:

    simple_tag: Processes the data and returns a string
    inclusion_tag: Processes the data and returns a rendered template

Template tags must live inside Django applications.

Inside your blog application directory, create a new directory, name it templatetags, and add an empty __init__.py file to it. Create another file in the same folder and name it blog_tags.py. The file structure of the blog application should look like the following:

blog/
    __init__.py
    models.py
    ...
    templatetags/
        __init__.py
        blog_tags.py

The way you name the file is important. You will use the name of this module to load tags in templates.

Let's start by creating a simple tag to retrieve the total posts published on the blog. Edit the blog_tags.py file you just created and add the following code:

from django import template
from ..models import Post
register = template.Library()
@register.simple_tag
def total_posts():
    return Post.published.count()

You have created a simple template tag that returns the number of posts published so far. Each module that contains template tags needs to define a variable called register to be a valid tag library. This variable is an instance of template.Library, and it's used to register your own template tags and filters.

In the code above, you define a tag called total_posts with a Python function and use the @register.simple_tag decorator to register the function as a simple tag. Django will use the function's name as the tag name. If you want to register it using a different name, you can do so by specifying a name attribute, such as @register.simple_tag(name='my_tag').

After adding a new template tags module, you will need to restart the Django development server in order to use the new tags and filters in templates.

Before using custom template tags, you have to make them available for the template using the {% load %} tag. As mentioned before, you need to use the name of the Python module containing your template tags and filters.

Open the blog/templates/base.html template and add {% load blog_tags %} at the top of it to load your template tags module. Then, use the tag you created to display your total posts. Just add {% total_posts %} to your template. The template should look like this:

{% load blog_tags %}
{% load static %}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
  <link href="{% static "css/blog.css" %}" rel="stylesheet">
</head>
<body>
  <div id="content">
    {% block content %}
    {% endblock %}
  </div>
  <div id="sidebar">
    <h2>My blog</h2>
    <p>This is my blog. I've written {% total_posts %} posts so far.</p>
  </div>
</body>
</html>

You will need to restart the server to keep track of the new files added to the project. Stop the development server with Ctrl + C and run it again using the following command:

python manage.py runserver

Open http://127.0.0.1:8000/blog/ in your browser. You should see the total number of posts in the sidebar of the site, as follows:

Figure 3.1: The total posts published included in the sidebar

The power of custom template tags is that you can process any data and add it to any template regardless of the view executed. You can perform QuerySets or process any data to display results in your templates.

Now, you will create another tag to display the latest posts in the sidebar of your blog. This time, you will use an inclusion tag. Using an inclusion tag, you can render a template with context variables returned by your template tag.

Edit the blog_tags.py file and add the following code:

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

In the preceding code, you register the template tag using @register.inclusion_tag and specify the template that will be rendered with the returned values using blog/post/latest_posts.html. Your template tag will accept an optional count parameter that defaults to 5. This parameter you to specify the number of posts that you want to display. You use this variable to limit the results of the query Post.published.order_by('-publish')[:count].

Note that the function returns a dictionary of variables instead of a simple value. Inclusion tags have to return a dictionary of values, which is used as the context to render the specified template. The template tag you just created allows you to specify the optional number of posts to display as {% show_latest_posts 3 %}.

Now, create a new template file under blog/post/ and name it latest_posts.html. Add the following code to it:

<ul>
  {% for post in latest_posts %}
    <li>
      <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

In the preceding code, you display an unordered list of posts using the latest_posts variable returned by your template tag. Now, edit the blog/base.html template and add the new template tag to display the last three posts. The sidebar code should look like the following:

<div id="sidebar">
  <h2>My blog</h2>
  <p>This is my blog. I've written {% total_posts %} posts so far.</p>
  <h3>Latest posts</h3>
  {% show_latest_posts 3 %}
</div>

The template tag is called, passing the number of posts to display, and the template is rendered in place with the given context.

Next, return to your browser and refresh the page. The sidebar should now look like this:

Figure 3.2: The sidebar, including the latest published posts

Finally, you will create a simple template tag that returns a value. You will store the result in a variable that can be reused, rather than directly outputting it. You will create a tag to display the most commented posts.

Edit the blog_tags.py file and add the following import and template tag to it:

from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
               total_comments=Count('comments')
           ).order_by('-total_comments')[:count]

In the preceding template tag, you build a QuerySet using the annotate() function to aggregate the total number of comments for each post. You use the Count aggregation function to store the number of comments in the computed field total_comments for each Post object. You order the QuerySet by the computed field in descending order. You also provide an optional count variable to limit the total number of objects returned.

In addition to Count, Django offers the aggregation functions Avg, Max, Min, and Sum. You can read more about aggregation functions at https://docs.djangoproject.com/en/3.0/topics/db/aggregation/.

Next, edit the blog/base.html template and append the following code to the sidebar <div> element:

<h3>Most commented posts</h3>
{% get_most_commented_posts as most_commented_posts %}
<ul>
  {% for post in most_commented_posts %}
    <li>
      <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

In the preceding code, you store the result in a custom variable using the as argument followed by the variable name. For your template tag, you use {% get_most_commented_posts as most_commented_posts %} to store the result of the template tag in a new variable named most_commented_posts. Then, you display the returned posts using an unordered list.

Now open your browser and refresh the page to see the final result. It should look like the following:

Figure 3.3: The post list view, including the complete sidebar with the latest and most commented posts

You have now a clear idea about how to build custom template tags. You can read more about them at https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/.
Custom template filters

Django has a variety of built-in template filters that allow you to alter variables in templates. These are Python functions that take one or two parameters, the value of the variable that the filter is applied to, and an optional argument. They return a value that can be displayed or treated by another filter. A filter looks like {{ variable|my_filter }}. Filters with an argument look like {{ variable|my_filter:"foo" }}. For example, you can use the capfirst filter to capitalize the first character of the value, like {{ value|capfirst }}. If value is "django", the output will be "Django". You can apply as many filters as you like to a variable, for example, {{ variable|filter1|filter2 }}, and each of them will be applied to the output generated by the preceding filter.

You can find the list of Django's built-in template filters at https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-filter-reference.

You will create a custom filter to enable you to use markdown syntax in your blog posts and then convert the post contents to HTML in the templates. Markdown is a plain-text formatting syntax that is very simple to use, and it's intended to be converted into HTML. You can write posts using simple markdown syntax and get the content automatically converted into HTML code. Learning markdown syntax is much easier than learning HTML. By using markdown, you can get other non-tech savvy contributors to easily write posts for your blog. You can learn the basics of the markdown format at https://daringfireball.net/projects/markdown/basics.

First, install the Python markdown module via pip using the following command:

pip install markdown==3.2.1

Then, edit the blog_tags.py file and include the following code:

from django.utils.safestring import mark_safe
import markdown
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

You register template filters in the same way as template tags. To prevent a name clash between your function name and the markdown module, you name your function markdown_format and name the filter markdown for use in templates, such as {{ variable|markdown }}. Django escapes the HTML code generated by filters; characters of HTML entities are replaced with their HTML encoded characters. For example, <p> is converted to &lt;p&gt; (less than symbol, p character, greater than symbol). You use the mark_safe function provided by Django to mark the result as safe HTML to be rendered in the template. By default, Django will not trust any HTML code and will escape it before placing it in the output. The only exceptions are variables that are marked as safe from escaping. This behavior prevents Django from outputting potentially dangerous HTML and allows you to create exceptions for returning safe HTML.

Now, load your template tags module in the post list and detail templates. Add the following line at the top of the blog/post/list.html and blog/post/detail.html templates after the {% extends %} tag:

{% load blog_tags %}

In the post/detail.html template, look for the following line:

{{ post.body|linebreaks }}

Replace it with the following one:

{{ post.body|markdown }}

Then, in the post/list.html template, find the following line:

{{ post.body|truncatewords:30|linebreaks }}

Replace it with the following one:

{{ post.body|markdown|truncatewords_html:30 }}

The truncatewords_html filter truncates a string after a certain number of words, avoiding unclosed HTML tags.

Now open http://127.0.0.1:8000/admin/blog/post/add/ in your browser and add a post with the following body:

This is a post formatted with markdown
--------------------------------------
*This is emphasized* and **this is more emphasized**.
Here is a list:
* One
* Two
* Three
And a [link to the Django website](https://www.djangoproject.com/)

Open your browser and take a look at how the post is rendered. You should see the following output:

Figure 3.4: The post with markdown content rendered as HTML

As you can see in the preceding screenshot, custom template filters are very useful for customizing formatting. You can find more information about custom filters at https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/#writing-custom-template-filters.
Adding a sitemap to your site

Django comes with a sitemap framework, which allows you to generate sitemaps for your site dynamically. A sitemap is an XML file that tells search engines the pages of your website, their relevance, and how frequently they are updated. Using a sitemap will make your site more visible in search engine rankings: sitemaps help crawlers to index your website's content.

The Django sitemap framework depends on django.contrib.sites, which allows you to associate objects to particular websites that are running with your project. This comes in handy when you want to run multiple sites using a single Django project. To install the sitemap framework, you will need to activate both the sites and the sitemap applications in your project.

Edit the settings.py file of your project and add django.contrib.sites and django.contrib.sitemaps to the INSTALLED_APPS setting. Also, define a new setting for the site ID, as follows:

SITE_ID = 1
# Application definition
INSTALLED_APPS = [
    # ...
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

Now run the following command to create the tables of the Django site application in the database:

python manage.py migrate

You should see an output that contains the following lines:

Applying sites.0001_initial... OK
Applying sites.0002_alter_domain_unique... OK

The sites application is now synced with the database.

Next, create a new file inside your blog application directory and name it sitemaps.py. Open the file and add the following code to it:

from django.contrib.sitemaps import Sitemap
from .models import Post
class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Post.published.all()
    def lastmod(self, obj):
        return obj.updated

You create a custom sitemap by inheriting the Sitemap class of the sitemaps module. The changefreq and priority attributes indicate the change frequency of your post pages and their relevance in your website (the maximum value is 1).

The items() method returns the QuerySet of objects to include in this sitemap. By default, Django calls the get_absolute_url() method on each object to retrieve its URL. Remember that you created this method in Chapter 1, Building a Blog Application, to retrieve the canonical URL for posts. If you want to specify the URL for each object, you can add a location method to your sitemap class.

The lastmod method receives each object returned by items() and returns the last time the object was modified.

Both the changefreq and priority attributes can be either methods or attributes. You can take a look at the complete sitemap reference in the official Django documentation located at https://docs.djangoproject.com/en/3.0/ref/contrib/sitemaps/.

Finally, you just need to add your sitemap URL. Edit the main urls.py file of your project and add the sitemap, as follows:

from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

In the preceding code, you include the required imports and define a dictionary of sitemaps. You define a URL pattern that matches sitemap.xml and uses the sitemap view. The sitemaps dictionary is passed to the sitemap view.

Now run the development server and open http://127.0.0.1:8000/sitemap.xml in your browser. You will see the following XML output:

<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>http://example.com/blog/2020/1/2/markdown-post/</loc>
    <lastmod>2020-01-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>
http://example.com/blog/2020/1/1/who-was-django-reinhardt/
</loc>
    <lastmod>2020-01-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>

The URL for each post has been built calling its get_absolute_url() method.

The lastmod attribute corresponds to the post updated date field, as you specified in your sitemap, and the changefreq and priority attributes are also taken from the PostSitemap class.

You can see that the domain used to build the URLs is example.com. This domain comes from a Site object stored in the database. This default object was created when you synced the site's framework with your database.

Open http://127.0.0.1:8000/admin/sites/site/ in your browser. You should see something like this:

Figure 3.5: The Django administration list view for the Site model of the site's framework

The preceding screenshot contains the list display administration view for the site's framework. Here, you can set the domain or host to be used by the site's framework and the applications that depend on it. In order to generate URLs that exist in your local environment, change the domain name to localhost:8000, as shown in the following screenshot, and save it:

Figure 3.6: The Django administration edit view for the Site model of the site's framework

The URLs displayed in your feed will now be built using this hostname. In a production environment, you will have to use your own domain name for the site's framework.
Creating feeds for your blog posts

Django has a built-in syndication feed framework that you can use to dynamically generate RSS or Atom feeds in a similar manner to creating sitemaps using the site's framework. A web feed is a data format (usually XML) that provides users with the most recently updated content. Users will be able to subscribe to your feed using a feed aggregator (software that is used to read feeds and get new content notifications).

Create a new file in your blog application directory and name it feeds.py. Add the following lines to it:

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post
class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'
    def items(self):
        return Post.published.all()[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return truncatewords(item.body, 30)

- First, you subclass the Feed class of the syndication framework. The title, link, and description attributes correspond to the `<title>`, `<link>`, and `<description>` RSS elements, respectively.

- Add RSS feed into the URLs:

```py
from .feeds import LatestPostsFeed

urlpatterns = [
    # ...
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
```
