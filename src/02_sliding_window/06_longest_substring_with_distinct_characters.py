# Longest Substring with Distinct Characters (hard)

# * MARK: - Problem Statement
# Given a string, find the length of the longest substring, which has all distinct characters.

# * MARK: - Example 1
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".
# * MARK: - Example 2
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring with distinct characters is "ab".
# * MARK: - Example 3
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings with distinct characters are "abc" & "cde".

# * MARK: - Solution
# This problem follows the Sliding Window pattern, and we can use a similar dynamic
# sliding window strategy as discussed in Longest Substring with K Distinct Characters.
# We can use a HashMap to remember the last index of each character we have processed.
# Whenever we get a duplicate character, we will shrink our sliding window to ensure that
# we always have distinct characters in the sliding window.

def non_repeat_substring(string: str) -> int:
    char_frequency: dict[str, int] = {}
    window_start: int = 0
    max_length: int = 0

    for window_end in range(len(string)):
        right_char = string[window_end]

        if right_char in char_frequency:
            window_start = max(window_start, char_frequency[right_char] + 1)

        char_frequency[right_char] = window_end

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


# * MARK: - Time Complexity
# The above algorithm’s time complexity will be O(N), where ‘N’ is the number of characters
# in the input string.

# * MARK: - Space Complexity
# The algorithm’s space complexity will be O(K), where K
# is the number of distinct characters in the input string. This also means K<=N,
# because in the worst case, the whole string might not have any duplicate character,
# so the entire string will be added to the HashMap. Having said that, since we can expect a
# fixed set of characters in the input string (e.g., 26 for English letters),
# we can say that the algorithm runs in fixed space O(1); in this case,
# we can use a fixed-size array instead of the HashMap.
