import psycopg2


class UserDb():
	def connect(self):
		try:
			self.conn = psycopg2.connect(host="localhost",database="MY DIARY", user="postgres", password="relapse92", port = 58270)
		except:
			return ("Unable to connect to database")
	def create_table():
		c = conn.cursor()
		c.execute('''CREATE TABLE Users(
    	fullname varchar (40) NOT NULL,
    	username varchar (20) NOT NULL,
    	email varchar (60) NOT NULL,
    	password varchar (4) NOT NULL,
    	id SERIAL PRIMARY KEY

                    ''')
	def insert_data(self, var1, var2, var3, var4):
		c = conn.cursor()
		c.commit()
		c.close()

class EntryDb():
	def connect(self):
		try:
			self.conn = psycopg2.connect(host="localhost",database="MY DIARY", user="postgres", password="relapse92", port = 58270)
		except:
			return ("Unable to connect to database")
	def create_table():
		c = conn.cursor()
		c.execute('''CREATE TABLE Entries(
    	title varchar (20) NOT NULL,
    	day date varchar (10) NOT NULL,
    	time_of time varchar (60) NOT NULL,
    	content varchar (200) NOT NULL,
    	id SERIAL PRIMARY KEY

                    ''')
		c.commit()
		c.close()       


	

    
   




