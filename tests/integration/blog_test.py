from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Post Title', 'Post Content')

        self.assertEqual(1, len(blog.posts))
        self.assertEqual('Post Title', blog.posts[0].title)
        self.assertEqual('Post Content', blog.posts[0].content)

    def test_json(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test Post', 'Test Content')
        
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {'title': 'Test Post', 'content': 'Test Content'}
            ]
        }

        self.assertDictEqual(expected, blog.json())

    def test_json_no_posts(self):
        blog = Blog('Test', 'Test Author')
        expected = {'title': 'Test', 'author': 'Test Author', 'posts': []}

        self.assertDictEqual(expected, blog.json())

    
