from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')

        self.assertEqual('Test', blog.title)
        self.assertEqual('Test Author', blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog = Blog('Test', 'Test Author')
        expected = f'<Blog - Title: Test, Author: Test Author, Posts: 0 posts>'

        self.assertEqual(expected, blog.__repr__())
        
        
        blog2 = Blog('Test 2', 'Test Author 2')
        blog2.posts.append('something')
        expected2 = f'<Blog - Title: Test 2, Author: Test Author 2, Posts: 1 post>'

        self.assertEqual(expected2, blog2.__repr__())
