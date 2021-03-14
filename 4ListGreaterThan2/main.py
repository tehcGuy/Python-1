# For a given list of strings write a function that
# returns the number of strings in that
# list where the length is greater than 2 and the
# last character is identical to the first

def number_of_strings(user_words):
    count = 0
    for i in user_words:
        if len(i) > 2 :
            if i[0:1] == i[len(i)-1:]:
                print(i)
                count += 1
    return count


set_words_list = ["argentina", "football", "ss", "poland","america"]
x = number_of_strings(set_words_list)
print(x)
