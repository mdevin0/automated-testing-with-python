from unittest import TestCase

from rest_api.main.app import app
from rest_api.main.db import db

class TestBase(TestCase):
    def setUp(self):
        # Make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        
        # Get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    # Runs at the end of each test
    def tearDown(self):
        # makes sure database is blank for next tests
        with app.app_context():
            db.session.remove()
            db.drop_all()