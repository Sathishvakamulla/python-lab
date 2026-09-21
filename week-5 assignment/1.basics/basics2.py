'''
->Without slicing

str = input("Enter string: ")
rev = ""

for i in range(len(str)-1, -1, -1):
    rev = rev + str[i]

print(rev)

#output:
Enter string: sathish
hsihtas
'''


'''
->with slicing
str = input("Enter string: ")
print(str[::-1])


#output:
Enter string: sathish
hsihtas

'''
