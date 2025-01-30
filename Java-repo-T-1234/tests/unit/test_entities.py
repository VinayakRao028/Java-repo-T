import unittest
from decimal import Decimal
from datetime import datetime
from unittest.mock import Mock

# Mock classes for testing
class Country:
    def __init__(self, id, code, name):
        self.id = id
        self.code = code
        self.name = name
        self.states = []

class Product:
    def __init__(self, id, category, sku, name, description, unit_price, image_url, active, units_in_stock, date_created, last_updated):
        self.id = id
        self.category = category
        self.sku = sku
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.image_url = image_url
        self.active = active
        self.units_in_stock = units_in_stock
        self.date_created = date_created
        self.last_updated = last_updated

class ProductCategory:
    def __init__(self, id, category_name):
        self.id = id
        self.category_name = category_name
        self.products = set()

class State:
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country

class TestCountry(unittest.TestCase):
    def test_country_attributes(self):
        country = Country(id=1, code="US", name="United States")
        self.assertEqual(country.id, 1)
        self.assertEqual(country.code, "US")
        self.assertEqual(country.name, "United States")
        self.assertEqual(country.states, [])

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.category = ProductCategory(id=1, category_name="Electronics")
        self.product = Product(
            id=1,
            category=self.category,
            sku="PROD001",
            name="Smartphone",
            description="Latest model smartphone",
            unit_price=Decimal("999.99"),
            image_url="http://example.com/smartphone.jpg",
            active=True,
            units_in_stock=100,
            date_created=datetime.now(),
            last_updated=datetime.now()
        )

    def test_product_attributes(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.sku, "PROD001")
        self.assertEqual(self.product.name, "Smartphone")
        self.assertEqual(self.product.description, "Latest model smartphone")
        self.assertEqual(self.product.unit_price, Decimal("999.99"))
        self.assertEqual(self.product.image_url, "http://example.com/smartphone.jpg")
        self.assertTrue(self.product.active)
        self.assertEqual(self.product.units_in_stock, 100)
        self.assertIsInstance(self.product.date_created, datetime)
        self.assertIsInstance(self.product.last_updated, datetime)

class TestProductCategory(unittest.TestCase):
    def test_product_category_attributes(self):
        category = ProductCategory(id=1, category_name="Electronics")
        self.assertEqual(category.id, 1)
        self.assertEqual(category.category_name, "Electronics")
        self.assertEqual(category.products, set())

class TestState(unittest.TestCase):
    def test_state_attributes(self):
        country = Country(id=1, code="US", name="United States")
        state = State(id=1, name="California", country=country)
        self.assertEqual(state.id, 1)
        self.assertEqual(state.name, "California")
        self.assertEqual(state.country, country)

if __name__ == '__main__':
    unittest.main()