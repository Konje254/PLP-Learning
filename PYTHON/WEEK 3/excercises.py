word_int = input('Enter any word')

is_palindrom = lambda word_int : print('It is a palindrome') if word_int[::-1] == word_int else print('It is not a palindrome')

is_palindrom(word_int)