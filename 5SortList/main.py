# For a given list of strings write a function that returns a sorted list
# with all strings starting with the character x at the beginning (define two lists)


set_words_list = ["argentinax", "football", "ss", "poxland", "axmerica", "xmas", "xxx:)", "XL"]

x_words = []
nox_words = []
for word in set_words_list:
    if word.startswith("x"):
        x_words.append(word)
    else:
        nox_words.append(word)

result = sorted(x_words) + sorted(nox_words)
print(result)
