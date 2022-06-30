# Minimum in Rotated Sorted Array
# Let's try our approach when the input is a rotated and sorted array.

# Difficulty Level: Medium

# * MARK: - Problem statement
# Suppose an array that was sorted in ascending order is rotated. For example, the array nums = [0, 1, 2, 4, 5, 6, 7]
# might become:

# [4, 5, 6, 7, 0, 1, 2], if it is rotated 4 times.
# [0, 1, 2, 4, 5, 6, 7], if it is rotated 7 times.

# Notice the rotation of an array[nums[0], nums[1], nums[2], ..., nums[n-1]] 1 time results in the array[nums[n-1],
# nums[0], nums[1], nums[2], ..., nums[n-2]].

# Given sorted and rotated array nums, return the minimum element in the array.
# ? Constraints:

# - 1 <= nums.length <= 5000
# - -5000 <= nums[i] <= 5000
# - All of the integers of nums are unique.
# - nums is sorted and rotated.

# ? Example 1:
# Input: [3, 4, 5, 1, 2]
# Output: 1
# Explanation: The original array was[1, 2, 3, 4, 5], and it was rotated 3 times.

# ? Example 2:
# Input: [4, 5, 6, 7, 0, 1, 2]
# Output: 0
# Explanation: The original array was[0, 1, 2, 4, 5, 6, 7], and it was rotated 4 times.

# ? Example 3:
# Input: [11, 13, 15, 17]
# Output: 11
# Explanation: The original array was[11, 13, 15, 17], and it was rotated 4 times.

# * MARK: - Intuition
# - With the binary search approach, we can find a pivot point of the array.
# - We will run the binary search algorithm for two ascending parts, separately.

# * MARK: - Algorithm
# - Set the left boundary to 0, and the right boundary to nums.length
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with nums[mid - 1]
#      - If nums[mid - 1] > nums[mid], the job will be done, and it will return the index.
#      - Else, if nums[left] < nums[mid], then we will move the left boundary left = mid
#      - Otherwise, when we will move the right boundary right = mid
# - Return left

import binary_search_pro


def searchInBitonicArray(nums, target):
    bitonicPoint = binary_search_pro.findBitonicPoint(nums)
    indexInLeftPart = binary_search_pro.ascendingBinarySearch(
        nums, 0, bitonicPoint, target)

    if -1 != indexInLeftPart:
        return indexInLeftPart

    indexInRightPart = binary_search_pro.descendingBinarySearch(
        nums, bitonicPoint + 1, len(nums), target)

    if -1 != indexInRightPart:
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


def findMin(nums):
    pivot = findPivot(nums)

    return min(nums[0], nums[pivot])


def main():
    print("The minimum element is ---> " +
          str(findMin([-5, 1, 2, 3, 4, 5, -8, -7, -6])))
    print("The minimum element is ---> " +
          str(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log_2 \space n)
# Space complexity: O(1)
