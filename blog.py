class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'<Bost Title: {self.title}, Author: {self.author}, Posts: {self.posts}>'

    
    def create_post(self, title, content):
        pass

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'blogs': self.posts,
        }