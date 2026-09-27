def build_profile(**details):
    print("----- Profile Card -----")
    
    for key, value in details.items():
        print(key.capitalize(), ":", value)
    
    print("------------------------")



build_profile(name="Sathish", age=19, city="Hyderabad")

build_profile(name="Ravi", hobby="Cricket", branch="CSE")

build_profile(name="sai", age=20, city="Vizag", hobby="Reading", college="GMRIT")


'''output:
----- Profile Card -----
Name : Sathish
Age : 19
City : Hyderabad
------------------------

----- Profile Card -----
Name : Ravi
Hobby : Cricket
Branch : CSE
------------------------

----- Profile Card -----
Name : sai
Age : 20
City : Vizag
Hobby : Reading
College : GMRIT
------------------------'''
