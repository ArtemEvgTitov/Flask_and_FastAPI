from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])


class RegisterForm(FlaskForm):
    """
    ● StringField — строковое поле для ввода текста;
    ● IntegerField — числовое поле для ввода целочисленных значений;
    ● FloatField — числовое поле для ввода дробных значений;
    ● BooleanField — чекбокс;
    ● SelectField — выпадающий список;
    ● DateField — поле для ввода даты;
    ● FileField — поле для загрузки файла.
    """
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'),
                                            ('female', 'Женщина')])


class RegistrationForm(FlaskForm):
    # pip install email-validator
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])
