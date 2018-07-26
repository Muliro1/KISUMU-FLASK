import psycopg2


class UserDb():
	def __init__(self, db = "MY DIARY", user = "postgres", host = "localhost", password = "relapse92", port = 5432):
		self.conn = psycopg2.connect(database = db, user = user, host = host, password = password, port = port)
		self.c = self.conn.cursor()
	def create_table(self):
		self.c.execute('''CREATE TABLE Users(
    	fullname varchar (40) NOT NULL,
    	username varchar (20) NOT NULL,
    	email varchar (60) NOT NULL,
    	password varchar (4) NOT NULL,
    	id SERIAL PRIMARY KEY

                    ''')
		self.c.commit()
	def save(self):
		self.c.commit()
	def close(self):
		self.c.close
		

class EntryDb():
	def __init__(self, db = "MY DIARY", user = "postgres", host = "localhost", password = "relapse92", port = 5432):
		self.conn = psycopg2.connect(database = db, user = user, host = host, password = password, port = port)
		self.c = self.conn.cursor()
	def create_table(self):
		self.c = conn.cursor()
		self.c.execute('''CREATE TABLE Entries(
    	title varchar (20) NOT NULL,
    	day date varchar (10) NOT NULL,
    	time_of time varchar (60) NOT NULL,
    	content varchar (200) NOT NULL,
    	id SERIAL PRIMARY KEY

                    ''')
	def save(self):
		self.c.commit()
	def close(self):
		self.c.close()

		     


	

    
   




