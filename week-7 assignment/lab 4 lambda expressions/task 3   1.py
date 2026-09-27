students = []

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))

students = sorted(students, key=lambda x: x[1], reverse=True)

print("Students sorted by marks:")
for student in students:
    print(student)


'''output:
Enter student name: Ravi
Enter marks: 75
Enter student name: Anu
Enter marks: 92
Enter student name: Kiran
Enter marks: 68
Enter student name: Priya
Enter marks: 85
Enter student name: Rahul
Enter marks: 78

Students sorted by marks:
('Anu', 92)
('Priya', 85)
('Rahul', 78)
('Ravi', 75)
('Kiran', 68)'''
