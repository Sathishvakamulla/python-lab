def is_palindrome(word):
    return word == word[::-1]

words = []

n = int(input("Enter number of words: "))

for i in range(n):
    word = input("Enter word: ")
    words.append(word)

palindromes = list(filter(is_palindrome, words))

print("Palindromes:", palindromes)


'''output:
Enter number of words: 5
Enter word: madam
Enter word: hello
Enter word: level
Enter word: python
Enter word: radar
Palindromes: ['madam', 'level', 'radar']'''
