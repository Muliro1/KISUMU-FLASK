import psycopg2
from psycopg2.extensions import connection
from flask import Blueprint
database = Blueprint('database', __name__)


class UserDb(psycopg2.extensions.connection):
	def __init__(self, db = "MY DIARY", user = "postgres", host = "localhost", password = "relapse92", port = 5432):
		self.conn = psycopg2.connect(database = db, user = user, host = host, password = password, port = port)
		self.c = self.conn.cursor()
	def create_table(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS Users(
    	fullname varchar (40) NOT NULL,
    	username varchar (20) NOT NULL,
    	email varchar (60) NOT NULL,
    	password varchar (4) NOT NULL,
    	id SERIAL PRIMARY KEY
                    )''')
	def save(self):
		self.conn.commit()
	def close(self):
		self.c.close
		

class EntryDb(psycopg2.extensions.connection):
	def __init__(self, db = "MY DIARY", user = "postgres", host = "localhost", password = "relapse92", port = 5432):
		self.conn = psycopg2.connect(database = db, user = user, host = host, password = password, port = port)
		self.c = self.conn.cursor()
	def create_table(self):
		self.c = self.conn.cursor()
		self.c.execute('''CREATE TABLE IF NOT EXISTS Entries(
    	title varchar (20) NOT NULL,
    	day  varchar (10) NOT NULL,
    	time_of  varchar (60) NOT NULL,
    	content varchar (200) NOT NULL
                    )''')
	def save(self):
		self.conn.commit()
	def close(self):
		self.c.close()

		     


	

    
   




