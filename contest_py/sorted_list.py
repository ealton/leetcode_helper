from sortedcontainers import SortedList


"""
    Add: O(log(n))
    Clear: O(n)
    discard: O(log(n))
"""



# initializing a sorted list with parameters
# it takes an iterable as a parameter.
sorted_list = SortedList([1, 2, 3, 4])

# initializing a sorted list using default constructor
sorted_list = SortedList()

# inserting values one by one using add()
for i in range(5, 0, -1):
    sorted_list.add(i)

# prints the elements in sorted order
print('list after adding 5 elements: ', sorted_list)
#
# list after adding 5 elements:  SortedList([1, 2, 3, 4, 5], load=1000)
#

print('list elements are: ', end='')
#
# list elements are: 1 2 3 4 5
#

# iterating through a sorted list
for i in sorted_list:
    print(i, end=' ')
print()

# removing all elements using clear()
sorted_list.clear()

# adding elements using the update() function
elements = [10, 9, 8, 7, 6]

sorted_list.update(elements)

# prints the updated list in sorted order
print('list after updating: ', sorted_list)
#
# list after updating:  SortedList([6, 7, 8, 9, 10], load=1000)
#

# removing a particular element
sorted_list.discard(8)

print('list after removing one element: ', sorted_list)
#
# list after removing one element:  SortedList([6, 7, 9, 10], load=1000)
#

# removing all elements
sorted_list.clear()

print('list after removing all elements using clear: ', sorted_list)
#
# list after removing all elements using clear:  SortedList([], load=1000)
#