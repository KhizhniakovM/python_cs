# 2399. Check Distances Between Same Letters (easy)

# You are given a 0-indexed string s consisting of only lowercase English letters,
# where each letter in s appears exactly twice. You are also given a 0-indexed
# integer array distance of length 26.

# Each letter in the alphabet is numbered
# from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

# In a well-spaced string, the number of letters between the two occurrences
# of the ith letter is distance[i]. If the ith letter does not appear in s,
# then distance[i] can be ignored.

# Return true if s is a well-spaced string, otherwise return false.

# Example 1:
# Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: true
# Explanation:
# - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
# - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
# - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
# Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
# Return true because s is a well-spaced string.

# Example 2:
# Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: false
# Explanation:
# - 'a' appears at indices 0 and 1 so there are zero letters between them.
# Because distance[0] = 1, s is not a well-spaced string.

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n^2)
    # space_complexity: O(1)

    def checkDistances(self, s, distance):
        alphabet = 'abcdefghigklmnopqrstuvwxyz'
        for left_char_index in range(len(s)):
            right_char_index = len(s) - 1

            while s[left_char_index] != s[right_char_index] or left_char_index == right_char_index:
                right_char_index -= 1

            current_char = s[left_char_index]
            diff = abs(right_char_index - left_char_index) - 1
            alph_index = alphabet.index(current_char)
            if diff != distance[alph_index]:
                return False

        return True

    def test(self):
        s, distance = "abaccb", [1, 3, 0, 5, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = True
        result = self.checkDistances(s, distance)
        self.assertEqual(expected, result)


unittest.main()
