### make the forms here

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of pup: ')
    submit = SubmitField('add ze pup')

class DelForm(FlaskForm):

    id = IntegerField('id num of pup to remove:')
    submit = SubmitField('remove ze pup')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of owner:')
    pup_id = IntegerField('id of pup:')
    submit = SubmitField('add owner')
