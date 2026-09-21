sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:]

print("Title Case:", " ".join(words))


'''output:
Enter a sentence: i love python
Title Case: I Love Python
'''
