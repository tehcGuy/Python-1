import sys

# Create a function that removes the first and 
# last two characters of any string


def remove(user_word):
    return user_word[1:len(user_word) - 2]


name = sys.argv[1]
print(remove(name))
