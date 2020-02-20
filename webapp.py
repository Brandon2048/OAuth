from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from flask import render_template

import pprint
import os

app = Flask(__name__)

app.debug = True #Change this to False for production

app.secret_key = os.environ['SECRET_KEY'] 
oauth = OAuth(app)












if __name__ == '__main__':
    app.run()
