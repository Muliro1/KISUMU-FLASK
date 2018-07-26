from flask import Flask, request, jsonify, json, make_response
from functools import wraps
import jwt
import datetime
from database import UserDb, EntryDb
from flask import Blueprint
from project.Entries.utils import token_required
from database import EntryDb

entries = Blueprint('Entries', __name__)



@token_required
@entries.route('/entries', methods = ['POST'])
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
@entries.route('/entries', methods = ['GET'])
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
@entries.route('/entries/<int:entryId>', methods = ['GET'])
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
@entries.route('/entries/<int:entryId>', methods = ['PUT'])
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