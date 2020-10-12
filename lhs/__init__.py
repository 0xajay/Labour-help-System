from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from datetime import timedelta
from mongoengine import connect
# from werkzeug.contrib.fixers import ProxyFix
import os
import gc

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.wsgi_app = ProxyFix(app.wsgi_app)
jwt = JWTManager(app) #binding JWT to handle jwt
db = connect(host=os.environ.get('MONGO_URI'))

@app.teardown_request
def teardown(Exception):
    gc.collect()

from lhs.modules.users.routes import users

app.register_blueprint(users,url_prefix='/api/v1/user') #registering user blueprint

# @app.route("/")
# def index():
#     return render_template("api.html")
