# What Is Binary Search?
# Learn what binary search is and how we can implement it.

# Binary Search (BS) is one of the most basic searching algorithms. It is common for interviewers to ask coding
# questions where the only or optimal solution requires us to use binary search. . This is especially important
# at on-site interviews, where interviewees are asked only two to four different problems. Unfortunately,
# failure to effectively use binary search bug-free can be a red flag.

# Binary search is also referred to as half-interval search, which gives us a hint at when to use it. If we can,
# roughly, eliminate half of the search area with a single condition, then we are binary searching our target.

# ? Handling Corner Cases!

# The most common reason why candidates fail at binary search coding interview questions is that they fail to
# handle corner cases.

# There are many reasons why binary search corner cases might form. For instance, a corner case is formed
# when the target is at the 0th index of an array when the target is at (n - 1)th index, when the loop goes
# infinite, and so on.

# Luckily, these pitfalls can be avoided if we choose the same approach every time.

# Now, we will take a walk through this approach.

# * MARK: - One universal approach
# ? 1. Pattern
# This is a unique form of binary search. It uses the current index and its immediate left and right neighbors’
# indices in the array.

# Let’s list the essential points of the algorithm and understand each one of them.

# ? Pseudocode
# left = 0
# right = size of array

# while (left + 1 < right)
#   mid = (left + right) / 2

#   if (array[mid] == target)
#     return mid
#   else if (array[mid] < target)
#     continue search in right side
#   else
#     continue search in left side

# if (array[left] == target)
#   return left

# return -1

# Let’s list the essential points of the algorithm and understand each one of them.

# - Line 1: We take 0 as our left index.
# - Line 2: We will take the size of the array as our right index. Hence, we will need to be careful with the right one when we check the item on this index.
# - Line 4: The while loop finishes when there is no element between the left and right ones. Thus, if there is one element in the array, we will skip the loop.
# - Line 14: We must check the element on the left index outside the loop because if we skip the loop, it can become the target.

# ? 2. Implementation
# Here is the code for our approach:

def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    # the initial value for left index is 0
    left = 0
    # the initial value for right index is the number of elements in the array
    right = len(nums)
    # left + 1 >= right will finish while loop
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid] == target:
            # mid is the index of the target
            return mid
        elif nums[mid] < target:
            # there is no sense to search in the left half of the array
            left = mid
        else:
            # there is no sense to search in the right half of the array
            right = mid
    # left can be the index of the target
    if nums[left] == target:
        return left
    # the target doesn't exist in the array
    return -1


def main():
    nums = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

    print("Index of 37 is ---> " + str(binarySearch(nums, 37)))
    print("Index of 1 is ---> " + str(binarySearch(nums, 1)))
    print("Index of 59 is ---> " + str(binarySearch(nums, 59)))
    print("Index of 25 is ---> " + str(binarySearch(nums, 25)))


main()

# Here is a visual representation of our algorithm, in a general case where 37 is a target:

# images/001.png
# images/002.png
# images/003.png
# images/004.png
# images/005.png

# Let’s check the steps that our algorithm takes to handle corner cases:
# - The target is the first element in our array.

# images/006.png
# images/007.png
# images/008.png
# images/009.png
# images/010.png

# - The target is the last element in our array.

# images/011.png
# images/012.png
# images/013.png
# images/014.png
# images/015.png
# images/016.png

# - The target doesn’t exist in our array.

# images/017.png
# images/018.png
# images/019.png
# images/020.png
# images/021.png

# ? 3. Details
# Most of the people who deal with binary search problems get stuck by considering the specifics of each problem.
# But, most binary search questions rely on the same concepts. If we use the same solid foundation for our solution,
# we can easily bypass all of the specifics.

# Our foundation is built on five simple points:

# - The left index points to 0 index.
# - The right index points to the size of array.
# - The while loop condition is left + 1 > right.
# - We will move the left or right index to the mid index.
# - We will check an element on the left index, outside of the loop.

# Let’s take a look at the complexity of our approach in the next lesson.
