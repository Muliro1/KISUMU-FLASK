from routes import app
import unittest

class FlaskTestCase(unittest.TestCase):
	def setup(self):
		tester = app.test_client(self)

	def test_login(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/login', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	def test_login_loads(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/login', content_type = 'html/text')
		self.assertTrue(b'Username:' in response.data)

	def test_logout(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/login', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	def test_logout_loads(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/login', content_type = 'html/text')
		self.assertTrue(b'Username:' in response.data)

	def test_entries(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/entry', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	def test_entries_loads(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/entry', content_type = 'html/text')
		self.assertTrue(b'Entries' in response.data)

	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/create_entry', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	def test_home_loads(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/create_entry', content_type = 'html/text')
		self.assertTrue(b'entry title :' in response.data)

	def test_delete(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/delete_entry', content_type = 'html/text')
		self.assertEqual(response.status_code, 405)



if __name__ == '__main__':
	unittest.main()