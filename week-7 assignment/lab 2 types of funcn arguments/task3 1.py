def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks = input("Enter marks separated by spaces: ").split()
marks = [float(mark) for mark in marks]

total, average = total_marks(*marks)

print("Total marks:", total)
print("Average marks:", average)


'''output:
Enter marks separated by spaces: 80 75 90 85 70
Total marks: 400.0
Average marks: 80.0'''
