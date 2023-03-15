# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# * MARK: - Example 1
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# * MARK: - Example 2
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# * MARK: - Example 3
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

# * MARK: - Example 4
# Input: String="cbbebi", K=10
# Output: 6
# Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(k)
    def findLongestSubstringLength(self, string: str, k: int) -> float:
        longest_substring = 0
        window_start = 0
        char_frequency = {}

        for window_end in range(len(string)):
            right_char = string[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1

            while len(char_frequency) > k:

                left_char = string[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

            window_size = window_end - window_start + 1
            longest_substring = max(longest_substring, window_size)

        return longest_substring

    def test(self):
        string, k = "araaci", 2
        expected = 4
        result = self.findLongestSubstringLength(string, k)
        self.assertEqual(expected, result)


unittest.main()
