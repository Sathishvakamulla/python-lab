numbers = [10, 20, 5, 40, 30]

maximum = numbers[0]
minimum = numbers[0]
total = 0

for i in numbers:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

    total = total + i

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)


''' output:
Maximum: 40
Minimum: 5
Sum: 105

'''
