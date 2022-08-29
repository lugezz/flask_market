from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, user_to_check): #Flask va a buscar automaticamente los métodos que empiecen con "validate"
        #Y va a controlar los que siga después del guión bajo.
        user = User.query.filter_by(username=user_to_check.data)

        if user.count() > 0:
            raise ValidationError('Username already exists, try a different one')

    def validate_email_address(self, email_to_check): #Flask va a buscar automaticamente los métodos que empiecen con "validate"
        #Y va a controlar los que siga después del guión bajo.
        email = User.query.filter_by(email_address=email_to_check.data)

        if email.count() > 0:
            raise ValidationError('Email Address already exists, try a different one')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

