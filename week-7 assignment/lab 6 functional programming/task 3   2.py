from functools import reduce

words = []

n = int(input("Enter number of words: "))

for i in range(n):
    word = input("Enter word: ")
    words.append(word)

sentence = reduce(lambda x, y: x + " " + y, words)

print("Sentence:", sentence)



'''output:
Enter number of words: 4
Enter word: Python
Enter word: is
Enter word: very
Enter word: useful
Sentence: Python is very useful'''
