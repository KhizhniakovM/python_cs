# 2200. Find All K-Distant Indices in an Array (easy)

# You are given a 0-indexed integer array nums and two integers key and k.
# A k-distant index is an index i of nums for which there exists at least
# one index j such that |i - j| <= k and nums[j] == key.

# Return a list of all k-distant indices sorted in increasing order.

# Example 1:
# Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
# Output: [1,2,3,4,5,6]
# Explanation: Here, nums[2] == key and nums[5] == key.
# - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key.
# Thus, 0 is not a k-distant index.
# - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
# - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
# - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
# - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
# - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
# - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
# Thus, we return [1,2,3,4,5,6] which is sorted in increasing order.

# Example 2:
# Input: nums = [2,2,2,2,2], key = 2, k = 2
# Output: [0,1,2,3,4]
# Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index.
# Hence, we return [0,1,2,3,4].

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n^2)
    # space_complexity: O(n)
    def findKDistantIndices(self, nums, key, k):
        key_indexes, result = [], []

        for num_index in range(len(nums)):
            if nums[num_index] == key:
                key_indexes.append(num_index)

        for num_index in range(len(nums)):
            for key_index in key_indexes:
                if abs(num_index - key_index) <= k:
                    result.append(num_index)
                    break

        return result

    def test(self):
        nums, key, k = [2, 2, 2, 2, 2], 2, 2
        expected = [0, 1, 2, 3, 4]
        result = self.findKDistantIndices(nums, key, k)
        self.assertEqual(expected, result)


unittest.main()
