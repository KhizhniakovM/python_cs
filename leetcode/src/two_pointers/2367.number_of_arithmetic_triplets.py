# 2367. Number of Arithmetic Triplets(easy)

# You are given a 0-indexed, strictly increasing integer array nums and a
# positive integer diff. A triplet(i, j, k) is an arithmetic triplet
# if the following conditions are met:
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.

# Return the number of unique arithmetic triplets.

# Example 1:
# Input: nums = [0, 1, 4, 6, 7, 10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

# Example 2:
# Input: nums = [4, 5, 6, 7, 8, 9], diff = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n^2)
    # space_complexity: O(1)
    def arithmeticTriplets(self, nums, diff):
        counter = 0
        for n in nums:
            if n + diff in nums and n + diff + diff in nums:
                counter += 1
        return counter

    def test(self):
        nums, diff = [0, 1, 4, 6, 7, 10], 3
        expected = 2
        result = self.arithmeticTriplets(nums, diff)
        self.assertEqual(expected, result)


unittest.main()
