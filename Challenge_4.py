# Coding Challenge #4 (Hard)

# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

def smallest_pos(array):
    if not array:
        return 1
    array = [num for num in array if num > 0]
    array.sort()
    for counter, num in enumerate(array):
        if counter+1 != num:
            return counter+1
    return counter+2


assert smallest_pos([3, 4, -1, 1]) == 2
assert smallest_pos([1, 2, 0]) == 3
