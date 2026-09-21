string = input("Enter a string: ")

if string.isdigit():
    print("Only digits")
elif string.isalpha():
    print("Only alphabets")
elif string.isalnum():
    print("Alphanumeric")
else:
    print("Contains special characters")


'''output:
Enter a string: sathish123
Alphanumeric
'''
