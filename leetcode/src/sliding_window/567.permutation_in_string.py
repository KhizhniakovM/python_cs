# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(n)
    def hasPattern(self, string, pattern):
        # Method with comparing two HashMap
        # window_start = 0
        # pattern_map = {}
        # window_map = {}

        # for char in pattern:
        #     if char not in pattern_map:
        #         pattern_map[char] = 0
        #     pattern_map[char] += 1

        # for window_end in range(len(string)):
        #     right_char = string[window_end]
        #     if right_char not in window_map:
        #         window_map[right_char] = 0
        #     window_map[right_char] += 1

        #     if window_end - window_start + 1 == len(pattern):
        #         if pattern_map == window_map:
        #             return True
        #         left_char = string[window_start]
        #         window_map[left_char] -= 1
        #         if window_map[left_char] == 0:
        #             del window_map[left_char]
        #         window_start += 1

        # return False

        # Method with using counter
        window_start, matching = 0, 0
        pattern_map = {}
        for char in pattern:
            if char not in pattern_map:
                pattern_map[char] = 0
            pattern_map[char] += 1

        for window_end in range(len(string)):
            right_char = string[window_end]
            if right_char in pattern_map:
                pattern_map[right_char] -= 1
                if pattern_map[right_char] == 0:
                    matching += 1

            if matching == len(pattern_map):
                return True

            if window_end >= len(pattern) - 1:
                left_char = string[window_start]
                window_start += 1
                if left_char in pattern_map:
                    if pattern_map[left_char] == 0:
                        matching -= 1
                    pattern_map[left_char] += 1

        return False

    def test(self):
        string, pattern = "abcdeabcdx", "abcdxabcde"
        expected = True
        result = self.hasPattern(string, pattern)
        self.assertEqual(expected, result)


unittest.main()
