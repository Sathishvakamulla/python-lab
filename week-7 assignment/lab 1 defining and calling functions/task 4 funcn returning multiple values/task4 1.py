def stats(numbers):
    """Return the minimum, maximum and average of a list."""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average

numbers = [10, 20, 30, 40, 50]

result = stats(numbers)

print("Minimum =", result[0])
print("Maximum =", result[1])
print("Average =", result[2])

'''output: Minimum = 10
Maximum = 50
Average = 30.0'''
