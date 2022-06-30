# Square Root of Integer
# Let's try to solve one problem with different inputs.

# Difficulty Level: Easy

# * MARK: - Problem statement
# Suppose we are given an integer a. Compute and return the square root of a. If a is not a perfect square,
# we will truncate the decimal digits.

# ? Constraints:
# 0 <= a <= 10 ^ 3

# ? Example 1:
# Input: 11
# Output: 3
# Explanation: The square root of 11 is 3.3166... and since the decimal part is truncated, 3 is returned.

# ? Example 2:
# Input: 9
# Output: 3
# Explanation: 9 gives a perfect square root.

# * MARK: - Intuition
# Binary search works well for searching elements in a sorted array. It works this way because the array
# itself is monotonic(either increasing or decreasing). Hence, if we are in a particular position, we can
# make a definite call as to whether the answer lies in the left part or the right part of the position.

# A similar thing can be done with monotonic functions(monotonically increasing or decreasing) as well.
# Let’s say there is a function f(x), which increases when x increases.

# Hence, given a problem of finding x so that f(x) = v, we can do a binary search for x

# At any instance,

# - if f(currentPosition) > v, we will search for values lower than the currentPosition
# - if f(currentPosition) < v, we will search for values higher than the currentPosition
# - if f(currentPosition) = v, then this will be the answer.

# * MARK: - Algorithm
# - If a < 2, we will return a.
# - Set the left boundary to 0, and the right boundary to a
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compute mid * mid and compare it with a:
#      - If mid * mid == a, the integer square root is here, we will return it.
#      - Else, if mid * mid < a, we will move the left boundary left = mid
#      - Otherwise, mid * mid > a, we will move the right boundary right = mid
# - Return left

# images/037.png
# images/038.png
# images/039.png
# images/040.png
# images/041.png
# images/042.png

def sqrt(a):
    if a < 2:
        return a
    # the initial value for left is 0
    left = 0
    # the initial value for right is the number
    right = a
    # left + 1 >= right will finish while loop
    while left + 1 < right:
        mid = (right + left) // 2

        if mid * mid == a:
            # mid is the answer
            return mid
        elif mid * mid < a:
            # there is no sense to search among numbers less than mid
            left = mid
        else:
            # there is no sense to search among numbers bigger than mid
            right = mid
    # the answer is left
    return left


def main():
    print("The square root of 11 is ---> " + str(sqrt(11)))
    print("The square root of 9 is ---> " + str(sqrt(9)))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log_2 \space a)
# Space complexity: O(1)

# * MARK: - Challenge 1
# We can play with the square root of a further.

# ? Problem statement
# Suppose we are given a positive integer a. Write a function that returns True if a is a perfect square and
# returns False if a is not a perfect square.

# Constraints:
# 1 <= a <= 10 ^ 3

# ? Example 1:
# Input: 16
# Output: true

# ? Example 2:
# Input: 14
# Output: false

# Now, we will try to write this algorithm.
# ? We have to return True if mid*mid == a. Otherwise, return False.

# * MARK: - Challenge 2
# Let’s use the binary search with a monotonic function here.

# ? Problem statement
# Suppose that there are a total of n coins that we want to form into a staircase shape, where every k-th row
# contains exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# Constraints:
# 1 <= n <= 10 ^ 3

# ? Example 1:
# Input: 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we will return 2.

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤

# ? Example 2:
# Input: 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we will return 3.

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# You have to return mid if mid * (mid + 1) / 2 == n. Otherwise, continue the binary search.
