blogs = {}


def menu():
    print_blogs()

def print_blogs():
    i = 0
    for title in blogs.keys():
        print(f'{i} - {title}')
        i += 1

if __name__ == '__main__':
    menu()