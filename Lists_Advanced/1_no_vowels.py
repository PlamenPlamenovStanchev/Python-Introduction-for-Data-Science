vowels = ["a", "e", "i", "o", "u"]
word = input()

no_vowel_word = ''.join([letter for letter in word if letter.lower() not in vowels])
print(no_vowel_word)