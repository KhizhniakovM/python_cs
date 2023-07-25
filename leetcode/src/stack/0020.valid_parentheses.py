# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

import unittest


class Solution(unittest.TestCase):
    def validParentheses(self, s):
        tmp_stack = []
        for letter_index in range(len(s)):
            if s[letter_index] == ")":
                if tmp_stack and tmp_stack[-1] == "(":
                    tmp_stack.pop()
                    continue
                else:
                    return False
            elif s[letter_index] == "}":
                if tmp_stack and tmp_stack[-1] == "{":
                    tmp_stack.pop()
                    continue
                else:
                    return False
            elif s[letter_index] == "]":
                if tmp_stack and tmp_stack[-1] == "[":
                    tmp_stack.pop()
                    continue
                else:
                    return False
            else:
                tmp_stack.append(s[letter_index])

        return len(tmp_stack) == 0

    def test(self):
        pass


unittest.main()
