string = input("Enter a string: ")

for ch in set(string):
    count = string.count(ch)
    
    if count > 1:
        print(ch, ":", count)


'''output:
Enter a string: sathish
h : 2
s : 2'''
