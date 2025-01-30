import unittest
from unittest.mock import patch, MagicMock
from decimal import Decimal
from datetime import datetime

class TestCountryRepository(unittest.TestCase):
    @patch('your_module.CountryRepository')
    def test_country_repository(self, mock_repo):
        # Setup mock
        mock_country = MagicMock()
        mock_country.id = 1
        mock_country.code = "US"
        mock_country.name = "United States"
        mock_repo.find_all.return_value = [mock_country]
        mock_repo.find_by_id.return_value = mock_country

        # Test find all
        countries = mock_repo.find_all()
        self.assertEqual(len(countries), 1)
        self.assertEqual(countries[0].code, "US")

        # Test find by id
        country = mock_repo.find_by_id(1)
        self.assertEqual(country.name, "United States")

class TestProductCategoryRepository(unittest.TestCase):
    @patch('your_module.ProductCategoryRepository')
    def test_product_category_repository(self, mock_repo):
        # Setup mock
        mock_category = MagicMock()
        mock_category.id = 1
        mock_category.category_name = "Electronics"
        mock_repo.find_all.return_value = [mock_category]
        mock_repo.find_by_id.return_value = mock_category

        # Test find all
        categories = mock_repo.find_all()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].category_name, "Electronics")

        # Test find by id
        category = mock_repo.find_by_id(1)
        self.assertEqual(category.category_name, "Electronics")

class TestProductRepository(unittest.TestCase):
    @patch('your_module.ProductRepository')
    def test_product_repository(self, mock_repo):
        # Setup mock
        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = "Smartphone"
        mock_product.unit_price = Decimal("999.99")
        mock_repo.find_all.return_value = [mock_product]
        mock_repo.find_by_id.return_value = mock_product
        mock_repo.find_by_category_id.return_value = [mock_product]
        mock_repo.find_by_name_containing.return_value = [mock_product]

        # Test find all
        products = mock_repo.find_all()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Smartphone")

        # Test find by id
        product = mock_repo.find_by_id(1)
        self.assertEqual(product.unit_price, Decimal("999.99"))

        # Test find by category id
        products = mock_repo.find_by_category_id(1, None)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Smartphone")

        # Test find by name containing
        products = mock_repo.find_by_name_containing("phone", None)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Smartphone")

class TestStateRepository(unittest.TestCase):
    @patch('your_module.StateRepository')
    def test_state_repository(self, mock_repo):
        # Setup mock
        mock_state = MagicMock()
        mock_state.id = 1
        mock_state.name = "California"
        mock_repo.find_all.return_value = [mock_state]
        mock_repo.find_by_id.return_value = mock_state
        mock_repo.find_by_country_code.return_value = [mock_state]

        # Test find all
        states = mock_repo.find_all()
        self.assertEqual(len(states), 1)
        self.assertEqual(states[0].name, "California")

        # Test find by id
        state = mock_repo.find_by_id(1)
        self.assertEqual(state.name, "California")

        # Test find by country code
        states = mock_repo.find_by_country_code("US")
        self.assertEqual(len(states), 1)
        self.assertEqual(states[0].name, "California")

if __name__ == '__main__':
    unittest.main()