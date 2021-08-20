# Wed Development With Flask

## Sources

- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Flask Course - Python Web Application Development](https://www.youtube.com/watch?v=Qr4QMBUPxWo)

## Project Structure

- Flask app should be structured like a regular python package. All code should be stored in a seperate folder with ```__init__.py``` file in it that will ensure that no **circular imports** happen within the code.

- ```__init__.py``` should initiate app:

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes
```

- Application should be run from a seperate file (not located in the package itself) that will just execute an app stored in a package:

```python
from market import app

if __name__ == '__main__':
    app.run(debug=True)
```

### Flask Blueprints

- In Flask, a blueprint is a logical structure that represents a subset of the application. A blueprint can include elements such as routes, view functions, forms, templates and static files. If you write your blueprint in a separate Python package, then you have a component that encapsulates the elements related to specific feature of the application. You can think of a blueprint as a temporary storage for application functionality that helps in organizing your code.

- The creation of a blueprint is fairly similar to the creation of an application. This is done in the *___init__.py* module of the blueprint package:

```python
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
```

- The Blueprint class takes the name of the blueprint, the name of the base module (typically set to `__name__` like in the Flask application instance). After the blueprint object is created, I import the *handlers.py* module, so that the error handlers in it are registered with the blueprint. This import is at the bottom to avoid circular dependencies.

- Registering blueprint in the main app:

```python
app = Flask(__name__)
# ...
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)  # `url_prefix` argument can be used to define URL prefix
```

- When defining routes in a blueprint, the `@bp.route` decorate is used instead of `@app.route`. There is also a required change in the syntax used in the `url_for()` to build URLs. For regular view functions attached directly to the application, the first argument to `url_for()` is the view function name. When a route is defined in a blueprint, **this argument must include the blueprint name and the view function name, separated by a period**. So for example, I had to replace all occurrences of `url_for('login')` with `url_for('auth.login')`.

- The `current_app` variable that Flask provides is a special "context" variable that Flask initializes with the application before it dispatches a request. This makes it easy for view functions to access the application instance without having to import it: `from flask import current_app`.

## Application Development

- Starting flask server:

```bash
# in terminal
export FLASK_APP=hello.py
# in powershell
[set] $env:FLASK_APP = "hello.py"

# additionally following variables can be set
# to allow automated reloads whenever change is made
# in terminal
$env:FLASK_ENV=development
# in powershell
$env:FLASK_ENV = "development"
# to start a server with a debug mode being on
$env:FLASK_DEBUG = 1

flask run
```

- Terminal variables are not remembered so in order to skip manual setting of the variables create *.flaskenv* file and populate it with desired varialbes and use ```pip install python-dotenv```.

- Simple flask app:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')  # home.html is stored in 'templates' directory
```

- The ```@app.route``` can use dynamic patterns which is indicated as the ```<username>``` URL component that is surrounded by < and >. When a route has a dynamic component, Flask will accept any text in that portion of the URL, and will invoke the view function with the actual text as an argument:

```python
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)
```

- One interesting aspect of the ```url_for()``` function is that you can add any keyword arguments to it, and if the names of those arguments are not referenced in the URL directly, then Flask will include them in the URL as query arguments:

```python
@app.route('/user/<username>')
@login_required
def user(username):
    ...
    url_for('user', page=posts.prev_num)  # 'page' will be passed as a query argument
    # 'username' will be  matched with the <username> within the route
    url_for('user', username=current_user)
```

- Static files in Flask should be located in *app/static* and can be accessed with: `url_for('static', filename='loading.gif')`.

- Environment variables should be stored in a config and can be loaded with *python-dotenv* package.

### User Authentication

- Form part in routes is the same as for the registration part.

- In *forms.py* within the appropriate form class created for user login additional validations should be included to check provided user name and password. Such validation can also be included as part of the routes within the ```validate_on_submit``` if clase:

```python
def validate_username(self, username):
    if User.query.filter_by(username=username.data).first() is None:
        raise ValidationError(message='This username does not exist.')

def validate_password(self, password):
    candidate = User.query.filter_by(username=self.username.data).first().password_hash
    if not bcrypt.check_password_hash(candidate, password.data):
        raise ValidationError(message='Incorrect username and password.')
```

- To initiate login functionality use ```flask_login``` module:

```python
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
```

- Within the *models* callback function should be located:

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

- To skip manual implementation of methods required by Flask in the ```User``` class we can inherit from ```UserMixin``` class that provides implementation of these methods.

