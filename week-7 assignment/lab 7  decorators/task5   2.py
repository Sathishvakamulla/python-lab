is_logged_in = False

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

print("\nWhen is_logged_in = True:")
is_logged_in = True
view_profile(name)

print("\nWhen is_logged_in = False:")
is_logged_in = False
view_profile(name)

'''output:
Enter your name: Sathish

When is_logged_in = True:
Welcome Sathish
You can view your profile.

When is_logged_in = False:
Access denied. Please log in.'''
