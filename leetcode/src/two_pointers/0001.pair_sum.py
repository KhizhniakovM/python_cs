# 0001. Two Sum (easy)

# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

import unittest


class Solution(unittest.TestCase):
    def twoSum(self, nums, target):
        nums.sort()
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer < right_pointer:
            if nums[left_pointer] + nums[right_pointer] == target:
                return [left_pointer, right_pointer]
            elif nums[left_pointer] + nums[right_pointer] > target:
                right_pointer -= 1
            else:
                left_pointer += 1

        return []

    def test(self):
        pass


unittest.main()
