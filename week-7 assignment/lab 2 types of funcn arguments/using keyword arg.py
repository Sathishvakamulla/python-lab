def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)


student_info("Sathish", 101, "CSE")

print()


student_info(branch="CSE", name="Sathish", roll_no=101)


'''output:
Name: Sathish
Roll No: 101
Branch: CSE
'''
