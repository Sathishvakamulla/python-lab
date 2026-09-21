sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)


''' output:
Enter a sentence: i love python programming
Longest word: programming'''
