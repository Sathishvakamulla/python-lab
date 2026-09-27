import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

@timer
def sum_large_range(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

n = int(input("Enter the range limit: "))

result = sum_large_range(n)

print("Sum:", result)


'''output:
Enter the range limit: 10000000
Execution time: 0.52 seconds
Sum: 50000005000000'''
