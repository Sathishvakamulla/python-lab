
num = int(input("Enter a number: "))

temp = num
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10       
    sum_digits += digit     
    count += 1              
    temp //= 10             

if count != 0:
    average = sum_digits / count
else:
    average = 0

print("Sum of digits:", sum_digits)
print("Average of digits:", average)


'''output-
Enter a number: 6576
Sum of digits: 24
Average of digits: 6.0
'''
