# Given a string s, find the length of the longest
# substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

import unittest


class Solution(unittest.TestCase):
    def getMaxSubstringLength(self, s):
        longest_substring = 0
        window_start = 0
        char_freq = {}
        
        # Simple solution
        # for window_end in range(len(s)):
        #     right_char = s[window_end]
        #     if right_char not in char_freq:
        #         char_freq[right_char] = 0
        #     char_freq[right_char] += 1

        #     while char_freq[right_char] > 1:
        #         left_char = s[window_start]
        #         char_freq[left_char] -= 1
        #         if char_freq[left_char] == 0:
        #             del char_freq[left_char]
        #         window_start += 1

        #     window_size = window_end - window_start + 1
        #     longest_substring = max(longest_substring, window_size)

        # Tricky solution
        # We can save index of our char to jump exactly into it
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_freq:
                window_start = max(window_start, char_freq[right_char] + 1)

            char_freq[right_char] = window_end
            window_size = window_end - window_start + 1
            longest_substring = max(longest_substring, window_size)

        return longest_substring

    def test(self):
        s = "abcabcbb"
        expected = 3
        result = self.getMaxSubstringLength(s)
        self.assertEqual(expected, result)


unittest.main()
