# 1748. Sum of Unique Elements(easy)

# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

# Example 1:
# Input: nums = [1, 2, 3, 2]
# Output: 4
# Explanation: The unique elements are[1, 3], and the sum is 4.

# Example 2:
# Input: nums = [1, 1, 1, 1, 1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.

# Example 3:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 15
# Explanation: The unique elements are[1, 2, 3, 4, 5], and the sum is 15.

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(n)
    def sum_of_unique(self, nums):
        freq_num = {}
        result = 0
        for num in nums:
            if num not in freq_num:
                freq_num[num] = 0
            freq_num[num] += 1

        for num in nums:
            if freq_num[num] == 1:
                result += num
        return result

    def test(self):
        nums = [1, 2, 3, 2]
        expected = 4
        result = self.sum_of_unique(nums)
        self.assertEqual(expected, result)


unittest.main()
