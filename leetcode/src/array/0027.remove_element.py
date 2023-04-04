# 27. Remove Element (easy)

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in
# nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain
# the elements which are not equal to val. The remaining elements of nums
# are not important as well as the size of nums.

# Return k.

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(1)
    def removeElement(self, nums, val):
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left
        # counter = 0
        # for num in nums:
        #     if num != val:
        #         nums[counter] = num
        #         counter += 1
        # return counter

    def test(self):
        nums, val = [0, 1, 2, 2, 3, 0, 4, 2],  2
        expected = 5
        result = self.removeElement(nums, val)
        print(nums)
        self.assertEqual(expected, result)


unittest.main()
