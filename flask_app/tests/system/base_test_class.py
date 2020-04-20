'''
Key takeaways:
* This is a base class to reuse stuff on testing classes. 
It should have a different pattern than the test classes (e.g., in this case, different than *_test).
Hence, the "_class" at the end of this file name.
'''

from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True # tells Flask we're testing the app, so errors are handled differently
        self.app = app.test_client()