- After a successful validation user should be created:

```python
user = User.query.filter_by(username=form.username.data).first()
login_user(user)
```

- Indication of routes accessible only by logged users requires ```@login_required``` decorator. In order to render desired view configure ```LoginManager()``` instance by setting its ```login_view``` property. If custom functionality is required for handling unauthorized users use ```unauthorized_handler(callback)```:

```python
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message = 'Please login before accessing this page.'
login_manager.login_message_category = 'info'
```

- ```logout_user()``` will logout the user.

- ```current_user``` provides properties that allow for checking authentication status of the current user such as ```curent_user.is_authenticated``` and ```curent_user.is_anonymous```. ```curent_user``` is accessible via Jinja syntax as well.

### Models and Databases

- Flask has a dedicated wrapper for SQLAlchemy which is ```flask-sqlalchemy```.

- Basic config for SQLAlchemy:

```python
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
```

- Creating a table 'Item' with desired fields:

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=15), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    # This is not an actual database field, but a high-level view of the relationship
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
```

- For a one-to-many relationship, a ```db.relationship``` field is normally defined on the "one" side, and is used as a convenient way to get access to the "many".

- In order to initiate a database file use in a python console:

```python
from market import db
db.create_all()
```

- Adding items via Python console:

```python
from market import db
from market import Item
item1 = Item(name='phone', price=500, barcode='12345', description='dummy descr')
db.session.add(item1)
db.session.commit()
```

- To query a database to show all of the items ```Item.query.all()```.

- To query a table by item's ID ```User.query.get(1)```.

- Default representation of an object in a table can be changed by overwriting ```__repr__``` function within a model class:

```python
def __repr__(self):
        return f'Item {self.name}'
```

- Filtering of a table can be done with ```Item.query.filter_by(price=500)```.

- To delete entire database: ```db.drop_all()```.

- If custom table name should be given it can be done via ```__tablename__ = 'name'```.

- We often need to run queries outside of the application to check functionality of our app/models. In orde to do so we can choose one of the following:

```python
# First option: In opened Python session
from market import db
from market.models import User, Item

# Second option (in run.py)
from market import app, db
from market.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

flask shell  # to run Python session in the Flask application context
```

#### Migrations

- Working with a relational databases can be made simpler by using Alembic which handles all database schema changes:

```python
# Using Flask-Migrate wrapper for Alembic
from flask_migrate import Migrate
migrate = Migrate(app, db)

# In terminal
flask db init  # creates structure for the db migration
flask db migrate -m 'comment'  # first db migration (generates migration script only)
flask db upgrade  # run migration script making required changes
```

- Migration workflow in short: ```changes to the models -> run db migrate -> run db upgrade```. Run ```db downgrade``` in case of any issues.

### Flask Forms

- Installing WTForms:

```bash
pip install flask-wtf
pip install wtforms
```

- Forms require configuration of a secret key in Flask:

```python
# generating 12-bit long secret key with os module
os.urandom(12).hex()
# adding a secret key configuration in flask app
app.config['SECRET_KEY'] = '66efeae7789c36c34266d5d1'
```

- Above is fine, but additional separation will improve the structure of code:

```python
# in config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '66efeae7789c36c34266d5d1'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# in __init__.py
from config import Config

