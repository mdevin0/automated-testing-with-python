from unittest import TestCase
from unittest.mock import patch
import builtins

import app
from blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Testing', 'Test Author')
        app.blogs = {blog.title: blog}
        
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('0 - Testing')