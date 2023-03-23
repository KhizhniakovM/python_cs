# 2006. Count Number of Pairs With Absolute Difference K (easy)

# Given an integer array nums and an integer k, return the number of pairs (i, j)
# where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:
# x if x >= 0.
# -x if x < 0.


# Example 1:
# Input: nums = [1,2,2,1], k = 1
# Output: 4

# Example 2:
# Input: nums = [1,3], k = 3
# Output: 0

# Example 3:
# Input: nums = [3,2,1,5,4], k = 2
# Output: 3


import unittest


class Solution(unittest.TestCase):

    def countKDifference(self, nums, k):
        # time_complexity: O(n^2)
        # space_complexity: O(1)
        # count = 0
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if abs(nums[i] - nums[j]) == k:
        #             count += 1

        # return count

        # time_complexity: O(n)
        # space_complexity: O(n)
        num_freq = {}
        count = 0

        for num in nums:
            if num not in num_freq:
                num_freq[num] = 1
            else:
                num_freq[num] += 1

        for num in nums:
            if num + k in num_freq:
                count += num_freq[num + k]

        return count

    def test(self):
        nums, k = [-1, 1, 3, 5], 2
        expected = 3
        result = self.countKDifference(nums, k)
        self.assertEqual(expected, result)


unittest.main()
