grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = []

for i in range(6):
    m = int(input("Enter marks: "))
    marks.append(m)

for m in marks:
    print(m, ":", grade(m))


'''output:
Enter marks: 75
Enter marks: 32
Enter marks: 48
Enter marks: 20
Enter marks: 90
Enter marks: 39
75 : Pass
32 : Fail
48 : Pass
20 : Fail
90 : Pass
39 : Fail'''
