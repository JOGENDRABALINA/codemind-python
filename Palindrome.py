def is_palindrome(word):
    word = word.lower()

    word = ''.join(e for e in word if e.isalnum())

    return word == word[::-1]

word = input()
if is_palindrome(word):
    print(True)
else:
    print(False)