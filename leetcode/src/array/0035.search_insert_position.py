# 35. Search Insert Position (easy)

# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index 
# where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

import unittest


class Solution(unittest.TestCase):
    def search_insert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            center = (left + right) // 2
            if nums[center] == target:
                return center 
            
            if nums[center] > target:
                right = center - 1
            else: 
                left = center + 1
        return left


    def test(self):
        pass


unittest.main()