# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(n)
    def findAllAnagrams(self, s, p):
        window_start, matched = 0, 0
        result = []
        p_freq = {}

        for char in p:
            if char not in p_freq:
                p_freq[char] = 0
            p_freq[char] += 1

        for window_end in range(len(s)):
            right_char = s[window_end]

            if right_char in p_freq:
                p_freq[right_char] -= 1
                if p_freq[right_char] == 0:
                    matched += 1

            if matched == len(p_freq):
                result.append(window_start)

            if window_end >= len(p) - 1:
                left_char = s[window_start]
                window_start += 1

                if left_char in p_freq:
                    if p_freq[left_char] == 0:
                        matched -= 1
                    p_freq[left_char] += 1

        return result

    def test(self):
        s, p = "cbaebabacd", "abc"
        expected = [0, 6]
        result = self.findAllAnagrams(s, p)
        self.assertEqual(expected, result)


unittest.main()
