# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

# * MARK: - Example 1
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

# * MARK: - Example 2
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

import unittest


class Solution(unittest.TestCase):
    # k - count of "0" we can change

    # time_complexity: O(n)
    # space_complexity: O(1)
    def getLongestSubarrayAfterReplacement(self, arr, k):
        window_start, max_length, max_ones = 0, 0, 0

        for window_end in range(len(arr)):
            if arr[window_end] == 1:
                max_ones += 1
                        # window_size
            while window_end - window_start + 1 - max_ones > k:
                if arr[window_start] == 1:
                    max_ones -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    def test(self):
        arr, k = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3
        expected = 9
        result = self.getLongestSubarrayAfterReplacement(arr, k)
        self.assertEqual(expected, result)


unittest.main()
