# 713. Subarray Product Less Than K(medium)

# Given an array of integers nums and an integer k,
# return the number of contiguous subarrays where the product of
# all the elements in the subarray is strictly less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that[10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Example 2:
# Input: nums = [1, 2, 3], k = 0
# Output: 0

import unittest


class Solution(unittest.TestCase):
    def numSubarrayProductLessThanK(self, nums, k):
        result = []
        window_start, window_product = 0, 1
        for window_end in range(len(nums)):
            right_num = nums[window_end]
            window_product *= right_num

            while window_product >= k and window_start <= window_end:
                window_product /= nums[window_start]
                window_start += 1

            tmp_list = []
            for i in range(window_end, window_start - 1, -1):
                tmp_list.insert(0, nums[i])
                result.append(list(tmp_list))

        return result

    def test(self):
        nums, k = [8, 2, 6, 5], 50
        expected = [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
        result = self.numSubarrayProductLessThanK(nums, k)
        print(result)
        self.assertEqual(expected, result)


unittest.main()
