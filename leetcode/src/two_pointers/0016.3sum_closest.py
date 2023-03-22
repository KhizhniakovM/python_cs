# 16. 3Sum Closest (medium)

# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.

# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

import math
import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n^2)
    # space_complexity: O(n)
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_diff = float('inf')

        for num_index in range(len(nums)):
            left, right = num_index + 1, len(nums) - 1

            while left < right:
                diff = target - (nums[num_index] + nums[left] + nums[right])

                if diff == 0:
                    return nums[num_index] + nums[left] + nums[right]

                if (abs(diff) < abs(min_diff)) or (abs(diff) == abs(min_diff) and diff > min_diff):
                    min_diff = diff

                if diff > 0:
                    left += 1
                else:
                    right -= 1

        return target - min_diff

    def test(self):
        nums, target = [4, 0, 5, -5, 3, 3, 0, -4, -5], -2
        expected = -2
        result = self.threeSumClosest(nums, target)
        self.assertEqual(expected, result)


unittest.main()
