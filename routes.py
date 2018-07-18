from flask import Flask, render_template, url_for, flash, redirect, request, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'



@app.route('/api/v1/register', methods = ['GET', 'POST'])
def register():
	'''
	This view function displays a registration form for users to register a new account
	'''
	return render_template('index.html')

@app.route('/api/v1/login', methods = ['GET', 'POST'])
def login():
	'''
	This view function displays a registration form for users to log into their account
	'''
	return render_template('login.html')

@app.route('/api/v1/entries', methods = ['GET', 'POST'])
def get_entries():
	'''
	This view function displays all diary entries
	'''
	return render_template('entries.html')

@app.route('/api/v1/entries/entry', methods = ['GET', 'POST'])
def get_entry():
	'''
	This view function displays a specific entry
	'''
	return render_template('account.html')

@app.route('/api/v1/entries/create_entry', methods = ['GET', 'POST'])
def create_entry():
	'''
	This view function displays a form for creating diary entries
	'''
	return render_template('create_diary.html')

@app.route('/api/v1/entries/delete_entry', methods = ['PUT', 'POST'])
def delete_entry():
	'''
	This view function displays a form for editing a specific diary entry
	'''
	return render_template('account.html')


if __name__ == '__main__':
	app.run(debug = True)