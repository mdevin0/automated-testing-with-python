from unittest import TestCase
from unittest.mock import patch, call
import builtins

from blog_app.main import app
from blog_app.main.blog import Blog
from blog_app.main.post import Post

class AppTest(TestCase):
    def test_list_data_called_with_blogs(self):
        b1 = Blog('First Blog', 'Me')
        b2 = Blog('Second Blog', 'Me Too')
        blogs = [b1, b2]
        expected_blog_prints = [call('0 - First Blog'), call('1 - Second Blog')]

        with patch('builtins.print') as mocked_print:
            app.list_titles(blogs)
            mocked_print.assert_has_calls(expected_blog_prints)

    def test_list_data_called_with_posts(self):
        p1 = Post('First Post', 'Me')
        p2 = Post('Second Post', 'Me too')
        posts = [p1, p2]
        expected_post_prints = [call('0 - First Post'), call('1 - Second Post')]

        
        with patch('builtins.print') as mocked_print:
            app.list_titles(posts)
            mocked_print.assert_has_calls(expected_post_prints)