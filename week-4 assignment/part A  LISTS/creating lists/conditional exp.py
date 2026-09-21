numbers = [10, -5, 20, -3, 0, 15, -8]

new_list = [0 if i < 0 else i for i in numbers]

print(new_list)


'''output:
[10, 0, 20, 0, 0, 15, 0]'''
