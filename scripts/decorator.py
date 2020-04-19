# Key takewaways:
# * use functools.wraps not to lose the __name__ and documentation of the given function
# * use *args and **kwargs to be able to pass functions with as many parameters as you'd like

from functools import wraps

user = {'username': 'someone', 'access_level': 'guest'}


def make_secure(func):
    @wraps(func) #makes sure
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No admin permissions for {user["username"]}.'

    return secure_function


@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'


print(get_password.__name__)  # this prints "secure_function" if @wraps is not used.
print(get_password('billing'))
