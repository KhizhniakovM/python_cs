# 977. Squares of a Sorted Array (easy)

# Given an integer array nums sorted in non-decreasing order, return an array of the squares
# of each number sorted in non-decreasing order.


# Example 1:
# Input: nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
# Explanation: After squaring, the array becomes[16, 1, 0, 9, 100].
# After sorting, it becomes[0, 1, 9, 16, 100].

# Example 2:
# Input: nums = [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]

import unittest


class Solution(unittest.TestCase):
    def sortedSquares(self, nums):
        length = len(nums)
        left, right = 0, length - 1
        result = [None] * length
        biggest_index = length - 1

        while left <= right:
            left_x = nums[left] * nums[left]
            right_x = nums[right] * nums[right]

            if left_x > right_x:
                result[biggest_index] = left_x
                left += 1
            else:
                result[biggest_index] = right_x
                right -= 1
            biggest_index -= 1

        return result

    def test(self):
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        result = self.sortedSquares(nums)
        self.assertEqual(expected, result)


unittest.main()
