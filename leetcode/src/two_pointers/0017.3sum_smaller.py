# 0017 Triplets with Smaller Sum (medium)

# * MARK: - Problem statement
# Given an array arr of unsorted numbers and a target sum,
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
# Write a function to return the count of such triplets.

# * MARK: - Example 1
# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

# * MARK: - Example 2
# Input: [-1, 4, 2, 1, 3], target=5
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

import unittest


class Solution(unittest.TestCase):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        result = 0
        for num_index in range(len(nums)):
            left, right = num_index + 1, len(nums) - 1

            while left < right:
                current_sum = nums[num_index] + nums[left] + nums[right]

                if current_sum < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1

        return result

    def test(self):
        nums, target = [-1, 0, 2, 3], 3
        expected = 2
        result = self.threeSumSmaller(nums, target)
        self.assertEqual(expected, result)


unittest.main()
