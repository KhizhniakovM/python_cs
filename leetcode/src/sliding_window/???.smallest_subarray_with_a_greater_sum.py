# Given an array of positive numbers and a positive number ‘S’
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0 if no such subarray exists.

# * MARK: - Example 1
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

# * MARK: - Example 2
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# * MARK: - Example 3
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

import math
import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(1)
    def findSmallestSubarrayWithAGreaterSum(self, arr, s):
        smallest_length = math.inf
        window_start, window_sum = 0, 0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while (window_sum >= s):
                window_size = window_end - window_start + 1
                smallest_length = min(smallest_length, window_size)

                window_sum -= arr[window_start]
                window_start += 1

        if smallest_length == math.inf:
            return 0
        return smallest_length

    def test(self):
        testcase, k = [2, 1, 5, 2, 8], 7
        result = self.findSmallestSubarrayWithAGreaterSum(testcase, k)
        expected = 1
        self.assertEqual(expected, result)


unittest.main()
