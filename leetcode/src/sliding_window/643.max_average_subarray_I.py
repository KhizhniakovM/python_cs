# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average
# value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

import math
import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(1)
    def findMaxAverage(self, arr: list[int], k: int) -> float:
        result = -math.inf
        window_start, window_sum = 0, 0.0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_end - window_start + 1 == k:
                result = max(result, window_sum / k)
                window_sum -= arr[window_start]
                window_start += 1
        return result

    def test(self):
        testcase, k = [1, 12, -5, -6, 50, 3], 4
        expected_result = 12.75
        result = Solution.findMaxAverage(self, testcase, k)
        self.assertEqual(expected_result, result)


unittest.main()
