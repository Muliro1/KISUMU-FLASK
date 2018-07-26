from flask import Flask, request, jsonify, json, make_response
from functools import wraps
import jwt
import datetime
from database import UserDb, EntryDb




app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'

user_db = UserDb()
user_db.create_table()
entry_db = EntryDb()
entry_db.create_table()

def token_required(f):
	def decorated(*args, **kwargs):
		token = request.args.get('token')
		if not token:
			return jsonify({'message':'token is missing!'}), 403
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message':'token is invalid'}), 403
		return f(*args, **kwargs)
	return decorated

@app.route('/auth/signup', methods = ['GET', 'POST'])
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

@app.route('/auth/login', methods = ['GET', 'POST'])
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

@token_required
@app.route('/entries', methods = ['POST'])
def add_entry():
	'''
	This view function creates a new entry and adds it to the database
	go to postman and using a POST method, add a dictionary within the body containing 
	five keys title, date, time, content and data_id..then add in values of your own choosing
	'''
	try:
		title = request.get_json()['title']
		date = request.get_json()['date']
		time = request.get_json()['time']
		content = request.get_json()['content']
		data_id = request.get_json()['data_id']
		entry_db.c.execute('''
	    	INSERT INTO Entries(title, day, time_of, content)
	    	VALUES({}, {}, {}, {})
	    	''').format(title, date, time, content)
		entry_db.save()
		entry_db.close()
	except:
		return jsonify({'message': 'please include all the required data'})
	return jsonify({'current_len':len(dummy_entries)})
@token_required
@app.route('/entries', methods = ['GET'])
def get_entries():
	'''
	This view function returns all the diary entries
	'''
	entry_db.c.execute('''
		SELECT * FROM Entries
		''')
	values = entry_db.c.fetchall()
	user_db.save()
	user_db.close()
	keys = ['title', 'date', 'time', 'content']
	new_dict = {k: v for k, v in zip(keys, values)}
	return jsonify(new_dict)
@token_required
@app.route('/entries/<int:entryId>', methods = ['GET'])
def get_entry(entryId):
	'''
	This view function displays a specific entry using an id
	'''
	entry_db.c.execute('''
		SELECT * FROM Entries WHERE id = %d
		''') %(entryId )
	output = entry_db.c.fetchall()
	return jsonify({output})


@token_required
@app.route('/entries/<int:entryId>', methods = ['PUT'])
def update_entry(entryId):
	'''
	#This view function deletes a particular diary entry from the database
	'''
	title = request.get_json()['title']
	date = request.get_json()['date']
	time = request.get_json()['time']
	content = request.get_json()['content']
	data_id = request.get_json()['data_id']
	entry_db.c.execute('''
		UPDATE Entries SET title = %s, day = %s, time_of = %s, content = %s
		WHERE id = %d
		''') %(title, date, time, content, entryId)
	entry_db.save()
	entry_db.commit()
	return jsonify({'message':'you have successfully updated the entry'})



