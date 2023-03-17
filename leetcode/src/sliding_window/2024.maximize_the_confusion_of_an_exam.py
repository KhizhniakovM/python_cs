# 2024. Maximize the Confusion of an Exam (medium)
# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F'
# denoting false. He wants to confuse the students by maximizing the number of consecutive
# questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith
# question. In addition, you are given an integer k, the maximum number of times you may
# perform the following operation:

# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing
# the operation at most k times.

# Example 1:
# Input: answerKey = "TTFF", k = 2
# Output: 4
# Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
# There are four consecutive 'T's.

# Example 2:
# Input: answerKey = "TFFT", k = 1
# Output: 3
# Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
# Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
# In both cases, there are three consecutive 'F's.

# Example 3:
# Input: answerKey = "TTFTTFTT", k = 1
# Output: 5
# Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
# Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT".
# In both cases, there are five consecutive 'T's.

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(1)
    def maxConsecutiveAnswers(self, answerKey, k):
        window_start, max_length = 0, 0
        max_t, max_f = 0, 0

        for window_end in range(len(answerKey)):
            right_char = answerKey[window_end]

            if right_char == "T":
                max_t += 1
            else:
                max_f += 1

            while window_end - window_start + 1 - max_t > k and window_end - window_start + 1 - max_f > k:
                left_char = answerKey[window_start]
                if left_char == "T":
                    max_t -= 1
                else:
                    max_f -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    def test(self):
        answerKey, k = "TTFTTFTT", 1
        expected = 5
        result = self.maxConsecutiveAnswers(answerKey, k)
        self.assertEqual(expected, result)


unittest.main()
