from flask import Flask, request, jsonify, json, make_response

app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'

from project.Users.routes import users
from project.Entries.routes import entries

app.register_blueprint(entries)
app.register_blueprint(users)