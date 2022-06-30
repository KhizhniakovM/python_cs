# Element in Bitonic Array
# Let's try to conduct a binary search of a bitonic array.

# Difficulty Level: Medium

# * MARK: - Problem statement
# Suppose we are given an integer array, nums, which is guaranteed to be a bitonic array and a target value.
# It will return the index if the target is found. If not, it will return -1.

# Constraints:
# 3 <= nums.length <= 10 ^ 5
# 1 <= nums[i], target <= 10 ^ 8
# A given array always contains a bitonic point.
# Array nums always contain distinct elements.

# ? Example 1:
# Input: [3, 9, 10, 20, 17, 5, 1], 20
# Output: 3

# ? Example 2:
# Input: [5, 6, 7, 8, 9, 10, 3, 2, 1], 30
# Output: -1

# * MARK: - Intuition
# Use the findBitonicPoint function from the previous lesson to find the index of a bitonic point. Then, we will
# know that all of the elements on the left hand of the bitonic point are arranged in ascending order and all those
# on the right hand are sorted in descending order.

# Run the binary search algorithm for the ascending and descending parts, separately.

# * MARK: - Algorithm for the BS in the ascending array
# - Set the left boundary to 0, and the right boundary to nums.length
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with nums[mid - 1] and nums[mid + 1]
#      - If nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid], the job will be done and we will return the index.
#      - Else, if nums[mid - 1] < nums[mid], we will move the left boundary left = mid
#      - Otherwise, we will move the right boundary right = mid
# - If nums[left] == target, we will return left.
# - If nums[right] == target, we will return right.
# - Return - 1

def findBitonicPoint(nums):
    # the initial value for left index is 0
    left = 0
    # the initial value for right index is the number of elements in the array
    right = len(nums)
    # left + 1 >= right will finish while loop
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            # mid is the index to answer
            return mid
        elif nums[mid - 1] < nums[mid]:
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

    if nums[right] == target:
        return right

    return -1


def descendingBinarySearch(nums, left, right, target):
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            left = mid
        else:
            right = mid

    if nums[left] == target:
        return left

    if nums[right] == target:
        return right

    return -1


def searchInBitonicArray(nums, target):
    bitonicPoint = findBitonicPoint(nums)
    indexInLeftPart = ascendingBinarySearch(nums, 0, bitonicPoint, target)

    if -1 != indexInLeftPart:
        return indexInLeftPart

    indexInRightPart = descendingBinarySearch(
        nums, bitonicPoint + 1, len(nums), target)

    if -1 != indexInRightPart:
        return indexInRightPart

    return -1


def main():
    print("Index of 5 is ---> " +
          str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], 5)))
    print("Index of 1 is ---> " +
          str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], 1)))
    print("Index of -9 is ---> " +
          str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], -9)))
    print("Index of -1 is ---> " +
          str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], -1)))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log n)
# Space complexity: O(1)
