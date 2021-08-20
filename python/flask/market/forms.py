from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
from market import bcrypt


class RegisterForm(FlaskForm):

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() != None:
            raise ValidationError(message='This username is already in use.')

    def validate_email_address(self, email_address):
        if User.query.filter_by(email_address=email_address.data).first() != None:
            raise ValidationError(message='This email address is already in use.')

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


class LoginForm(FlaskForm):

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is None:
            raise ValidationError(message='This username does not exist.')

    def validate_password(self, password):
        password_hash = User.query.filter_by(username=self.username.data).first().password_hash
        if not bcrypt.check_password_hash(password_hash, password.data):
            raise ValidationError(message='Incorrect username and password.')
    
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')