app =Flask(__name__)
app.config.from_object(Config)
```

- Creating a Flask form with validators. Custom validators can be added as a function within the form's class - it is best to name such function in a following pattern: 'validate_[field_name]'. This way validating function does not need to be included in the ```validators``` argument since it will be automatically found and executed by Flask WTForms:

```python
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    # this validation will be automatically executed for 'username' field
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() != None:
            raise ValidationError(message='This username is already in use.')

    username = StringField(
        label='User Name:',
        validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(
        label='Email Address:',
        validators=[Email(), DataRequired()])
    password1 = PasswordField(
        label='Password:',
        validators=[Length(min=4), DataRequired()])
    password2 = PasswordField(
        label='Confirm Password:',
        validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
```

- To generate an HTML version of a form fields call attributes of the passed form class using Jinja syntax:

```python
# 'form' is an instantiated RegisterForm class
# that has been passed to a render_template() as an argument
{{ form.username.label() }}
# each field can be passed HTML attributes as arguments
{{ form.username(class="form-control", placeholder="User Name") }}
```

- The ```form.hidden_tag()``` template argument generates a hidden field that includes a token that is used to protect the form against **CSRF attacks**.

- Form route needs to accept both GET and POST methods. Form validation will automatically detect what kind of a request it is and act accordingly:

```python
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    # flask.request.form is automatically passed here
    form = RegisterForm()
    # shortcut for form.is_submitted() and form.validate()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            possword=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()

        # user can be automatically logged in after successful registration
        login_user(user_to_create)
        flash(  'User has been created successfully! You are now logged in to the page.',
                category='info')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f'Following error occured when trying to create the user: {err_msg}',
                category='danger')
    return render_template('register.html', form=form)
```

- In the ```User``` class password property needs to be added which ensures that within a database only hashed password will be stored:

```python
@property
def password(self):
    return self.password

@password.setter
def password(self, plain_txt_pw):
    self.password_hash = bcrypt.generate_password_hash(plain_txt_pw).decode('utf-8')
```

- Above requires ```bcrypt``` initiation:

```python
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
```

- When we want to use 'submit' button in order to confirm and post some information to backend we can use define form with a single button in it. If specific submission needs to be assigned to a specific object, additional hidden input tag should be added in the form with value that needs to be received by backend:

```html
<form method="POST">
    {{ purchase_form.hidden_tag() }}
    <input id="purchased_item" name="purchased_item" type="hidden" value="{{ item.name }}">
    <div class="d-grid">
        {{ purchase_form.submit(class="btn btn-primary") }}    
    </div>
</form>
```

- Value from the hidden input can be grabbed by ```request.form['field_name']```.

```python
@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if purchase_form.validate_on_submit():
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.assign_buyer(current_user)
                flash(f'You purchased {p_item_object.name} for {p_item_object.price}', category='info')
            else:
                flash(f'You do not have sufficient funds on your account!', category='danger')
        return redirect(url_for('market_page'))
    
    if request.method == 'GET':
        items = Item.query.filter_by(owner=None)
    return render_template('market.html', items=items, purchase_form=purchase_form, sell_form=sell_form)
```

- Validation of requirements can be included as a method within a given object's blueprint (f.e. user class):

```python
# in user class
def can_purchase(self, item_to_purchase):
    return self.budget >= item_to_purchase.price
```

- Similarly action of object assignment to another object should be done using object method:

```python
# in item class
def assign_buyer(self, buyer):
    self.owner = buyer.id
    buyer.budget -= self.price
    db.session.commit()
```

- ```request.method``` is a Flask's request property that stores a request type and can be used to alter behaviour of the route depending on the taken action.

### Flash

- ```flash``` function in flask allows for passing the messages to the app that can later be rendered in the page template with Jinja:

```python
# routes.py
flash(
    f'Following error occured when trying to create the user: {err_msg},'category='danger')

# base.html
# 'with' create a new inner scope for variables
# get_flashed_messages() grabs all of the messages passed to the template
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

## Jinja

- Variable block in a print statement: ```{{ }}```.

- Instruction block:

```python
{# Comments here #}
{% for i in range(10) %}
    <p>Item number {{ i + 1 }}>
{% endfor %}
```

- To access attributes of a variable, in addition to a standard Python ```__getitem__``` syntax (```[]```), dot syntax (```.```) can be used.

- Defining an inner scope is done with ```with``` block:

```python
{% with var1 = 2 %}
    {{ var1 }}
{% endwith %}
# var1 is not accessible outside of the with block scope
```

- Setting a variable is done with a ```set``` keyword: ```{% set var1 = 'value' %}```.

- To capture the contents of a block into a variable use `set` as a block:

```python
{% set navigation %}
    <li><a href="/">Index</a>
    <li><a href="/downloads">Downloads</a>
{% endset %}
# 'navigation' variable is now available for use in template
```

### Template Inheritance

- In order to inherit HTML code from base/template use ```{% extends 'base.html' %}```.

- ```{% block block_name %}``` indicates unique elements in the base template from which other pages will inherit:

```python
# in the base.html
<title>
    {% block title %}

    {% endblock %}
</title>

# in the home.html
{% block title %}
    Home Page
{% endblock %}
```

- URLs should not be hardcoded inside the templates, but instead ```url_for('page_generating_func')``` should be used.

### Jinja Add-Ons

- HTML elements that should be included in the given page, but might be too verbose, can be included with the ```{% include 'includes/html_page.html' %}``` syntax. Those HTML chunks will have access to all of the variables within the context that they are spawned in. This is also useful when same code appears on different pages - in case of changes in the code those need to be done in a single template. Such components should be stored in a separate folder like *subtemplates*.
