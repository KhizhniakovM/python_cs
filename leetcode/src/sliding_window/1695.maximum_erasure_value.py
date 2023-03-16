# 1695. Maximum Erasure Value (medium)
# You are given an array of positive integers nums and want to erase a subarray
# containing unique elements. The score you get by erasing the subarray is equal
# to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a,
# that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


# Example 1:
# Input: nums = [4, 2, 4, 5, 6]
# Output: 17
# Explanation: The optimal subarray here is [2, 4, 5, 6].

# Example 2:
# Input: nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
# Output: 8
# Explanation: The optimal subarray here is [5, 2, 1] or [1, 2, 5].

import unittest


class Solution(unittest.TestCase):
    def getMaxErasureValue(self, nums):
        window_start, current_sum, max_sum = 0, 0, 0
        num_freq = {}

        for window_end in range(len(nums)):
            right_num = nums[window_end]

            if right_num not in num_freq:
                num_freq[right_num] = 0
            num_freq[right_num] += 1
            current_sum += right_num

            while num_freq[right_num] > 1:
                left_num = nums[window_start]
                num_freq[left_num] -= 1
                window_start += 1
                current_sum -= left_num

            max_sum = max(max_sum, current_sum)

        return max_sum

    def test(self):
        nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
        expected = 8
        result = self.getMaxErasureValue(nums)
        self.assertEqual(expected, result)


unittest.main()
