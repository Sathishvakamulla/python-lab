from functools import wraps

is_logged_in = False

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper

@require_login
def view_profile(name):
    print("Welcome", name)
    print("You can view your profile.")

name = input("Enter your name: ")

is_logged_in = True
view_profile(name)

is_logged_in = False
view_profile(name)

print("Function name:", view_profile.__name__)


'''output:
Enter your name: Sathish
Welcome Sathish
You can view your profile.
Access denied. Please log in.
Function name: view_profile'''
