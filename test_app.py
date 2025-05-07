import unittest
from main import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello CI/CD! This is a simple Flask application.", response.data)
if __name__ == '__main__':
    unittest.main()
