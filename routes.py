from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'

dummy_entries = []

@app.route('/api/v1/entries/create_entry', methods = ['GET', 'POST'])
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

@app.route('/api/v1/entries', methods = ['GET', 'POST'])
def get_entries():
	'''
	This view function returns all the diary entries
	'''
	return jsonify(dummy_entries)

@app.route('/api/v1/entries/<int:id>', methods = ['GET', 'POST'])
def get_entry(id):
	'''
	This view function displays a specific entry using an id
	'''
	return jsonify(dummy_entries[id])



@app.route('/api/v1/entries/delete/<int:id>', methods = ['GET','DELETE'])
def delete_entry(id):
	'''
	#This view function deletes a particular diary entry from the database
	'''
	dummy_entries.pop(id)
	return jsonify({'message':'you have deleted an entry'})



if __name__ == '__main__':
	app.run(debug = True)