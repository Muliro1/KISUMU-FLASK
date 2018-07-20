from flask import Flask, render_template, url_for, flash, redirect, request, jsonify

app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'

dummy_entries = dummy_entries = [{'title':'bleach',
                  'date' :'12/09/1992',
                  'time' :'4.00 pm', 
                  'content' :'Kurosaki Ichigo',
                  'id' : 1             
                  },{
                   'title':'Naruto',
                  'date' :'13/09/1992',
                  'time' :'4.02 pm', 
                  'content' :'Uzumaki Naruto',
                  'id' : 2
                  }]


@app.route('/api/v1/entries', methods = ['GET', 'POST'])
def get_entries():
	'''
	This view function returns all the diary entries
	'''
	return jsonify(dummy_entries[1], dummy_entries[0])

@app.route('/api/v1/entries/<int:id>', methods = ['GET', 'POST'])
def get_entry(id):
	'''
	This view function displays a specific entry using an id
	'''
	return jsonify(dummy_entries[id])

@app.route('/api/v1/entries/create_entry', methods = ['GET', 'POST'])
def create_entry():
	'''
	This view function creates a new entry and adds it to the list of dictionaries
	'''
	dummy_entries.append(jsonify(request.args))
	return jsonify({'current_len':len(dummy_entries)})

@app.route('/api/v1/entries/delete/<int:id>', methods = ['GET','DELETE'])
def delete_entry(id):
	'''
	#This view function deletes a particular diary entry from the database
	'''
	dummy_entries.pop(id)
	return jsonify({'current_len':len(dummy_entries)})



if __name__ == '__main__':
	app.run(debug = True)