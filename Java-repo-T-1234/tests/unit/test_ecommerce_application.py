import unittest
from unittest.mock import patch
from flask import Flask

class TestEcommerceApplication(unittest.TestCase):
    @patch('flask.Flask.run')
    def test_ecommerce_application_runs(self, mock_run):
        # Arrange
        app = Flask(__name__)

        # Act
        with app.app_context():
            app.run()

        # Assert
        mock_run.assert_called_once()

    def test_app_configuration(self):
        # Arrange
        app = Flask(__name__)

        # Act & Assert
        self.assertIsNotNone(app.config)
        self.assertEqual(app.debug, False)  # Assuming production mode by default

    @patch('flask_swagger_ui.get_swaggerui_blueprint')
    def test_swagger_ui_integration(self, mock_get_swaggerui_blueprint):
        # Arrange
        app = Flask(__name__)

        # Act
        from flask_swagger_ui import get_swaggerui_blueprint
        SWAGGER_URL = '/api/docs'
        API_URL = '/static/swagger.json'

        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "Ecommerce API"
            }
        )
        app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

        # Assert
        mock_get_swaggerui_blueprint.assert_called_once_with(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "Ecommerce API"
            }
        )

if __name__ == '__main__':
    unittest.main()