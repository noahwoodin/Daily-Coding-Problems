# Coding Challenge #2 (Hard)

# Given an array of integers...
# return a new array such that each element at index i of the new array is the product of all the numbers
# in the original array except the one at i.

# Follow-up: what if you can't use division?

def product_array(num_list):
    if not num_list or 0 in num_list:
        return 0
    product = 1
    for num in num_list:
        product = product * num
    for index, num in enumerate(num_list):
        num_list[index] = product/num
    return num_list


list1 = product_array([1, 2, 3, 4, 5])
print(list1)

list2 = product_array([2, 2, 3, 4, 9])
print(list2)

list3 = product_array([0])
print(list3)

list3 = product_array([])
print(list3)
