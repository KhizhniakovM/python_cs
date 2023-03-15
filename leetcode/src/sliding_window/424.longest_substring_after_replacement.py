# You are given a string s and an integer k.
# You can choose any character of the string and change it to any
# other uppercase English character. You can perform this operation
# at most k times.

# Return the length of the longest substring containing the same
# letter you can get after performing the above operations.

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

# Input: s = "abccde", k = 1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(len(s))

    # s - string
    # k - count of letters we can replace
    def getLongestSubstringAfterReplacement(self, s, k):
        longest_substring, window_start, max_repeat_letter = 0, 0, 0
        char_freq = {}

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_freq:
                char_freq[right_char] = 0
            char_freq[right_char] += 1

            max_repeat_letter = max(max_repeat_letter, char_freq[right_char])

            while window_end - window_start + 1 - max_repeat_letter > k:
                left_char = s[window_start]
                char_freq[left_char] -= 1
                window_start += 1

            window_size = window_end - window_start + 1
            longest_substring = max(longest_substring, window_size)

        return longest_substring

    def test(self):
        s, k = "AABABBA", 1
        expected = 4
        result = self.getLongestSubstringAfterReplacement(s, k)
        self.assertEqual(expected, result)


unittest.main()
