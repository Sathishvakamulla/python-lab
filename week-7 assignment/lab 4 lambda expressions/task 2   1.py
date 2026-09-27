grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = int(input("Enter marks: "))

print("Result:", grade(marks))


''' output:
Enter marks: 75
Result: Pass'''
