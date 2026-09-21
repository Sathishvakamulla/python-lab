sentence = input("Enter a sentence: ")

words = sentence.split()

words.reverse()

print("Reversed sentence:", " ".join(words))


''' output:
Enter a sentence: i love python
Reversed sentence: python love i'''
