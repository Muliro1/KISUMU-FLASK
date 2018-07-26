import psycopg2
from psycopg2.extensions import connection


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
                    );''')
	def save(self):
		self.conn.commit()
	def close(self):
		self.c.close