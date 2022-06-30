# First Element Equals its Index
# Let's check another problem with a sorted input array.

# Difficulty Level: Easy

# * MARK: - Problem statement
# Suppose we are given a sorted array of distinct integers, nums, which are sorted in ascending order. We
# will return the smallest index i, which satisfies nums[i] == i. If no such i exists, we will return -1.

# ? Constraints:
# 1 <= nums.length <= 10 ^ 3
# -10 ^ 3 <= nums[i] <= 10 ^ 3

# ? Example 1: General case
# Input: [-10, -5, 0, 3, 7]
# Output: 3
# Explanation: For the given array, nums[0] = -10, nums[1] = -5, nums[2] = 0, nums[3] = 3, the output is 3.

# ? Example 2: The answer is at the beginning of the array
# Input: [0, 2, 5, 8, 17]
# Output: 0
# Explanation: nums[0] = 0. Thus the output is 0.

# ? Example 3: The answer is missing
# Input: [-10, -5, 3, 4, 7, 9]
# Output: -1
# Explanation: There is no such i that nums[i] = i. Thus the output is -1.

# * MARK: - Intuition
# This problem is similar to the first challenge that we solved in the previous lesson. But, in the case of
# this problem, there is a greater range of integers and the index we are looking for is absent. An index of
# an element is our target here.

# ? Algorithm
# Set the left boundary to 0, and the right boundary to the size of nums.

# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with target
#      - If nums[mid] == mid and left < nums[left], the job will be done and we will return the index.
#      - Else, if nums[mid] < mid, then we will move the left boundary left = mid
#      - Otherwise, if nums[mid] > mid, then we will move the right boundary right = mid
# - If nums[left] == left, then we will return left
# - If right < size of nums and nums[right] == right, then we will return right
# - Return - 1

# images/031.png
# images/032.png
# images/033.png
# images/034.png
# images/035.png
# images/036.png

def fixedPoint(nums):
    # the initial value for left index is 0
    left = 0
    # the initial value for right index is the number of elements in the array
    right = len(nums)
    # left + 1 >= right will finish while loop
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid] == mid and left < nums[left]:
            # mid is the index to answer
            return mid
        elif nums[mid] < mid:
            # there is no sense to search in the left half of the array
            left = mid
        else:
            # there is no sense to search in the right half of the array
            right = mid
    # left can be the index to answer
    if nums[left] == left:
        return left
    # right can be the index to answer
    if right < len(nums) and nums[right] == right:
        return right
    # there is no item equal to its index in the array
    return -1


def main():
    print("The fixed index is ---> " +
          str(fixedPoint([1, 5, 8, 9, 11, 13, 15, 19, 21])))
    print("The fixed index is ---> " +
          str(fixedPoint([-8, -2, -1, 0, 2, 5, 8, 9])))
    print("The fixed index is ---> " +
          str(fixedPoint([-1, 0, 1, 2, 3, 4, 5, 6, 7, 9])))
    print("The fixed index is ---> " +
          str(fixedPoint([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log_2 \space n)
# Space complexity: O(1)
