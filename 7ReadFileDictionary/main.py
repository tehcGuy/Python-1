# Write a program that opens a file containing two columns and save it as a dictionary
# where the values of the first column are the keys for values in the second column


dictionary_done = {}  # declaring dictionary data type

dictionary_of_names = open("names.txt")

for line in dictionary_of_names:
    key, value = line.split()

    dictionary_done[key] = value

print(dictionary_done)
