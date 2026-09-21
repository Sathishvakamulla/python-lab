string = input("Enter a string: ")
sub = input("Enter substring: ")

index = -1
count = 0

for i in range(len(string) - len(sub) + 1):
    if string[i:i + len(sub)] == sub:
        if index == -1:
            index = i
        count += 1

print("First index:", index)
print("Count:", count)


'''output:
Enter a string: banana
Enter substring: an
First index: 1
Count: 2'''

'''
