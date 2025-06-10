from flask import Flask,render_template,flash,redirect,url_for,request
from forms import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username == 'admin' and password == '123456':
            flash(f"Hi,{username}!",)
            return redirect(url_for('index'))
        else:
            flash('出了点问题哦')
            return render_template('login.html',form=form,error='1')

    return render_template('login.html',title='登录',form=form,error='')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)