employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employees.append({
        "name": name,
        "department": department,
        "salary": salary
    })

dept = input("Enter department to select: ")

selected = list(filter(lambda emp: emp["department"] == dept, employees))

print("Employees from", dept, "department:")

for emp in selected:

    print(emp)
'''output:
Enter number of employees: 3
Enter employee name: Ravi
Enter department: IT
Enter salary: 30000
Enter employee name: Sita
Enter department: HR
Enter salary: 35000
Enter employee name: Amit
Enter department: IT
Enter salary: 40000
Enter department to select: IT

Employees from IT department:
{'name': 'Ravi', 'department': 'IT', 'salary': 30000.0}
{'name': 'Amit', 'department': 'IT', 'salary': 40000.0}'''
