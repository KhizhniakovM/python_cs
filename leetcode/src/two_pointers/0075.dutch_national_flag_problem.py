# 75. Sort colors. Dutch National Flag Problem (medium)

# * MARK: - Problem statement
# Given an array containing 0s, 1s and 2s, sort the array in-place.
# You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue;
# and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# * MARK: - Example 1
# Input: [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]

# * MARK: - Example 2
# Input: [2, 2, 0, 1, 2, 0]
# Output: [0, 0, 1, 2, 2, 2]

import unittest


class Solution(unittest.TestCase):
    def sortColors(self, nums):
        low, high = 0, len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1

    def test(self):
        nums = [2, 2, 0, 1, 2, 0]
        expected = [0, 0, 1, 2, 2, 2]
        self.sortColors(nums)
        self.assertEqual(expected, nums)


unittest.main()
