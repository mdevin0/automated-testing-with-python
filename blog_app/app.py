from blog import Blog
from post import Post


# Program data
MENU = '''
Options:
c - create a blog
l - list existing blogs
r - read a blog
q - quit
'''

POST_TEMPLATE = '''
--- {} ---

{}
'''

blogs = []


def menu():
    option = None
    while option != 'q':
        option = input(MENU).lower()
        if option == 'c':
            pass
        elif option == 'l':
            list_blogs()
        elif option == 'r':
            read_blog()
        else:
            print(f'Invalid option {option}')
            
    print('Thanks for using the blog app!')

def list_titles(data: list):
    i = 0
    for item in data:
        print(f'{i} - {item.title}')
        i += 1

def list_blogs():
    list_titles(blogs)

def read_blog():
    list_blogs()
    option = None
    while True:
        option = input('Which blog would you like to read? (number to select or "b" to go back)').lower()
        try:
            if option == 'b':
                return
            else:
                list_posts(blogs[int(option)])
        except (ValueError, IndexError):
            print(f'Invalid option {option}')

def list_posts(blog: Blog):
    list_titles(blog.posts)
    option = None
    while True:
        option = input('Which post would you like to read? (number to select or "b" to go back)').lower()
        try:
            if option == 'b':
                return
            else:
                display_post(blog.posts[int(option)])
        except (ValueError, IndexError):
            print(f'Invalid option {option}')

def display_post(post: Post):
    print(POST_TEMPLATE.format(post.title, post.content))
    

        

if __name__ == '__main__':
    menu()