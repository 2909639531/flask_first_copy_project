import flask
from flask_my_wtf import LoginForm
from flask import redirect,render_template,request,flash,url_for

app = flask.Flask(__name__)

app.secret_key = "密钥"


@app.route('/',methods=['GET','POST'])
def index():
    form = LoginForm()
    return flask.render_template('index.html', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return flask.render_template('login.html',username=username,password=password)