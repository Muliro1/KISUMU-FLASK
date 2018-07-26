from flask import Flask, request, jsonify, json, make_response
from functools import wraps
from database import UserDb, EntryDb




app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'

user_db = UserDb()
user_db.create_table()
entry_db = EntryDb()
entry_db.create_table()

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
	user_db.c.execute('''
		SELECT email, password FROM Users
		''')
	rows = user_db.c.fetchall()
	user_db.save()
	user_db.close()
	email = request.get_json()['email']
	password = request.get_json()['password']
	if email in rows and password in rows:
		return jsonify({'message':'you are now logged in'})
	else:
		return jsonify({'message':'you need to register before logging in'})


@app.route('/entries', methods = ['GET', 'POST'])
def create_entry():
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

@app.route('/entries', methods = ['GET', 'POST'])
def get_entries():
	'''
	This view function returns all the diary entries
	'''
	entry_db.c.execute('''
		SELECT * FROM Entries
		''')
	rows = entry_db.c.fetchall()
	user_db.save()
	user_db.close()
	return jsonify({rows})

@app.route('/entries/<int:entryId>', methods = ['GET', 'POST'])
def get_entry(entryId):
	'''
	This view function displays a specific entry using an id
	'''
	entry_db.c.execute('''
		SELECT * FROM Entries WHERE id = %d
		''') %(entryId )
	output = entry_db.c.fetchall()
	return jsonify({output})



@app.route('/entries/<int:entryId>', methods = ['GET','PUT'])
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



if __name__ == '__main__':
	app.run(debug = True)