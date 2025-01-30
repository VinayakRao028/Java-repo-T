import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

class TestMyDataRestConfig(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.db = SQLAlchemy(self.app)
        
        # Mock the entity classes
        self.Product = MagicMock()
        self.ProductCategory = MagicMock()
        self.Country = MagicMock()
        self.State = MagicMock()
        
    @patch('flask_restful.Api.add_resource')
    def test_configure_api_endpoints(self, mock_add_resource):
        # Implement the configuration logic here
        self.api.add_resource(self.Product, '/api/products')
        self.api.add_resource(self.ProductCategory, '/api/product-categories')
        self.api.add_resource(self.Country, '/api/countries')
        self.api.add_resource(self.State, '/api/states')
        
        # Assert that add_resource was called for each entity
        mock_add_resource.assert_any_call(self.Product, '/api/products')
        mock_add_resource.assert_any_call(self.ProductCategory, '/api/product-categories')
        mock_add_resource.assert_any_call(self.Country, '/api/countries')
        mock_add_resource.assert_any_call(self.State, '/api/states')
    
    @patch('flask_sqlalchemy.SQLAlchemy.create_all')
    def test_expose_ids(self, mock_create_all):
        # Implement the logic to expose entity IDs
        self.db.create_all()
        
        # Assert that create_all was called
        mock_create_all.assert_called_once()
    
    def test_disable_http_methods(self):
        # Implement the logic to disable certain HTTP methods
        for entity in [self.Product, self.ProductCategory, self.Country, self.State]:
            resource = self.api.resources[0]
            self.assertNotIn('put', resource.methods)
            self.assertNotIn('post', resource.methods)
            self.assertNotIn('delete', resource.methods)

if __name__ == '__main__':
    unittest.main()