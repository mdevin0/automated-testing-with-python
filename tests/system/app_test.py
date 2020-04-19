'''
Key takeaways
    * The method setUp() runs before every test method, but it won't reset global variables. For example, if app.blogs.append() 
    were used instead of assigning a new list, 'app' would have an additional post on every test run.
'''

from unittest import TestCase
from unittest.mock import patch, call
import builtins

import app
from blog import Blog
from post import Post

class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Blog Title', 'Blog Author')
        app.blogs = [blog]

    def test_print_menu(self):
        with patch('builtins.input', return_value = 'q') as mocked_input:
            app.menu()
            mocked_input.assert_called_once_with(app.MENU)

    def test_list_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.list_blogs()
            mocked_print.assert_called_with('0 - Blog Title')

    def test_read_post(self):
        app.blogs[0].create_post('Post Title', 'Post content.')
        expected_post_print = app.POST_TEMPLATE.format('Post Title', 'Post content.')

        with patch('builtins.print') as mocked_print:
            with patch('builtins.input', side_effect = ('r', '0', '0', 'b', 'b', 'q')) as mocked_input:
                app.menu()
                expected_input_calls = [
                    call(app.MENU),
                    call('Which blog would you like to read? (number to select or "b" to go back)'),
                    call('Which post would you like to read? (number to select or "b" to go back)'),
                ]
                mocked_input.assert_has_calls(expected_input_calls)
                mocked_print.assert_any_call(expected_post_print)