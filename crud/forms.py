from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from crud.models import User
class AddForm(FlaskForm):
    firstname= StringField('First name', validators=[DataRequired(),Length(min=2, max=20)])
    lastname= StringField('Last name', validators=[DataRequired(),Length(min=2, max=20)])
    title= StringField('Designation', validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email', validators=[DataRequired(),Email()])
    number= StringField('Mobile',validators=[DataRequired(), Length(min=10, max=10)],)
    about=TextAreaField('About', render_kw={"rows": 4, "cols": 4} , validators=[DataRequired(), Length(max=200)])
    submit= SubmitField('Submit')

    def validate_number(self,number):
        if (not (number.data).isnumeric()):
            raise ValidationError('Enter Valid Number')
        else:
            user=User.query.filter_by(number=number.data).first()
            if user:
                raise ValidationError('Number already exists in DataBase')
    def validate_email(self,email):
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exists in DataBase')

class UpdateForm(FlaskForm):
    firstname= StringField('First name', validators=[DataRequired(),Length(min=2, max=20)])
    lastname= StringField('Last name', validators=[DataRequired(),Length(min=2, max=20)])
    title= StringField('Designation', validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email', validators=[DataRequired(),Email()])
    number= StringField('Mobile',validators=[DataRequired(), Length(min=10, max=10)],)
    about=TextAreaField('About', render_kw={"rows": 4, "cols": 4} , validators=[DataRequired(), Length(max=200)])
    submit= SubmitField('Update')

    def validate_number(self,number):
        if (not (number.data).isnumeric()):
            raise ValidationError('Enter Valid Number')
        else:
            user=User.query.filter_by(number=number.data).first()
            if user:
                raise ValidationError('Number already exists in DataBase')
    def validate_email(self,email):
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exists in DataBase')

class Searchform(FlaskForm):
    firstname=StringField('First name',validators=[DataRequired()])
    lastname= StringField('Last name(Optional)')