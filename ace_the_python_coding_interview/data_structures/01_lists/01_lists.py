
# * MARK: - Lists
# Python lists are data structures that group sequences of elements. Lists can have elements
# of several types, and you can also mix different types within the same list (although all
# elements are usually of the same datatype).

# Lists are created using square brackets [], and the elements are separated by commas (,).
# The elements in a list can be accessed by their positions, starting with 0 as the index
# of the first element.

# list=[element1,element2,...]
# For example, to create list l with five elements, write

# l = [1, 2, 3, 4, 5]

# print(l)  # prints the entire list
# print(l[0])  # prints value at index 0
# print(l[1])  # prints value at index 1


# * MARK: - Sublist
# Sometimes you want just a small portion of a list—a sublist. Sublists are simply subsets
# of a list; they can be retrieved using a technique called slicing.

# A sublist is created by writing the list name, then separating the start and end indexes
# with a colon (: ) and enclosing them within square brackets ([]).

# sublist=list[startindex:endindex]
# Given a list l ,to create sublist l1 and l2 write:

# l = [1, 2, 3, 4, 5]

# l1 = l[0:3]
# l2 = l[3:5]

# Note: The start index is inclusive and end index is exclusive in the range.

# l = ['a', 'b', 'c', 'd', 'e']
# print(l[0:3])

# * MARK: - Operations on List
# Some basic operations on the lists are explained below:-

# ? List Concatenation
# Lists can be concatenated using the + operator
# print([1,2] + [3,4])

# ? Traverse a List#
# Finally, lists can be iterated over using for loops in Python.

# l=[1, 2, 4, 8, 10]
# for val in l:
#   print(val)

