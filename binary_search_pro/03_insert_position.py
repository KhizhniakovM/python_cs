# Insert Position
# Let's solve one basic problem and test our approach.

# Difficulty Level: Easy

# * MARK: - Problem statement
# We are given a sorted array of distinct integers and a target value. We will return the index if the
# target is found. Otherwise, we will return the index to where it would be if it were inserted in order.

# Constraints:
# - 1 <= nums.length <= 10^3
# - -10^3 <= nums[i] <= 10^3
# - contains distinct values, sorted in ascending order.
# - -10^3 <= target <= 10^3

# ? Example 1: General case
# Input: [2,4,5,9,11], 5
# Output: 2

# ? Example 2: Missing element case
# Input: [2,4,5,9,11], 3
# Output: 1

# ? Example 3: Insert to the end of the array
# Input: [2,4,5,9,11], 15
# Output: 5

# ? Example 4: Insert to the beginning of the array
# Input: [2,4,5,9,11], -1
# Output: 0

# * MARK: - Intuition
# Based on the problem statement, we can use our pattern. However, instead of -1, we are asked to return an index
# that will be used to insert the target without a break in the order…

# All we need to change is the if condition, after the while loop and the return statement.

# Let’s think. What do we have outside of the (left + 1 == right) while loop?

# There will be two numbers:

# - left (0 <= left <= nums.length - 1)
# - right (1 <= right <= nums.length)

# images/023.png

# There will be four cases to consider:

# - nums[left] == target
# - nums[left] > target
# - nums[right] == target
# - nums[right] < target

# images/024.png

# The answer is left in the first two cases, while the answer is right in the last two. To complete our
# changes, we will add one if condition for the left to change the return statement to return right.

# * MARK: - Algorithm
# - Set the left boundary to 0, and the right boundary to the size of nums
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with target:
#       - If nums[mid] == target, the job will be done, and we will return the index.
#       - Else, if nums[mid] < target we will move to the left boundary left = mid
#       - Otherwise, nums[mid] > target we will move to the right boundary right = mid

#   - If nums[left] >= target, we wil return left
#   - Return right

# images/025.png
# images/026.png
# images/027.png
# images/028.png
# images/029.png
# images/030.png

def searchInsert(nums, target):
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
    # left can be the index to insert the target
    if nums[left] >= target:
        return left
    # right is the index to insert the target
    return right


def main():
    print("Index of 9 is ---> " +
          str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], 9)))
    print("Index of 12 is ---> " +
          str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], 12)))
    print("Index of -4 is ---> " +
          str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], -4)))
    print("Index of 27 is ---> " +
          str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], 27)))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log_2 \space n)
# Space complexity: O(1)

# * MARK: - Challenge 1
# Unlike the previous task, this one requires the if conditions inside the while loop to be changed.

# ? Problem statement
# We are given a sorted array of integers, nums, that contain n integers, where each integer is in the range[0, n−1]
# inclusive. There is only one duplicate number in nums. Find and return this duplicate number.

# ? Constraints:
# 2 <= nums.length <= 10 ^ 3
# 1 <= nums[i] < nums.length

# All of the integers in nums appear only once, except for one integer that appears twice.

# ? Example 1:
# Input: [1, 2, 3, 4, 4, 5, 6, 7]
# Output: 4

# ? Example 2:
# Input: [1, 1, 2, 3, 4, 5]
# Output: 1

# ? Example 3:
# Input: [1, 2, 3, 4, 5, 5]
# Output: 5

# ? Example 4:
# Input: [1, 1]
# Output: 1

# Let’s try to write this algorithm.
# ? Think about the element and its index. What can we say about the case where the index is smaller?
# ? The answer is the first element which is equal to its index.
