# Django

## Table of Contents

- [Django](#django)
  - [Table of Contents](#table-of-contents)
  - [Sources](#sources)
  - [Django Related Resources](#django-related-resources)
  - [Basics](#basics)
  - [Models](#models)
    - [Creating Model Managers](#creating-model-managers)
    - [Custom Many-to-Many Relationship](#custom-many-to-many-relationship)
    - [Generic Relations](#generic-relations)
    - [Model Inheritance](#model-inheritance)
      - [Abstract Models](#abstract-models)
      - [Multi-table Model Inheritance](#multi-table-model-inheritance)
      - [Proxy Models](#proxy-models)
    - [Custom Model Fields](#custom-model-fields)
    - [Activity Stream](#activity-stream)
    - [Relationship fields](#relationship-fields)
      - [on_delete](#on_delete)
    - [Fixtures](#fixtures)
  - [Databases and ORMs](#databases-and-orms)
    - [ORM Methods](#orm-methods)
      - [QuerySet API](#queryset-api)
        - [annotate](#annotate)
        - [values_list](#values_list)
    - [Optimizing QuerySets that Involve Related Objects](#optimizing-querysets-that-involve-related-objects)
      - [select_related](#select_related)
      - [prefetch_related](#prefetch_related)
    - [Using Signals for Denormalizing Counts](#using-signals-for-denormalizing-counts)
  - [Admin Panel and Customization](#admin-panel-and-customization)
    - [Adding Custom Actions to the Administration Site](#adding-custom-actions-to-the-administration-site)
    - [Extending the Administration Site with Custom Views](#extending-the-administration-site-with-custom-views)
  - [Views](#views)
    - [Generic Views](#generic-views)
    - [Generic Views (from Django tutorial)](#generic-views-from-django-tutorial)
  - [URLs](#urls)
  - [Templates](#templates)
    - [Custom Template Tags](#custom-template-tags)
    - [Filters](#filters)
    - [Custom Template Filters](#custom-template-filters)
    - [Pagination](#pagination)
    - [Context Processors](#context-processors)
  - [Testing](#testing)
    - [Client Testing](#client-testing)
    - [Testing Frontend with Selenium](#testing-frontend-with-selenium)
  - [Forms](#forms)
    - [Form Class Forms](#form-class-forms)
    - [ModelForm Class Forms](#modelform-class-forms)
    - [FormSets](#formsets)
  - [Authentication and Authorization](#authentication-and-authorization)
    - [Django Authentication Views](#django-authentication-views)
    - [Extending the User Model](#extending-the-user-model)
    - [Using a Custom User Model](#using-a-custom-user-model)
    - [Custom Authentication Backend](#custom-authentication-backend)
    - [Social Authentication](#social-authentication)
    - [django-guardian](#django-guardian)
  - [Session Management](#session-management)
  - [Message Framework](#message-framework)
  - [Static Files](#static-files)
  - [Caching](#caching)
    - [Memcached](#memcached)
      - [Low-level Cache API](#low-level-cache-api)
      - [Caching Template Fragments](#caching-template-fragments)
      - [Caching Views](#caching-views)
    - [Redis Cache](#redis-cache)
  - [Configuration](#configuration)
    - [Development Server Through HTTPS](#development-server-through-https)
  - [Utilities](#utilities)
    - [Sending Emails](#sending-emails)
    - [Absolute URI](#absolute-uri)
    - [Taggit](#taggit)
    - [Sitemaps](#sitemaps)
    - [Content Feed (RSS)](#content-feed-rss)
    - [Full-Text Search](#full-text-search)
      - [Simple Search Lookups](#simple-search-lookups)
      - [Searching Against Mltiple Fields](#searching-against-mltiple-fields)
      - [Stemming and Ranking Results](#stemming-and-ranking-results)
      - [Weighting Queries](#weighting-queries)
      - [Searching with Trigram Similarity](#searching-with-trigram-similarity)
    - [Translations](#translations)
      - [Translation Template Tags](#translation-template-tags)
      - [Rosetta](#rosetta)
    - [Recommendation Engine](#recommendation-engine)
  - [Redis](#redis)
    - [Redis with Django](#redis-with-django)
    - [Storing a view count in Redis](#storing-a-view-count-in-redis)
    - [Storing a ranking in Redis](#storing-a-ranking-in-redis)
  - [Celery](#celery)
    - [Adding Celery to the Project](#adding-celery-to-the-project)
    - [Asynchronous Task Example](#asynchronous-task-example)
    - [Monitoring Celery with Flower](#monitoring-celery-with-flower)
    - [Braintree](#braintree)
    - [Outputting PDF](#outputting-pdf)
  - [Django Rest Framework (DRF)](#django-rest-framework-drf)
    - [Adding Additional Actions to ViewSets](#adding-additional-actions-to-viewsets)
    - [Creating Custom Permissions](#creating-custom-permissions)
  - [Django Channels](#django-channels)
    - [Writing a Consumer](#writing-a-consumer)
    - [Routing](#routing)
    - [Implementing The WebSocket Client](#implementing-the-websocket-client)
    - [Enabling a Channel Layer](#enabling-a-channel-layer)
      - [Setting up a channel layer with Redis](#setting-up-a-channel-layer-with-redis)
  - [Django App Deployment](#django-app-deployment)
    - [Heroku](#heroku)

## Sources

- [Django Official Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- [CS50 Harvard Course](https://cs50.harvard.edu/web/2020/weeks/3/)
- [Django 3 By Example - Third Edition](https://learning.oreilly.com/library/view/django-3-by/9781838981952/)

## Django Related Resources

- [Django Cheat Sheet](https://dev.to/ericchapman/my-beloved-django-cheat-sheet-2056)
- [Django AdminLTE3 Tutorial](https://github.com/fseesink/django-adminlte3-tutorial)

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

- **Database indexes** improve query performance. Consider setting `db_index=True` for fields that you frequently query using `filter()`, `exclude()`, or `order_by()`. `ForeignKey` fields or fields with `unique=True` imply the creation of an index. You can also use `Meta.index_together` or `Meta.indexes` to create indexes for multiple fields. [More about database indexes](https://docs.djangoproject.com/en/3.0/ref/models/options/#django.db.models.Options.indexes).

- A **database index** is automatically created on the `ForeignKey` fields. You use `db_index=True` to create a database index for the created field. This will improve query performance when ordering QuerySets by this field.


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

### Custom Many-to-Many Relationship

- When you need additional fields in a many-to-many relationship, create a custom model with a ForeignKey for each side of the relationship. Add a ManyToManyField in one of the related models and indicate to Django that your intermediary model should be used by including it in the through parameter.

```py
class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

# On the User Model
following = models.ManyToManyField('self',
                                   through=Contact,
                                   related_name='followers',
                                   symmetrical=False)
```

### Generic Relations

- Generic relations allow to create foreign keys that can point to the objects of any model. This is useful if we need a model that needs to refer to other model that might need to store different types of data (text, file, image, URL, etc.):

```py
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                   on_delete=models.CASCADE,
                   limit_choices_to={'model__in':(
                                     'text',
                                     'video',
                                     'image',
                                     'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    def __str__(self):
        return self.title
class Text(ItemBase):
    content = models.TextField()
class File(ItemBase):
    file = models.FileField(upload_to='files')
class Image(ItemBase):
    file = models.FileField(upload_to='images')
class Video(ItemBase):
    url = models.URLField()
```

### Model Inheritance

- Django supports **model inheritance**. It works in a similar way to standard class inheritance in Python. Django offers the following three options to use model inheritance:

    - **Abstract models**: Useful when you want to put some common information into several models.
    - **Multi-table model inheritance**: Applicable when each model in the hierarchy is considered a complete model by itself.
    - **Proxy models**: Useful when you need to change the behavior of a model, for example, by including additional methods, changing the default manager, or using different meta options.

#### Abstract Models

- To mark a model as abstract, you need to include `abstract=True` in its `Meta` class.

```py
from django.db import models
class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
class Text(BaseContent):
    body = models.TextField()
```

#### Multi-table Model Inheritance

- In **multi-table inheritance**, each model corresponds to a database table. Django creates a `OneToOneField` field for the relationship between the child model and its parent model. To use multi-table inheritance, you have to subclass an existing model. **Django will create a database table for both the original model and the sub-model**. The following example shows multi-table inheritance:

```py
from django.db import models
class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
class Text(BaseContent):
    body = models.TextField()
```

#### Proxy Models

- A proxy model changes the behavior of a model. Both models operate on the database table of the original model. To create a proxy model, add `proxy=True` to the `Meta` class of the model. The following example illustrates how to create a proxy model:

```py
from django.db import models
from django.utils import timezone
class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
class OrderedContent(BaseContent):
    class Meta:
        proxy = True
        ordering = ['created']
    def created_delta(self):
        return timezone.now() - self.created
```

### Custom Model Fields

- Creating a custom `OrderField` that inherits from `PositiveIntegerField`:

```py
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)
    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # no current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    # filter by objects with the same field values
                    # for the fields in "for_fields"
                    query = {field: getattr(model_instance, field)\
                    for field in self.for_fields}
                    qs = qs.filter(**query)
                # get the order of the last item
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
```

### Activity Stream

- An **activity stream** is a list of recent activities performed by a user or a group of users. For example, Facebook's News Feed is an activity stream. Sample actions can be *user X bookmarked image Y* or *user X is now following user Y*.

- Django includes a `contenttypes` framework located at `django.contrib.contenttypes`. This application can track all models installed in your project and provides a generic interface to interact with your models.

- The contenttypes application contains a ContentType model. Instances of this model represent the actual models of your application, and new instances of ContentType are automatically created when new models are installed in your project. The ContentType model has the following fields:

  - `app_label`: This indicates the name of the application that the model belongs to. This is automatically taken from the app_label attribute of the model `Meta` options. For example, your `Image` model belongs to the `images` application.
  - `model`: The name of the model class.
  - `name`: This indicates the human-readable name of the model. This is automatically taken from the `verbose_name` attribute of the model `Meta` options.

```py
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
class Action(models.Model):
    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             db_index=True,
                             on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)
    class Meta:
        ordering = ('-created',)
```

- Django does not create any field in the database for `GenericForeignKey` fields. The only fields that are mapped to database fields are `target_ct` and `target_id`. Both fields have `blank=True` and `null=True` attributes, so that a target object is not required when saving `Action` objects.

### Relationship fields

#### on_delete

- `models.CASCADE` - cascade deletes. Django emulates the behavior of the SQL constraint `ON DELETE CASCADE` and also deletes the object containing the ForeignKey.

- `models.PROTECT` - prevents deletion of the referenced object by raising `ProtectedError`, a subclass of `django.db.IntegrityError`.

- `models.RESTRICT` - prevents deletion of the referenced object by raising `RestrictedError` (a subclass of `django.db.IntegrityError`). Unlike `PROTECT`, deletion of the referenced object is allowed if it also references a different object that is being deleted in the same operation, but via a `CASCADE` relationship.

```py
class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)

artist_one = Artist.objects.create(name='artist one')
artist_two = Artist.objects.create(name='artist two')
album_one = Album.objects.create(artist=artist_one)
album_two = Album.objects.create(artist=artist_two)
song_one = Song.objects.create(artist=artist_one, album=album_one)
song_two = Song.objects.create(artist=artist_one, album=album_two)
album_one.delete()
# Raises RestrictedError.
artist_two.delete()
# Raises RestrictedError.
artist_one.delete()
# (4, {'Song': 2, 'Album': 1, 'Artist': 1})
```

- `models.SET_NULL` - sets the ForeignKey `null`; this is only possible if `null` is `True`.

- `models.SET_DEFAULT` - sets the ForeignKey to its default value; a default for the ForeignKey must be set.

### Fixtures

- **Fixtures** can be used to provide initial data for models.

- Dumping current data from a database to the fixture files:

```bash
# dumping entire database
python manage.py dumpdata --indent=2
# dumping tables relate to specific application
python manage.py dumpdata courses --indent=2
# dumping table for specific model
python manage.py dumpdata courses.subject --indent=2
# dumping data to a specific location
python manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
```

- Loading fixtures into a database:

```bash
python manage.py loaddata subjects.json
```

- By default, Django looks for files in the `fixtures/` directory of each application, but you can specify the complete path to the fixture file for the `loaddata` command. You can also use the `FIXTURE_DIRS` setting to tell Django additional directories to look in for fixtures.

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

### Optimizing QuerySets that Involve Related Objects

#### select_related

- Django offers a QuerySet method called `select_related()` that allows you to retrieve related objects for one-to-many relationships. This translates to a single, more complex QuerySet, but you avoid additional queries when accessing the related objects. The `select_related` method is for `ForeignKey` and OneToOne fields. It works by performing a SQL `JOIN` and including the fields of the related object in the `SELECT` statement.

- You use `user__profile` to join the `Profile` table in a single SQL query. If you call `select_related()` without passing any arguments to it, it will retrieve objects from all `ForeignKey` relationships. Always limit `select_related()` to the relationships that will be accessed afterward.

```py
actions = actions.select_related('user', 'user__profile')[:10]
```

#### prefetch_related

- Django offers a different QuerySet method called `prefetch_related` that works for many-to-many and many-to-one relationships in addition to the relationships supported by `select_related()`. The `prefetch_related()` method performs a separate lookup for each relationship and joins the results using Python. This method also supports the prefetching of `GenericRelation` and `GenericForeignKey`.

```py
actions = actions.select_related('user', 'user__profile') \
                 .prefetch_related('target')[:10]
```

### Using Signals for Denormalizing Counts

- There are some cases when you may want to denormalize your data. Denormalization is making data redundant in such a way that it optimizes read performance. For example, you might be copying related data to an object to avoid expensive read queries to the database when retrieving the related data. You have to be careful about denormalization and only start using it when you really need it. The biggest issue you will find with denormalization is that it's difficult to keep your denormalized data updated.

```py
# This query is poorly optimized as it required computation
# of 'total_likes' field.
images_by_popularity = Image.objects.annotate(
    total_likes=Count('users_like')).order_by('-total_likes')

# Instead we can denormalize 'total_likes' count by creating additonal
# field in the model
class Image(models.Model):
    # ...
    total_likes = models.PositiveIntegerField(db_index=True,
                                              default=0)

# Updating count can be then performed using signals
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
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

### Adding Custom Actions to the Administration Site

- You can create a custom action by writing a regular function that receives the following parameters:

  - The current `ModelAdmin` being displayed
  - The current request object as an `HttpRequest` instance
  - A `QuerySet` for the objects selected by the user

```py
import csv
import datetime
from django.http import HttpResponse
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = 'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not \
    field.many_to_many and not field.one_to_many] 
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

# Adding custom action to the Admin Site
class OrderAdmin(admin.ModelAdmin):
    # ...
    actions = [export_to_csv]
```

### Extending the Administration Site with Custom Views

- Admin [base template](https://github.com/django/django/blob/main/django/contrib/admin/templates/admin/base.html)

```py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})
```

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

### Generic Views (from Django tutorial)

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

## URLs

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

## Templates

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

### Custom Template Tags

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

### Filters

- [Built-in template filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-filter-reference)

- Filters can be used outside of the templates as well. Default filters can be imported from `django.template.defaultfilters`.

- Django has a variety of built-in template filters that allow you to alter variables in templates. These are Python functions that take one or two parameters, the value of the variable that the filter is applied to, and an optional argument. They return a value that can be displayed or treated by another filter. A filter looks like `{{ variable|my_filter }}`. Filters with an argument look like `{{ variable|my_filter:"foo" }}`.

- You can apply as many filters as you like to a variable, for example, `{{ variable|filter1|filter2 }}`, and each of them will be applied to the output generated by the preceding filter.

- Example of template filters:

  - `truncatewords` truncates the value to the number of words specified
  - `linebreaks` converts the output into HTML line breaks
  - `pluralize` displays a plural suffix for the given word
  - `join` works the same as the Python string `join()` method concatenating elements from iterable

### Custom Template Filters

- You register template filters in the same way as template tags:

```py
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
```

### Pagination

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

### Context Processors

- A **context processor** is a Python function that takes the request object as an argument and returns a dictionary that gets added to the request context. Context processors come in handy when you need to make something available globally to all templates.

- Context processors are executed in all the requests that use `RequestContext`. You might want to create a custom template tag instead of a context processor if your functionality is not needed in all templates, especially if it involves database queries.

- Simple context processor example:

```py
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # ...
                'cart.context_processors.cart',
            ],
        },
    },
]

# context_processors.py
from .cart import Cart
def cart(request):
    return {'cart': Cart(request)}
```

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

### FormSets

- Django comes with an abstraction layer to work with multiple forms on the same page. These groups of forms are known as **formsets**. Formsets manage multiple instances of a certain `Form` or `ModelForm`. All forms are submitted at once and the formset takes care of the initial number of forms to display, limiting the maximum number of forms that can be submitted and validating all the forms.

- Formsets include an `is_valid()` method to validate all forms at once. You can also provide initial data for the forms and specify how many additional empty forms to display.

```py
from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module
ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title',
                                              'description'],
                                      extra=2,
                                      can_delete=True)
```

## Authentication and Authorization

- Django comes with a built-in authentication framework that can handle user authentication, sessions, permissions, and user groups. The authentication system includes views for common user actions such as log in, log out, password change, and password reset.

- When you create a new Django project using the `startproject` command, the authentication framework is included in the default settings of your project. It consists of the `django.contrib.auth` application and the following two middleware classes found in the `MIDDLEWARE` setting of your project:

    - `AuthenticationMiddleware`: Associates users with requests using sessions
    - `SessionMiddleware`: Handles the current session across requests

- **Middleware** are classes with methods that are globally executed during the request or response phase.

- The authentication framework also includes the following models:

  - `User`: A user model with basic fields; the main fields of this model are username, password, email, first_name, last_name, and is_active
  - `Group`: A group model to categorize users
  - `Permission`: Flags for users or groups to perform certain actions

- The framework also includes default authentication views and forms.

- Note the difference between `authenticate` and `login`: `authenticate()` checks user credentials and returns a `User` object if they are correct; `login()` sets the user in the current session.

### Django Authentication Views

- [Django buil-it authentication views](https://docs.djangoproject.com/en/3.0/topics/auth/default/#all-authentication-views)

- Django provides the following class-based views to deal with authentication. All of them are located in `django.contrib.auth.views`:

  - `LoginView`: Handles a login form and logs in a user
  - `LogoutView`: Logs out a user

- Django provides the following views to handle password changes:

  - `PasswordChangeView`: Handles a form to change the user's password
  - `PasswordChangeDoneView`: The success view that the user is redirected to after a successful password change

- Django also includes the following views to enable users to reset their password:

  - `PasswordResetView`: Allows users to reset their password. It generates a one-time-use link with a token and sends it to a user's email account.
  - `PasswordResetDoneView`: Tells users that an email—including a link to reset their password—has been sent to them.
  - `PasswordResetConfirmView`: Allows users to set a new password.
  - `PasswordResetCompleteView`: The success view that the user is redirected to after successfully resetting their password.

- If an app has been placed at the top of the `INSTALLED_APPS` setting then Django will use this application's templates instead of other default ones. The default path where the Django authentication views expect your authentication templates to be is *registration* folder inside templates directory.

- The settings that determine authentication related behaviours:

  - `LOGIN_REDIRECT_URL`: Tells Django which URL to redirect the user to after a successful login if no next parameter is present in the request
  - `LOGIN_URL`: The URL to redirect the user to log in (for example, views using the login_required decorator)
  - `LOGOUT_URL`: The URL to redirect the user to log out

### Extending the User Model

- When you have to deal with user accounts, you will find that the user model of the Django authentication framework is suitable for common cases. However, the user model comes with very basic fields. You may wish to extend it to include additional data. The best way to do this is by creating a profile model that contains all additional fields and a one-to-one relationship with the Django User model. A one-to-one relationship is similar to a `ForeignKey` field with the parameter `unique=True`. The reverse side of the relationship is an implicit one-to-one relationship with the related model instead of a manager for multiple elements. From each side of the relationship, you retrieve a single related object.

```py
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    def __str__(self):
        return f'Profile for user {self.user.username}'
```

- In order to keep your code generic, use the `get_user_model()` method to retrieve the user model and the `AUTH_USER_MODEL` setting to refer to it when defining a model's relationship with the user model, instead of referring to the auth user model directly.

### Using a Custom User Model

- [Substituting a custom user model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model)

- Django also offers a way to substitute the whole user model with your own custom model. Your user class should inherit from Django's AbstractUser class, which provides the full implementation of the default user as an abstract model.

### Custom Authentication Backend

- [Customizing Authentication](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#other-authentication-sources)

- Django allows you to authenticate against different sources. The `AUTHENTICATION_BACKENDS` setting includes the list of authentication backends for your project. By default, this setting is set as follows:

```py
['django.contrib.auth.backends.ModelBackend']
```

- The default `ModelBackend` authenticates users against the database using the user model of `django.contrib.auth`. This will suit most of your projects. However, you can create custom backends to authenticate your user against other sources, such as a Lightweight Directory Access Protocol (LDAP) directory or any other system.

- Whenever you use the `authenticate()` function of `django.contrib.auth`, Django tries to authenticate the user against each of the backends defined in `AUTHENTICATION_BACKENDS` one by one, until one of them successfully authenticates the user. Only if all of the backends fail to authenticate will the user not be authenticated into your site.

- Django provides a simple way to define your own authentication backends. An authentication backend is a class that provides the following two methods:

  - `authenticate()`: It takes the request object and user credentials as parameters. It has to return a user object that matches those credentials if the credentials are valid, or None otherwise. The request parameter is an HttpRequest object, or None if it's not provided to authenticate().
  - `get_user()`: This takes a user ID parameter and has to return a user object.

```py
from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
```

- The order of the backends listed in the `AUTHENTICATION_BACKENDS` setting matters. If the same credentials are valid for multiple backends, Django will stop at the first backend that successfully authenticates the user.

### Social Authentication

- You might also want to add social authentication to your site using services such as Facebook, Twitter, or Google. [**Python Social Auth**](https://github.com/python-social-auth/social-app-django) is a Python module that simplifies the process of adding social authentication to your website. Using this module, you can let your users log in to your website using their accounts from other services.

### django-guardian

- **django-guardian** is an implementation of per object permissions on top of Django's authorization backend. [django-guardian GitHub](https://github.com/django-guardian/django-guardian)

## Session Management

- [Django Sessions](https://docs.djangoproject.com/en/3.2/topics/http/sessions/)

- Example of sessions usage is available in Chapter 7 of Django by Example 3. [Shopping cart implementation using Django Sessions](https://github.com/PacktPublishing/Django-3-by-Example/blob/master/Chapter07/myshop/cart/cart.py)

- Django provides a **session framework** that supports anonymous and user sessions. The session framework allows you to store arbitrary data for each visitor. Session data is stored on the server side, and cookies contain the session ID unless you use the cookie-based session engine. The session middleware manages the sending and receiving of cookies. The default session engine stores session data in the database, but you can choose other session engines.

- Data can be stored in client session (first `python manage.py migrate` needs to be run to create all of the default tables inside a Django database):

```python
def add(request):
    if 'tasks' not in request.session:
        request.session['tasks'] += [task]
```

- When users log in to the site, their anonymous session is lost and a new session is created for authenticated users. If you store items in an anonymous session that you need to keep after the user logs in, you will have to copy the old session data into the new session. You can do this by retrieving the session data before you log in the user using the login() function of the Django authentication system and storing it in the session after that.

- Django offers the following options for storing session data. For better performance use a cache-based session engine. Django supports **Memcached** out of the box and you can find third-party cache backends for Redis and other cache systems.:

    - **Database sessions**: Session data is stored in the database. This is the default session engine.
    - **File-based sessions**: Session data is stored in the filesystem.
    - **Cached sessions**: Session data is stored in a cache backend. You can specify cache backends using the CACHES setting. Storing session data in a cache system provides the best performance.
    - **Cached database sessions**: Session data is stored in a write-through cache and database. Reads only use the database if the data is not already in the cache.
    - **Cookie-based sessions**: Session data is stored in the cookies that are sent to the browser.

## Message Framework

- Django has a built-in messages framework that allows you to display one-time notifications to your users.

- The messages framework is located at `django.contrib.messages` and is included in the default `INSTALLED_APPS` list of the *settings.py* file when you create new projects using `python manage.py startproject`. You will note that your settings file contains a middleware named `django.contrib.messages.middleware.MessageMiddleware` in the `MIDDLEWARE` settings.

- The messages framework provides a simple way to add messages to users. Messages are stored in a cookie by default (falling back to session storage), and they are displayed in the next request from the user. You can use the messages framework in your views by importing the messages module and adding new messages with simple shortcuts, as follows:

```py
from django.contrib import messages
messages.error(request, 'Something went wrong')
```

## Static Files

- Django’s `STATICFILES_FINDERS` setting contains a list of finders that know how to discover static files from various sources. One of the defaults is `AppDirectoriesFinder` which looks for a *static* subdirectory in each of the `INSTALLED_APPS`.

## Caching

- [Cache Django Docs](https://docs.djangoproject.com/en/3.2/topics/cache/)

- The overhead in some requests can be significant when your site starts getting more and more traffic. This is where **caching** becomes precious. By caching queries, calculation results, or rendered content in an HTTP request, you will avoid expensive operations in the following requests. This translates into shorter response times and less processing on the server side.

- Django includes a robust cache system that allows you to cache data with different levels of granularity. You can cache a single query, the output of a specific view, parts of rendered template content, or your entire site. Items are stored in the cache system for a default time. You can specify the default timeout for cached data.

- Django comes with several cache backends. These are the following:

  - `backends.memcached.MemcachedCache` or `backends.memcached.PyLibMCCache`: A Memcached backend. Memcached is a fast and efficient memory-based cache server. The backend to use depends on the Memcached Python bindings you choose.
  - `backends.db.DatabaseCache`: Use the database as a cache system.
  - `backends.filebased.FileBasedCache`: Use the file storage system. This serializes and stores each cache value as a separate file.
  - `backends.locmem.LocMemCache`: A local memory cache backend. This the default cache backend.
  - `backends.dummy.DummyCache`: A dummy cache backend intended only for development. It implements the cache interface without actually caching anything. This cache is per-process and thread-safe.

- For optimal performance, use a memory-based cache backend such as the Memcached backend.

### Memcached

- Configuring the cache:

```py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

- Extending Django Admin Panel to show addition info about cache usage:

```py
# use memcache admin index site
admin.site.index_template = 'memcache_status/admin_index.html'
```

- Cache levels provided by Django:

  - Low-level cache API: Provides the highest granularity. Allows you to cache specific queries or calculations.
  - Template cache: Allows you to cache template fragments.
  - Per-view cache: Provides caching for individual views.
  - Per-site cache: The highest-level cache. It caches your entire site.

#### Low-level Cache API

```py
subjects = cache.get('all_subjects')
if not subjects:
    subjects = Subject.objects.annotate(
                   total_courses=Count('courses'))
    cache.set('all_subjects', subjects)
```

- Caching based on dynamic data:

```py
def get(self, request, subject=None):
    subjects = cache.get('all_subjects')
    if not subjects:
        subjects = Subject.objects.annotate(
                        total_courses=Count('courses'))
        cache.set('all_subjects', subjects)
    all_courses = Course.objects.annotate(
                        total_modules=Count('modules'))
    if subject:
        subject = get_object_or_404(Subject, slug=subject)
        key = f'subject_{subject.id}_courses'  # dynamic key creation
        courses = cache.get(key)
        if not courses:
            courses = all_courses.filter(subject=subject)
            cache.set(key, courses)
    else:
        courses = cache.get('all_courses')
        if not courses:
            courses = all_courses
            cache.set('all_courses', courses)
    return self.render_to_response({'subjects': subjects,
                                    'subject': subject,
                                    'courses': courses})
```

#### Caching Template Fragments

```html
{% load cache %}
...
{% cache 600 module_contents module %}
  {% for content in module.contents.all %}
    {% with item=content.item %}
      <h2>{{ item.title }}</h2>
      {{ item.render }}
    {% endwith %}
  {% endfor %}
{% endcache %}
```

#### Caching Views

```py
from django.views.decorators.cache import cache_page

path('course/<pk>/',
     cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
     name='student_course_detail'),
path('course/<pk>/<module_id>/',
     cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
     name='student_course_detail_module'),
```

### Redis Cache

- [django-rediq](https://github.com/jazzband/django-redis)

- Redis Cache will become a default Django Cache starting from version 4.0.

- Installation: `python -m pip install django-redis`.

- Configuration:

```py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

## Configuration

### Development Server Through HTTPS

- The Django development server is not able to serve your site through HTTPS, since that is not its intended use. In order to test the social authentication functionality serving your site through HTTPS, you are going to use the RunServerPlus extension of the package Django Extensions. **Django Extensions** is a third-party collection of custom extensions for Django. Please note that this is never the method you should use to serve your site in a real environment; this is a development server.

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

- First, you subclass the Feed class of the syndication framework. The title, link, and description attributes correspond to the `<title>`, `<link>`, and `<description>` RSS elements, respectively.

- Add RSS feed into the URLs:

```py
from .feeds import LatestPostsFeed

urlpatterns = [
    # ...
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
```

### Full-Text Search

- [Details about below implementations](https://learning.oreilly.com/library/view/django-3-by/9781838981952/Text/Chapter_3.xhtml#_idParaDest-69)
- [PostgreSQL Full-Text Search](https://www.postgresql.org/docs/12/textsearch.html)
- [Full-Text Search and Performance in Django](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/search/)
- [Modular Search for Django with Haystack](https://django-haystack.readthedocs.io/en/master/) - it features a unified, familiar API that allows you to plug in different search backends (such as Solr, Elasticsearch, Whoosh, Xapian, etc.) without having to modify the code.

- Searching for data in the database with user input is a common task for web applications. The Django ORM allows you to perform simple matching operations using, for example, the `contains` filter (or its case-insensitive version, `icontains`):

```py
from blog.models import Post
Post.objects.filter(body__contains='framework')
```

- However, if you want to perform complex search lookups, retrieving results by similarity, or by weighting terms based on how frequently they appear in the text or by how important different fields are (for example, relevancy of the term appearing in the title versus in the body), you will need to use a full-text search engine. When you consider large blocks of text, building queries with operations on a string of characters is not enough. Full-text search examines the actual words against stored content as it tries to match search criteria.

- Django provides a powerful search functionality built on top of PostgreSQL's full-text search features. The django.contrib.postgres module provides functionalities offered by PostgreSQL that are not shared by the other databases that Django supports.

#### Simple Search Lookups

```py
from blog.models import Post
Post.objects.filter(body__search='django')
```

#### Searching Against Mltiple Fields

```py
from django.contrib.postgres.search import SearchVector
from blog.models import Post
Post.objects.annotate(
    search=SearchVector('title', 'body'),
).filter(search='django')
```

#### Stemming and Ranking Results

```py
search_vector = SearchVector('title', 'body')
search_query = SearchQuery(query)
results = Post.published.annotate(
              search=search_vector,
              rank=SearchRank(search_vector, search_query)
          ).filter(search=search_query).order_by('-rank')
```

#### Weighting Queries

```py
search_vector = SearchVector('title', weight='A') + \
                SearchVector('body', weight='B')
search_query = SearchQuery(query)
results = Post.published.annotate(
 rank=SearchRank(search_vector, search_query)
 ).filter(rank__gte=0.3).order_by('-rank')
```

#### Searching with Trigram Similarity

```py
results = Post.published.annotate(
    similarity=TrigramSimilarity('title', query),
).filter(similarity__gt=0.1).order_by('-similarity')
```

### Translations

- To internationalize your project do the following:

  1. Mark strings for translation in your Python code and your templates.
  2. Run the `makemessages` command to create or update message files that include all translation strings from your code.
  3. Translate the strings contained in the message files and compile them using the `compilemessages` management command.

- To translate literals in your Python code, you can mark strings for translation using the `gettext()` function included in `django.utils.translation`. This function translates the message and returns a string. The convention is to import this function as a shorter alias named `_` (underscore character).

- Django includes **lazy** versions for all of its translation functions, which have the suffix `_lazy()`. When using the lazy functions, strings are translated when the value is accessed, rather than when the function is called (this is why they are translated **lazily**). The lazy translation functions come in handy when strings marked for translation are in paths that are executed when modules are loaded.

- By using placeholders, you can reorder the text variables. For example, an English translation of the previous example might be today is April 14, while the Spanish one might be hoy es 14 de Abril. Always use string interpolation instead of positional interpolation when you have more than one parameter for the translation string. By doing so, you will be able to reorder the placeholder text.

```py
from django.utils.translation import gettext as _
month = _('April')
day = '14'
output = _('Today is %(month)s %(day)s') % {'month': month,
                                            'day': day}
```

- Creating message files for defined languages `django-admin makemessages --all`.

- Compiling messages `django-admin compilemessages`.

#### Translation Template Tags

- Django offers the `{% trans %}` and `{% blocktrans %}` template tags to translate strings in templates. In order to use the translation template tags, you have to add `{% load i18n %}` at the top of your template to load them.

```py
{% trans "Text to be translated" %}`

# OR

{% trans "Hello!" as greeting %}
<h1>{{ greeting }}</h1>
```

- The `{% blocktrans %}` template tag allows you to mark content that includes literals and variable content using placeholders. The following example shows you how to use the {% blocktrans %} tag, including a name variable in the content for translation:

```py
{% blocktrans %}Hello {{ name }}!{% endblocktrans %}
```

#### Rosetta

- **Rosetta** is a third-party application that allows you to edit translations using the same interface as the Django administration site. Rosetta makes it easy to edit `.po` files and it updates compiled translation files. Let's add it to your project.

### Recommendation Engine

- Recommendation engine that suggests products that are usually bought together. You will suggest products based on historical sales, thus identifying products that are usually bought together. You are going to suggest complementary products in two different scenarios:

  - **Product detail page**: You will display a list of products that are usually bought with the given product. This will be displayed as users who bought this also bought X, Y, Z. You need a data structure that allows you to store the number of times that each product has been bought together with the product being displayed.
  - **Cart detail page**: Based on the products users add to the cart, you are going to suggest products that are usually bought together with these ones. In this case, the score you calculate to obtain related products has to be aggregated.

- [Example of recommendation engine](https://learning.oreilly.com/library/view/django-3-by/9781838981952/Text/Chapter_9.xhtml) and [Chapter 09](https://github.com/PacktPublishing/Django-3-by-Example/blob/master/Chapter09/myshop/shop/recommender.py) in Django 3 by Example GitHub.

## Redis

- **Redis** is an advanced key/value database that allows you to save different types of data. It also has extremely fast I/O operations. Redis stores everything in memory, but the data can be persisted by dumping the dataset to disk every once in a while, or by adding each command to a log. Redis is very versatile compared to other key/value stores: it provides a set of powerful commands and supports diverse data structures, such as strings, hashes, lists, sets, ordered sets, and even bitmaps or HyperLogLogs.

- Although SQL is best suited to schema-defined persistent data storage, Redis offers numerous advantages when dealing with rapidly changing data, volatile storage, or when a quick cache is needed.

### Redis with Django

- The convention for naming Redis keys is to use a colon sign as a separator for creating namespaced keys. By doing so, the key names are especially verbose and related keys share part of the same schema in their names.

- Configuration in Django settings:

```py
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
```

- Setting up connection to Redis Sever:

```py
# In views.py
import redis
from django.conf import settings
# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)
```

### Storing a view count in Redis

```py
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    # increment total image views by 1
    total_views = r.incr(f'image:{image.id}:views')
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image,
                   'total_views': total_views})
```

### Storing a ranking in Redis

```py
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    # increment total image views by 1
    total_views = r.incr(f'image:{image.id}:views')
    # increment image ranking by 1
    r.zincrby('image_ranking', 1, image.id)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image,
                   'total_views': total_views})

@login_required
def image_ranking(request):
    # get image ranking dictionary
    image_ranking = r.zrange('image_ranking', 0, -1,
                             desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    # get most viewed images
    most_viewed = list(Image.objects.filter(
                           id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    return render(request,
                  'images/image/ranking.html',
                  {'section': 'images',
                   'most_viewed': most_viewed})
```

## Celery

- **Celery** is a distributed task queue that can process vast amounts of messages. Using Celery, not only can you create asynchronous tasks easily and let them be executed by workers as soon as possible, but you can also schedule them to run at a specific time.

- There are several options for a message broker for Celery, including key/value stores such as Redis, or an actual message system such as **RabbitMQ**. RabbitMQ is the recommended message worker for Celery. RabbitMQ is lightweight, it supports multiple messaging protocols, and it can be used when scalability and high availability are required.

### Adding Celery to the Project

- You have to provide a configuration for the Celery instance. Create a new file next to the `settings.py` file of myshop and name it `celery.py`. This file will contain the Celery configuration for your project. Add the following code to it:

```py
import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

- This code does the following:

    - You set the `DJANGO_SETTINGS_MODULE` variable for the Celery command-line program.
    - You create an instance of the application with `app = Celery('myshop')`.
    - You load any custom configuration from your project settings using the `config_from_object()` method. The namespace attribute specifies the prefix that Celery-related settings will have in your `settings.py` file. By setting the `CELERY` namespace, all Celery settings need to include the `CELERY_` prefix in their name (for example, `CELERY_BROKER_URL`).
    - Finally, you tell Celery to auto-discover asynchronous tasks for your applications. Celery will look for a `tasks.py` file in each application directory of applications added to INSTALLED_APPS in order to load asynchronous tasks defined in it.

- You need to import the celery module in the `__init__.py` file of your project to make sure it is loaded when Django starts. Edit the `myshop/__init__.py` file and add the following code to it:

```py
import celery
from .celery import app as celery_app
```

- The `CELERY_ALWAYS_EAGER` setting allows you to execute tasks locally in a synchronous way, instead of sending them to the queue. This is useful for running unit tests or executing the application in your local environment without running Celery.

### Asynchronous Task Example

- Create a new file inside the orders application and name it `tasks.py`. This is the place where Celery will look for asynchronous tasks. Add the following code to it:

```py
from celery import task
from django.core.mail import send_mail
from .models import Order
@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
```

- In the `view.py` you should add `order_created.delay(order.id)`- You call the `delay()` method of the task to execute it asynchronously.

- Use `celery -A myshop worker -l info` in a shell to see logs from Celery workers.

### Monitoring Celery with Flower

- You might want to monitor the asynchronous tasks that are executed. **Flower** is a web-based tool for monitoring Celery.

### Braintree

- [Docs](https://developer.paypal.com/braintree/docs/guides/hosted-fields/overview/javascript/v3)

- [Braintree Sandbox](https://www.braintreepayments.com/pl/sandbox)

- [Braintree Python](https://github.com/braintree/braintree_python)

### Outputting PDF

- [Outputting PDFs with Django](https://docs.djangoproject.com/en/3.2/howto/outputting-pdf/)

- [WeasyPrint](https://doc.courtbouillon.org/weasyprint/latest/first_steps.html)

## Django Rest Framework (DRF)

### Adding Additional Actions to ViewSets

- You can add extra actions to viewsets:

```py
from rest_framework.decorators import action
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    @action(detail=True,
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})
```

- Modifying `urls.py`:

```py
path('courses/<pk>/enroll/',
     views.CourseEnrollView.as_view(),
     name='course_enroll'),
```

- Actions can be also used to alter default behaviours of the given ViewSet methods. For instance mimicing `retrieve()` method, but using different serializer:

```py
from .permissions import IsEnrolled
from .serializers import CourseWithContentsSerializer
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    # ...
    @action(detail=True,
            methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```

### Creating Custom Permissions

Django provides a `BasePermission` class that allows you to define the following methods (these methods should return `True` to grant access, or `False` otherwise):

  - `has_permission()`: View-level permission check
  - `has_object_permission()`: Instance-level permission check

```py
from rest_framework.permissions import BasePermission
class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
```

## Django Channels

- Django 3 comes with support for running asynchronous Python through ASGI, but it does not yet support asynchronous views or middleware. However, as mentioned, Channels extends Django to handle not only HTTP, but also protocols that require long-running connections, such as WebSockets and chatbots.

- **WebSockets** provide full-duplex communication by establishing a persistent, open, bidirectional Transmission Control Protocol (TCP) connection between servers and clients. You are going to use WebSockets to implement your chat server.

- **Channels** replaces Django's request/response cycle with messages that are sent across channels. HTTP requests are still routed to view functions using Django, but they get routed over channels. This allows for WebSockets message handling as well, where you have producers and consumers that exchange messages across a channel layer. Channels preserves Django's synchronous architecture, allowing you to choose between writing synchronous code and asynchronous code, or a combination of both.

- Channels expects you to define a single root application that will be executed for all requests. You can define the root application by adding the ASGI_APPLICATION setting to your project. This is similar to the ROOT_URLCONF setting that points to the base URL patterns of your project. You can place the root application anywhere in your project, but it is recommended to put it in a project-level file named `routing.py`:

```py
from channels.routing import ProtocolTypeRouter
application = ProtocolTypeRouter({
    # empty for now
})

# Then, add the following line to the settings.py file of your project:
ASGI_APPLICATION = 'educa.routing.application'
```

- When Channels is added to the `INSTALLED_APPS` setting, it takes control over the runserver command, replacing the standard Django development server. Besides handling URL routing to Django views for synchronous requests, the Channels development server also manages routes to WebSocket consumers.

- Steps to run asynchronous application via Channels:

    - **Set up a consumer**: Consumers are individual pieces of code that can handle WebSockets in a very similar way to traditional HTTP views. You will build a consumer to read and write messages to a communication channel.
    - **Configure routing**: Channels provides routing classes that allow you to combine and stack your consumers. You will configure URL routing for your chat consumer.
    - **Implement a WebSocket client**: When the student accesses the chat room, you will connect to the WebSocket from the browser and send or receive messages using JavaScript.
    - **Enable a channel layer**: Channel layers allow you to talk between different instances of an application. They're a useful part of making a distributed real-time application. You will set up a channel layer using Redis.

### Writing a Consumer

```py
import json
from channels.generic.websocket import WebsocketConsumer
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # accept connection
        self.accept()
    def disconnect(self, close_code):
        pass
    # receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send message to WebSocket
        self.send(text_data=json.dumps({'message': message}))
```

### Routing

- Channels provides routing classes that allow you to combine and stack consumers to dispatch based on what the connection is. You can think of them as the URL routing system of Django for asynchronous applications.

- Create a new file inside the `chat` application directory and name it `routing.py`. Add the following code to it:

```py
from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/chat/room/(?P<course_id>\d+)/$', consumers.ChatConsumer),
]
```

- It is a good practice to prepend WebSocket URLs with `/ws/` to differentiate them from URLs used for standard synchronous HTTP requests. This also simplifies the production setup when an HTTP server routes requests based on the path.

- Edit the global `routing.py` file located next to the `settings.py` file so that it looks like this:

```py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
```

### Implementing The WebSocket Client

- This part is specific to the used front-end client.

### Enabling a Channel Layer

- Channel layers allow you to communicate between different instances of an application. A channel layer is the transport mechanism that allows multiple consumer instances to communicate with each other and with other parts of Django.

- Channel layers provide two abstractions to manage communications: channels and groups:

    - **Channel**: You can think of a channel as an inbox where messages can be sent to or as a task queue. Each channel has a name. Messages are sent to a channel by anyone who knows the channel name and then given to consumers listening on that channel.
    - **Group**: Multiple channels can be grouped into a group. Each group has a name. A channel can be added or removed from a group by anyone who knows the group name. Using the group name, you can also send a message to all channels in the group.

#### Setting up a channel layer with Redis

- Redis is the preferred option for a channel layer, though Channels has support for other types of channel layers. Redis works as the communication store for the channel layer.

```py
# pip install channels-redis==2.4.2
# Edit the settings.py file of the educa project and add the following code to it:

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}

# editing a consumer class
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id
        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # accept connection
        await self.accept()
    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        )
    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))
```

- Above you pass the following information in the event sent to the group:

    - `type`: The event type. This is a special key that corresponds to the name of the method that should be invoked on consumers that receive the event. You can implement a method in the consumer named the same as the message type so that it gets executed every time a message with that specific type is received.
    - `message`: The actual message you are sending.


## Django App Deployment

### Heroku

- [Example of Django app deployment on Heroku](https://www.youtube.com/watch?v=qPtScmB8CgA&t=2588s)

- In `settings.py` add following:

```py
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

- Install `django-heroku` and add in `settings.py`:

```py
import django_heroku
import dj_database_url

DATABASES = {"default": dj_database_url.config()}
django_heroku.settings(locals())
```

- Add heroku PostgreSQL database to the application:

```bash
heroku addons:create heroku-postgresql:hobby-dev
```
