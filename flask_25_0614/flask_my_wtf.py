from wtforms import Form, StringField, SubmitField, BooleanField, TextAreaField,PasswordField
from wtforms.validators import DataRequired,Length

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(message='姓名不可以为空哦')])
    password = PasswordField('Password', validators=[DataRequired(),Length(8,128)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')