from functools import reduce

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

updated = list(map(
    lambda emp: {
        "name": emp["name"],
        "department": emp["department"],
        "salary": emp["salary"] * 1.10
    },
    selected
))

total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    updated,
    0
)

print("Employees after 10% salary hike:")

for emp in updated:
    print(emp)

print("Total salary expenditure:", total_salary)


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

Employees after 10% salary hike:
{'name': 'Ravi', 'department': 'IT', 'salary': 33000.0}
{'name': 'Amit', 'department': 'IT', 'salary': 44000.0}
Total salary expenditure: 77000.0'''
