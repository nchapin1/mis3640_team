from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    """Registration form."""
    username = StringField("Username:", [DataRequired()])
    email = StringField('Email', [DataRequired()])
    phone = StringField("Username:", [DataRequired()])
    password = StringField("Password", [DataRequired()])

    submit = SubmitField("Submit")