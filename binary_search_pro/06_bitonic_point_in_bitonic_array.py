# Bitonic Point in Bitonic Array
# Let's use our approach in a problem with an unsorted array as the input.

# Difficulty Level: Easy

# * MARK: - Problem statement
# We’ll call an array, nums, a bitonic array if the following properties hold:

# - nums.length >= 3
# - There exists some i with 0 < i < nums.length - 1 such that:
#   - nums[0] < nums[1] < ... < nums[i-1] < nums[i]
#   - nums[i] > nums[i+1] > ... > nums[nums.length - 1]

# Suppose we are given an integer array nums that is guaranteed to be a bitonic one, and return any i such
# that nums[0] < nums[1] < ... < nums[i - 1] < nums[i] > nums[i + 1] > ... > nums[nums.length - 1].

# ? Constraints:
# 3 <= nums.length <= 10 ^ 4
# 0 <= nums[i] <= 10 ^ 6
# nums is guaranteed to be a bitonic array.

# ? Example 1:
# Input: [0, 1, 0]
# Output: 1

# ? Example 2:
# Input: [0, 2, 1, 0]
# Output: 1

# ? Example 3:
# Input: [0, 10, 5, 2]
# Output: 1

# ? Example 4:
# Input: [3, 4, 5, 1]
# Output: 2

# ? Example 5:
# Input: [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
# Output: 2

# * MARK: - Intuition
# The array increases until a certain point. The point at which it stops increasing is the bitonic point.

# ? Algorithm
# - Set the left boundary to 0, and the right boundary to nums.length
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with nums[mid - 1] and nums[mid + 1]
#      - If nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid], we will know that the job is done and we will return the index.
#      - Else, if nums[mid - 1] < nums[mid], we will move the left boundary left = mid
#      - Otherwise, we will move the right boundary right = mid
# - Return left

# images/043.png
# images/044.png
# images/045.png
# images/046.png
# images/047.png

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


def main():
    print("The peak index is ---> " +
          str(findBitonicPoint([-8, 1, 2, 3, 4, 5, -2, -3, -9])))
    print("The peak index is ---> " +
          str(findBitonicPoint([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
    print("The peak index is ---> " +
          str(findBitonicPoint([0, 9, 8, 7, 6, 5, 4, 3, 2, 1])))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log n)
# Space complexity: O(1)
