from flask import Flask
app = Flask(__name__)

from my_app.hello.views import hello

app.register_blueprint(hello)