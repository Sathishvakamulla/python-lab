students = {
    101: "Ravi",
    102: "Sita",
    103: "Arjun"
}

key = int(input("Enter roll number: "))

if key in students:
    print("Name:", students[key])
else:
    print("Key does not exist")


'''output:
Enter roll number: 103
Name: Arjun'''
