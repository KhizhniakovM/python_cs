# Element in Rotated Sorted Array
# Let's modify the problem with a rotated sorted array and solve it.

# Difficulty Level: Medium

# * MARK: - Problem statement
# Suppose an array that was sorted in ascending order is rotated. For example, the array
# nums = [0, 1, 2, 4, 5, 6, 7] might become:

# [4, 5, 6, 7, 0, 1, 2], if it is rotated 4 times.
# [0, 1, 2, 4, 5, 6, 7], if it is rotated 7 times.

# Notice that rotating an array[nums[0], nums[1], nums[2], ..., nums[n-1]] 1 time results in
# the array[nums[n-1], nums[0], nums[1], nums[2], ..., nums[n-2]].

# Suppose we are given a sorted rotated array nums, and an integer target. If target is found in
# the array, we will return its index. Otherwise, we will return -1.

# ? Constraints:
# 1  <= nums.length  <= 5000
# -10 ^ 4  <= nums[i]  <= 10 ^ 4
# All of the values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -10 ^ 4  <= target  <= 10 ^ 4

# ? Example 1:
# Input: [4, 5, 6, 7, 0, 1, 2], 0
# Output: 4

# ? Example 2:
# Input: [4, 5, 6, 7, 0, 1, 2], 3
# Output: -1

# ? Example 3:
# Input: [1], 0
# Output: -1

# * MARK: - Intuition
# With the binary search approach, we can find a pivot point of the array.
# We will run the binary search algorithm for the two ascending parts, separately.

# * MARK: - Algorithm
# - Set the left boundary to 0, and the right boundary to nums.length
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with nums[mid - 1]
#     - If nums[mid - 1] > nums[mid], the job will be done and we will return the index.
#     - Else, if nums[left] < nums[mid], we will move the left boundary left = mid
#     - Otherwise, we will move the right boundary right = mid
# - Return left

def search(nums, target):
    pivot = findPivot(nums)
    indexInLeftPart = ascendingBinarySearch(nums, 0, pivot, target)

    if indexInLeftPart != -1:
        return indexInLeftPart

    indexInRightPart = ascendingBinarySearch(nums, pivot, len(nums), target)

    if indexInRightPart != -1:
        return indexInRightPart

    return -1


def findPivot(nums):
    # the initial value for left index is 0
    left = 0
    # the initial value for right index is the number of elements in the array
    right = len(nums)
    # left + 1 >= right will finish while loop
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid - 1] > nums[mid]:
            # mid is the index to answer
            return mid
        elif nums[left] < nums[mid]:
            # there is no sense to search in the left half of the array
            left = mid
        else:
            # there is no sense to search in the right half of the array
            right = mid
    # left is the answer
    return left


def ascendingBinarySearch(nums, left, right, target):
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    if nums[left] == target:
        return left

    if right < len(nums) and nums[right] == target:
        return right

    return -1


def main():
    print("Index of 5 is ---> " +
          str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], 5)))
    print("Index of 6 is ---> " +
          str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], 6)))
    print("Index of -5 is ---> " +
          str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], -5)))
    print("Index of -6 is ---> " +
          str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], -6)))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log n)
# Space complexity: O(1)
