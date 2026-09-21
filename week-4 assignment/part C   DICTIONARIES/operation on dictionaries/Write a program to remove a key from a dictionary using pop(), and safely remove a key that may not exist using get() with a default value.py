students = {
    101: "Ravi",
    102: "Sita",
    103: "Arjun"
}

print("Before:", students)

students.pop(102)
print("After pop:", students)

value = students.get(105, "Key not found")
print(value)


'''output:
Before: {101: 'Ravi', 102: 'Sita', 103: 'Arjun'}
After pop: {101: 'Ravi', 103: 'Arjun'}
Key not found

'''
my_list = [10, 20, 30, 20, 40]
my_string = "hello"

set_from_list = set(my_list)
set_from_string = set(my_string)

print("Set from list:", set_from_list)
print("Set from string:", set_from_string)
