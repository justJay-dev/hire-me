from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import Email, InputRequired, Length
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
    email = EmailField('Email Address', validators=[InputRequired(), Length(min=4, max=80)])
    message = TextAreaField('Message', validators=[InputRequired()])
