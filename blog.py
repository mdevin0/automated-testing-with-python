from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        s = 's' if len(self.posts) != 1 else ''
        return f'<Post - Title: {self.title}, Author: {self.author}, Posts: {len(self.posts)} post{s}>'

    
    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }
