# 26. Remove Duplicates from Sorted Array (easy)

# Given an integer array nums sorted in non-decreasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order of
# the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first
# k elements of nums should hold the final result. It does not matter what you leave
# beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.


# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

import unittest


class Solution(unittest.TestCase):
    def removeDuplicates(self, nums):
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                
        return left + 1

    def test(self):
        nums = [1, 2]
        expected = 2
        result = self.removeDuplicates(nums)
        self.assertEqual(expected, result)


unittest.main()
