# -*- coding: utf-8 -*-

from wtforms import Form, StringField, validators


class LoginForm(Form):
    username = StringField('Username:', [validators.DataRequired(), validators.Length(min=1, max=30)])
    password = StringField('Password:', [validators.DataRequired(), validators.Length(min=1, max=30)])
    email = StringField('Email:', [validators.optional(), validators.Length(min=0, max=50)])