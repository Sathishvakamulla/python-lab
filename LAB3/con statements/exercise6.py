ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special symbol")


'''output:
Enter a character: 5
Digit'''

