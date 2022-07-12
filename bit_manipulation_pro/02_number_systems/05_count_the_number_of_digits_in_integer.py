# Count the Number of Digits in an Integer
# In this lesson, we will write code to count the number of digits in an integer.

# * MARK: - How to count the number of digits in an integer
# Given a decimal number, continue dividing the number by ten until it reaches 0 and records the
# remainder at each step.

# The resulting list of remainders is the equivalent place values of the Integer.

# ? Example:
# Input: 125
# Output: 3

# The illustration below explains the process of counting the digits in an integer.
# ../images/015.png

# * MARK: - Problem statement
# Given an integer, return the number of digits present in an integer input.

# ? Example  # 1:
# Input:  n = 125
# Output: 3
# Explanation: The number of digits present in input `n` is 3 (1, 2, 5).

# ? Example  # 2:
# Input:  n = 1256
# Output: 4
# Explanation: The number of digits present in input `n` is 4 (1, 2, 5, 6).

# * MARK: - Solution
# This is an example problem for counting digits in an integer. Solving this problem helps you find the
# place values and how they are represented in the decimal number system.

# Let’s see some of the approaches we can take to solve this algorithmic problem.

# ? Approach  # 1: Division [while loop]#
# In this program, while loop is iterated until the expression number != 0 is evaluated to 0 (false).

# Let’s see the iterations for number = 125.

# Iterations
# - After the first iteration, n(125) will be divided by 10, and its value will be 12, and the count is incremented to 1.
# - After the second iteration, the value of n(12) will be 1 and , the count is incremented to 2.
# - After the third iteration, the value of n(1) will be 0, and the count is incremented to 3.

# Then the expression is evaluated to false, as n is 0, and the loop terminates.

import math


def count_digits_loop(n: int) -> int:
    counter: int = 0

    while n > 0:
        n = math.floor(n / 10)
        counter += 1

    return counter


print(count_digits_loop(125))


# ? Time and space complexities
# Time complexity: O(n)
# The run time depends on the number of digits in n. In the worst case, it iterates through all the digits
# until it becomes 0.

# Space complexity: O(1)
# The space complexity is O(1) since no additional space is allocated.

# ? Approach  # 2: Logarithmic#
# We can use log_10 (logarithm of base 10) to count the number of digits of positive numbers.

# Digit count of N = upper bound of log_10(N).

# Note: Logarithms are not defined for negative numbers.

# log(0) is infinity

def count_digits_log(n: int) -> int:
    return -1 if n <= 0 else math.floor(math.log10(n) + 1)


print(count_digits_log(125))


# Some of the other ways to achieve this are shown below.

# Beware, these approaches are not recommended, as the time and space complexities are high.

# ? Approach  # 3: Recursive
# This recursive approach might be ineffective if we are dealing with a large integer n.

# A recursive call adds a stack entry every time it runs and again when once it reaches the base condition.
# It then backtracks and executes each recursive function.

def count_digits_rec(n: int) -> int:
    if n == 0:
        return 0
    return 1 + count_digits_rec(math.floor(n / 10))


print(count_digits_rec(125))


# Approach  # 4: Convert to string
# This is one of the ways to implement/solve the problem, but it is not recommended, as we are converting
# one type of data to another.

def count_digits_convert(n: int) -> int:
    return len(str(n))


print(count_digits_convert(125))
