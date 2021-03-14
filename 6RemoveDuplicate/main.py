# For a given list of numbers return a list where all identical,
# neighboring numbers are contracted to a single number (e.g. [1,2,2,3][1,2,3]


def remove_adjacent(nums):
    a = []
    for item in nums:
        if len(a):
            if a[-1] != item:
                a.append(item)
        else:
            a.append(item)
    return a


num = [1, 2, 2, 3, 3, 2, 1, 212, 32, 212]
store = remove_adjacent(num)
print(store)
