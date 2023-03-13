# Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any contiguous subarray of size ‘k’.

# * MARK: - Example 1
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# * MARK: - Example 2
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

import math
import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(1)
    def findMaxSumSubArrayOfSizeK(self, arr: list[int], k: int):
        max_sum = -math.inf
        window_start, window_sum = 0, 0.0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_end - window_start + 1 == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[window_start]
                window_start += 1
        return max_sum

    def test(self):
        arr, k = [2, 1, 5, 1, 3, 2], 3
        expected = 9
        result = self.findMaxSumSubArrayOfSizeK(arr, k)
        self.assertEqual(expected, result)


unittest.main()
