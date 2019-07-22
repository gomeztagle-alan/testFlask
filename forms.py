from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UsersForm(FlaskForm):
  email_address = StringField('Email Address', validators=[DataRequired()])
  password = IntegerField('Password', validators=[DataRequired()])
  submit = SubmitField('Enter')
  forgot = SubmitField('Forgot Password')
