# * MARK: - Solution 1: Doing it “by hand”
# Given a list of size n, remove all even integers from it. Implement this solution in
# Python and see if it runs without an error.

def remove_even(lst):
    odds = []  # Create a new empty list
    for number in lst:  # Iterate over input list
        # Check if the item in the list is NOT even
        # ('%' is the modulus symbol!)
        if number % 2 != 0:
            odds.append(number)  # If it isn't even append it to the empty list
    return odds  # Return the new list


print(remove_even([3, 2, 41, 3, 34]))

# This solution starts with the first element of the list and checks if it is not even.
# If it is odd, the element is appended to a new list. Otherwise, it skips to the next element.
# This repeats until the end of the list is reached.

# You might have written a solution like this one. It isn’t wrong, it’s not very Pythonic.
# Python is known for its economical code so we’ll be introducing ways to make your solutions
# as Pythonic as possible throughout this course!

# ? Time Complexity
# Since the entire list has to be iterated over, this solution is in O(n) time.


def remove_even_py(lst):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in lst if number % 2 != 0]


print(remove_even_py([3, 2, 41, 3, 34]))

# * MARK: - Solution #2: Using list comprehension

# A Python technique called list comprehension is used to iterate over the
# initial array. With list comprehension, checking a condition and appending to
# the new list can all be done in one line. The code for it starts and ends with
# a ‘[’ and ends with a ‘]’. The basic syntax is:

# newList = [expression(i) for i in oldList if filter(i)]

# The list is iterated. If the number is odd, it is appended to a list to be returned,
# and if even, the element is filtered out from the list. Repeat until the end of the list is reached.

# ? Time Complexity
# The time complexity of this solution is also O(n), since only the syntax has changed
# while the algorithm still iterates over all elements of the list.
