def stats(numbers):
    """Return the minimum, maximum and average of a list."""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

minimum, maximum, average = stats(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)


'''output:
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 7
Minimum = 2
Maximum = 7
Average = 4.2

'''
