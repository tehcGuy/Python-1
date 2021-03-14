# Write a program that counts the number words in the file
# and returns how many times each word is repeated

reader = open('names.txt', 'r')
data = reader.read()
words = data.split()  # Split a string into a list where each word is a list item; default separator is any whitespace

print('Amount of words =', len(words))
