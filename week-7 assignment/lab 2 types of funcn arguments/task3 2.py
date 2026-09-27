def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# 3 marks
total, average = total_marks(80, 75, 90)
print("3 Marks:")
print("Total:", total)
print("Average:", average)

# 5 marks
total, average = total_marks(80, 75, 90, 85, 70)
print("\n5 Marks:")
print("Total:", total)
print("Average:", average)

# 1 mark
total, average = total_marks(85)
print("\n1 Mark:")
print("Total:", total)
print("Average:", average)

'''output:
3 Marks:
Total: 245
Average: 81.66666666666667

5 Marks:
Total: 400
Average: 80.0

1 Mark:
Total: 85
Average: 85.0'''
