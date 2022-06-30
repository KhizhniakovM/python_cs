# Element Occurrence
# Let's try to count elements. This lesson is of medium-level difficulty.

# * MARK: - Problem statement
# Suppose we are given a sorted array of integers, find the number of occurrences of a given target value.
# If the target is not found in the array, return -1.

# ? Constraints:
# 1 <= nums.length <= 10 ^ 4
# -10 ^ 4 <= nums[i] <= 10 ^ 4
# nums contains values sorted in an ascending order.
# -10 ^ 4 <= target <= 10 ^ 4

# ? Example 1:
# Input: [5, 7, 7, 8, 8, 10], 8
# Output: 2

# * MARK: - Intuition
# Based on the description of the problem, we can see that it could be a good match with the binary search algorithm.

# * MARK: - Algorithm
# - Set the left boundary to 0, and the right boundary to nums.length
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with target
#      - If nums[mid] == target, the job will be done and we will return the index.
#      - Else, if nums[mid] < target, we will move the left boundary left = mid
#      - Otherwise nums[mid] > target, we will move the right boundary right = mid
# - If nums[left] < target, we will return right
# - Return left

def findCount(nums, target):
    left = binarySearch(nums, target, True)

    if left < 0:
        return -1

    right = binarySearch(nums, target, False)

    return right - left + 1


def binarySearch(nums, target, leftmost):
    # the initial value for left index is 0
    left = 0
    # the initial value for right index is the number of elements in the array
    right = len(nums)
    # left + 1 >= right will finish while loop
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid] == target:
            if leftmost:
                right = mid
            else:
                left = mid
        elif nums[mid] < target:
            # there is no sense to search in the left half of the array
            left = mid
        else:
            # there is no sense to search in the right half of the array
            right = mid
    # left can be the index to answer
    if nums[left] == target:
        return left
    # right can be the index to answer
    if right < len(nums) and nums[right] == target:
        return right
    # there is no target in the array
    return -1


def main():
    print("The number of occurrences of 5 is ---> " +
          str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 5)))
    print("The number of occurrences of 20 is ---> " +
          str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 20)))
    print("The number of occurrences of 1 is ---> " +
          str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 1)))
    print("The number of occurrences of 19 is ---> " +
          str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 19)))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log n)
# Space complexity: O(1)

# * MARK: - Challenge 1
# The variation of the previous problem is asked about frequently during phone interviews.

# ? Problem statement
# Suppose we are given an array of integers, nums, sorted in a non-decreasing order, and a number, target. We
# will return True only if target is a majority element. If the target is not found in the array, return False.

# A majority element is an element that appears more than N / 2 times in an array of length N.

# ? Constraints:
# 1 <= nums.length <= 10 ^ 3
# -10 ^ 3 <= nums[i] <= 10 ^ 3
# 1 <= target <= 10 ^ 3

# ? Example 1:
# Input: [2, 4, 5, 5, 5, 5, 5, 6, 6], 5
# Output: true
# Explanation: The value 5 appears 5 times and the length of the array is 9. Thus, 5 is a majority element
# because 5 > 9/2 is true.

# ? Example 2:
# Input: [10, 100, 101, 101], 101
# Output: false
# Explanation: nums[0] = 0. Thus, the output is 0.

# ? Example 3:
# Input: [-10], 10
# Output: false
# Explanation: The target is not found in the array. Thus, the output is false.

# Now, we will try to write this algorithm
# ? We can use BS two times to find the first and last index of the target.
