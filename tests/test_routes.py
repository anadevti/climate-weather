import unittest
from app import create_app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_weather_api(self):
        response = self.client.post('/', data=dict(city='London'))
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
