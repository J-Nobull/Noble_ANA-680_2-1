import unittest
from app680_21 import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Optionally check for expected content:
        # self.assertIn(b"some expected text", response.data)

if __name__ == "__main__":
    unittest.main()
