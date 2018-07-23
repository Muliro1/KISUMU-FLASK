from routes import app
import unittest
import coverage

class FlaskTestCase(unittest.TestCase):
	def setup(self):
		tester = app.test_client(self)
	def test_login(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)
	def test_logout(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/create_entry', content_type = 'html/text')
		self.assertEqual(response.status_code, 500)
	def test_info(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/<int:id>', content_type = 'html/text')
		self.assertEqual(response.status_code, 404)
	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/entries/delete_entry/<int:id>', content_type = 'html/text')
		self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
	unittest.main()