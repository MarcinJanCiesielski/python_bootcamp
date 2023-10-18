class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False
    

new_user = User("Marcin")

def authenticate_decorator(function):
    def wrapper(*args, **kwargs):
        args[0].is_logged_in = True
        return function(args[0])
    return wrapper

@authenticate_decorator
def create_blog_post(user):
    if user.is_logged_in:
        print(f"Post for user {user.name} was created")


create_blog_post(new_user)
