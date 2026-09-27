def build_profile(**details):
    print("----- Profile Card -----")
    
    for key, value in details.items():
        print(key.capitalize(), ":", value)

    print("------------------------")

build_profile(
    name="Sathish",
    age=19,
    city="Hyderabad",
    hobby="Coding"
)

'''output:
----- Profile Card -----
Name : Sathish
Age : 19
City : Hyderabad
Hobby : Coding
------------------------'''
