from project.Users.routes import entries
import unittest


class FlaskTestCase(unittest.TestCase):
	def setup(self):
		tester = entries.test_client(self)
	def test_signup(self):
		tester = entries.test_client(self)
		response = tester.get('/auth/signup', content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
	def test_login(self):
		tester = entries.test_client(self)
		response = tester.get('/auth/login', content_type = 'application/json')
		self.assertEqual(response.status_code, 400)