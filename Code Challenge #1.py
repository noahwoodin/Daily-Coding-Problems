# Coding Challenge #1 (Easy)

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def checker(num_list, k):
    list_spot = 1
    for num in num_list:
        counter = list_spot
        while counter < len(num_list):
            if num + num_list[counter] == k:
                return True
            counter += 1
        list_spot += 1
    return False


result1 = checker([1, 2, 3, 4], 7)
result2 = checker([6, 5, 4, 4], 10)
result3 = checker([1, 5, 3, 4, 2], 8)
result4 = checker([1, 5, 3, 4, 2], 10)
print(result1)
print(result2)
print(result3)
print(result4)