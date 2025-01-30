import unittest
import requests
from unittest.mock import patch, MagicMock

BASE_URL = "http://localhost:8080/api"  # Adjust this to your actual API base URL

class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    @patch('requests.get')
    def test_get_countries(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "_embedded": {
                "countries": [
                    {"id": 1, "code": "US", "name": "United States"},
                    {"id": 2, "code": "CA", "name": "Canada"}
                ]
            }
        }
        mock_get.return_value = mock_response

        response = self.session.get(f"{BASE_URL}/countries")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("_embedded", data)
        self.assertIn("countries", data["_embedded"])
        self.assertEqual(len(data["_embedded"]["countries"]), 2)

    @patch('requests.get')
    def test_get_product_categories(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "_embedded": {
                "productCategory": [
                    {"id": 1, "categoryName": "Books"},
                    {"id": 2, "categoryName": "Electronics"}
                ]
            }
        }
        mock_get.return_value = mock_response

        response = self.session.get(f"{BASE_URL}/product-category")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("_embedded", data)
        self.assertIn("productCategory", data["_embedded"])
        self.assertEqual(len(data["_embedded"]["productCategory"]), 2)

    @patch('requests.get')
    def test_get_products(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "_embedded": {
                "products": [
                    {"id": 1, "name": "Product 1", "description": "Description 1", "unitPrice": 19.99},
                    {"id": 2, "name": "Product 2", "description": "Description 2", "unitPrice": 29.99}
                ]
            }
        }
        mock_get.return_value = mock_response

        response = self.session.get(f"{BASE_URL}/products")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("_embedded", data)
        self.assertIn("products", data["_embedded"])
        self.assertEqual(len(data["_embedded"]["products"]), 2)

    @patch('requests.get')
    def test_get_states(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "_embedded": {
                "states": [
                    {"id": 1, "name": "California"},
                    {"id": 2, "name": "New York"}
                ]
            }
        }
        mock_get.return_value = mock_response

        response = self.session.get(f"{BASE_URL}/states")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("_embedded", data)
        self.assertIn("states", data["_embedded"])
        self.assertEqual(len(data["_embedded"]["states"]), 2)

if __name__ == '__main__':
    unittest.main()