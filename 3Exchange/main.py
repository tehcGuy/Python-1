# Create a function that takes two strings as input and returns
# two new strings where the first two characters are exchanged between the strings


def exchange(word_1, word_2):
    two_char_1 = word_1[0:2]
    two_char_2 = word_2[0:2]

    new_word_1 = two_char_2 + word_1[2:len(word_2)]
    new_word_2 = two_char_1 + word_2[2:len(word_1)]

    return new_word_1 + ' ' + new_word_2


user_word_1 = "Mother"
user_word_2 = "Father"

print(exchange(user_word_1, user_word_2))
