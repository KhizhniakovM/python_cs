# 202. Happy Number (easy)

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

import unittest


class Solution(unittest.TestCase):
    def happy_number(self, n):
        # space_complexity: O(n)
        # time_complexity: O(n)
        # seen = set()
        # while n != 1:
        #     seen.add(n)
        #     split = [int(x) for x in str(n)]
        #     n = 0
        #     for s in split:
        #         s *= s
        #         n += s
        #     if n in seen:
        #         return False
        # return True

        # time_complexity: O(n)
        # space_complexity: O(1)
        slow, fast = n, n
        while True:
            slow = self.find_square(slow)
            fast = self.find_square(self.find_square(fast))
            if slow == fast:
                break 

        return slow == 1

    def find_square(self, n):
        summ = 0
        for x in str(n):
            summ += int(x) ** 2
        return summ

    def test(self):
        n = 2
        expected = False
        result = self.happy_number(n)
        self.assertEqual(expected, result)


unittest.main()
