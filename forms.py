from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

class SearchForm(Form):
    search = TextField('Search', [DataRequired()])

class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class ProofPointForm(Form):
    customerCompany = TextField('customerCompany', [DataRequired()])
    customerIndustry = TextField('customerIndustry', [DataRequired()])
    customerProject = TextField('customerProject', [DataRequired()])
    customerProjectDescription = TextField('customerProjectDescription', [DataRequired()])
    useCase = TextField('useCase', [DataRequired()])