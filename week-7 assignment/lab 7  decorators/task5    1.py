is_logged_in = True

def require_login(func):
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

view_profile(name)


'''output:
Enter your name: Sathish
Welcome Sathish
You can view your profile.'''
