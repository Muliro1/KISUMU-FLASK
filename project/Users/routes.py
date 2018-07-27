from flask import Flask, request, jsonify, json, make_response
from functools import wraps
import jwt
import datetime
from database import UserDb, EntryDb
from flask import  Blueprint
from database import UserDb
from project.Users.utils import token_required

users = Blueprint('Users', __name__)



@users.route('/auth/signup', methods = ['GET', 'POST'])
def register():
	'''
	this route enables an individual to register
	'''
	try:
		fullname = request.get_json()['fullname']
		username = request.get_json()['username']
		email = request.get_json()['email']
		password = request.get_json()['password']
		confirm_password = request.get_json()['confirm_password']
		user_db.c.execute('''
			INSERT into Users (fullname, username, email, password)
			VALUES({}, {}, {}, {})
			''').format(fullname, username, email, password)
		user_db.save()
		user_db.close()
	except:
		return jsonify({'message':'Unable to connect to database'})
	return jsonify({'message':'you are now registered and have an account'})

@users.route('/auth/login', methods = ['GET', 'POST'])
def login():
	'''
	this route calls a view function that checks whether anindividual is registered
	and logs them in
	'''
	auth = request.authorization
	user_db.c.execute('''
		SELECT email, password FROM Users
		''')
	rows = user_db.c.fetchall()
	user_db.save()
	user_db.close()
	email = request.get_json()['email']
	password = request.get_json()['password']
	if auth and auth.password == password:
		token = jwt.encode({'password':auth.password, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes = 1440)}, app.config['SECRET_KEY'])
		return jsonify({'token':token.decode('UTF-8')})
	else:
		return jsonify({'message':'could not verify'})