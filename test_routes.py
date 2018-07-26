from routes import app
import unittest


class FlaskTestCase(unittest.TestCase):
	def setup(self):
		tester = app.test_client(self)
	def test_signup(self):
		tester = app.test_client(self)
		response = tester.get('/auth/signup', content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
	def test_login(self):
		tester = app.test_client(self)
		response = tester.get('/auth/login', content_type = 'application/json')
		self.assertEqual(response.status_code, 400)
	def test_add_entry(self):
		tester = app.test_client(self)
		response = tester.get('/entries/<int:id>', content_type = 'application/json')
		self.assertEqual(response.status_code, 404)
	def test_update_entry(self):
		tester = app.test_client(self)
		response = tester.get('/entries/<int:id>', content_type = 'application/json')
		self.assertEqual(response.status_code, 404)
	def test_get_entries(self):
		tester = app.test_client(self)
		response = tester.get('/entries', content_type = 'application/json')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()
