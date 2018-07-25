from flask import Flask, request, jsonify, json, make_response
from functools import wraps
from database import UserDb, EntryDb




app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'

dummy_entries = []
users = [{}]

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
		new_dict = {'fullname':fullname, 'username':username, 'email':email, 'password':confirm_password}
		users.append(new_dict)
	except:
		return 'please include all the required data'
	return jsonify({'message':'you are now registered and have an account'})

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
	'''
	this route calls a view function that checks whether anindividual is registered
	and logs them in
	'''
	user_id = len(users) - 1
	email = request.get_json()['email']
	password = request.get_json()['password']
	if email == users[user_id]['email'] and password in users[user_id]['password']:
		return jsonify({'message':'you are now logged in'})
	else:
		return jsonify({'message':'you need to register before logging in'})


@app.route('/entries', methods = ['GET', 'POST'])
def create_entry():
	'''
	This view function creates a new entry and adds it to the list of dictionaries
	go to postman and using a POST method, add a dictionary within the body containing 
	five keys title, date, time, content and data_id..then add in values of your own choosing
	'''
	try:
		title = request.get_json()['title']
		date = request.get_json()['date']
		time = request.get_json()['time']
		content = request.get_json()['content']
		data_id = request.get_json()['data_id']
		new_dict = {'title':title, 'date':date, 'time':time, 'content':content, 'data_id':data_id}
		dummy_entries.append(new_dict)
		json_str = json.dumps(dummy_entries)
	except:
		return jsonify({'message': 'please include all the required data'})
	return jsonify({'current_len':len(dummy_entries)})

@app.route('/entries', methods = ['GET', 'POST'])
def get_entries():
	'''
	This view function returns all the diary entries
	'''
	return jsonify(dummy_entries)

@app.route('/entries/<int:entryId>', methods = ['GET', 'POST'])
def get_entry(id):
	'''
	This view function displays a specific entry using an id
	'''
	return jsonify(dummy_entries[id])



@app.route('/entries/<int:entryId>', methods = ['GET','PUT'])
def delete_entry(id):
	'''
	#This view function deletes a particular diary entry from the database
	'''
	return jsonify(dummy_entries[id])



if __name__ == '__main__':
	app.run(debug = True)