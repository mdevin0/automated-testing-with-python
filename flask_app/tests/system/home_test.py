'''
Key takeaways:
    * assertEqual() will call assertDictEqual() if two dictonaries are given as parameters.
'''

import json

from flask_app.tests.system.base_test_class import BaseTest

class TestHome(BaseTest):
    def test_home(self):
        with self.app as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': 'Wow, this is an app!'}
            )
