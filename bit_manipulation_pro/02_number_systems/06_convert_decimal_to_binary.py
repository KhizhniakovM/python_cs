# Convert Decimal Number to Binary Number
# In this lesson, we will write the code to count the number of bits present for a given input.

# * MARK: - Introduction
# Given a decimal number, continue dividing the number by 2 until it reaches either 0/1 and record the
# remainder at each step. The resulting list of remainders is the equivalent binary number for your decimal number.

# For example:
# Input: 125
# Output: 1111101

# Repeatedly do the modulo operation until n becomes 0 using “%” and “division” operations.
# So, using the modulo and division method, we calculate the binary representation of a decimal number.
# Let’s represent the binary by considering the remainder column from bottom to top.

# (125)_{10} becomes (1111101)_{2}

# The illustration below explains the process of counting the digits in an integer.
# ../images/016.png

# ../images/017.png
# ../images/018.png
# ../images/019.png
# ../images/020.png
# ../images/021.png
# ../images/022.png
# ../images/023.png
# ../images/024.png
# ../images/025.png

# * MARK: - Problem statement
# Given an integer, return the number of bits present in an integer input.

# ? Example  # 1:
# Input:  n = 125
# Output: 7 (1, 1, 1, 1, 1, 0, 1)

# ? Example  # 2:
# Input:  n = 129
# Output: 8 (1, 0, 0, 0, 0, 0, 0, 1)

# ? Approach  # 1: Bit-shifting
# This is an example problem for converting from decimal to an integer. Solving this problem helps us
# to understand how bits are stacked together to form a decimal number. Let’s see some of the approaches
# to solve this algorithmic problem.

# We used the right-shift operator here >> . It divides the number 2 ^ {k} times, so, k = 1.

# Right Shift Formula:
# num >> 1 is equivalent to num / 2

# ? Implementation
# We only count the number of bits present in the number.

def decimal_to_binary_bit_shift(n: int) -> int:
    count: int = 0

    while n > 0:
        n >>= 1
        count += 1

    return count


print(decimal_to_binary_bit_shift(125))


# ? Approach  # 2: Using stacks
# Let’s represent the bits present in the number in an array of integers.

def decimal_to_binary_stack(n: int) -> list:
    array: list = []

    while n > 0:
        remainder: int = n % 2
        array.append(remainder)
        n >>= 1  # equivalent to n / 2

    return list(reversed(array))


print(decimal_to_binary_stack(245))

# As we receive the bits in reverse order, we use a stack for popping them one-by-one and storing them in
# an array of integers. So, the resultant bits array is { 1, 1, 1, 1, 1, 0, 1 } for the number 125.

# ? Complexity analysis:
# Time complexity: O(logn)
# The run time for this algorithm is: O(log N).

# With each iteration, we halve the number until we reach either 0 or 1. You only divide a number n recursively
# into halves at most log2(n) times, which is the boundary of the recursion.

# 2·2·…·2·2 = 2x ≤ n ⇒ log2(2 ^ x) = x ≤ log2(n)

# Hence, the time complexity takes logarithmic time.
# To understand more on this logarithmic approach, please search for “Master Theorem”.

# Space complexity: O(n / 2) or O(n)
# The space complexity is O(n + m).

# The extra space required depends on the number of items stored in the stack, which stores exactly n / 2
# elements. We also used an Integer array to store the bits, and the extra space required depends on the
# number of items stored in the int[] array, which stores exactly m / 2 elements.

# Hence, the overall space used is n / 2 + m / 2, which is O(n+m).

# ? Approach  # 3: Bit shifting(optimal)
# Using Bit-shifting is fast and easy.
# We have already seen how the bits stacked together for the number 125 using the stack approach.

# Now, imagine the binary 2 powers from right to left, which are arranged like below.

# 2 ^ 32........... 2 ^ {7}, 2 ^ {6}, 2 ^ {5}, 2 ^ {34}, 2 ^ {3}, 2 ^ {2}, 2 ^ {1}, 2 ^ {0}

# So, the binary representation of 125 is {1, 1, 1, 1, 1, 0, 1}.

# Note: Left shifting any number results in multiplying it with powers of 2.

# 1 << 0 = 1 * 2 ^ 0 = 1 * 1 = 1
# 1 << 1 = 1 * 2 ^ 1 = 1 * 2 = 2
# 1 << 2 = 1 * 2 ^ 2 = 1 * 4 = 4

# So, on each iteration, we get 1, 2, 4, 8, 16, 31, 64, 128, and so on.

# So, until 64, the loop runs, and when 128 is encountered, the loop terminates as 128 <= 125 fails.


def bit_lenght(n: int) -> int:
    counter: int = 0

    while 1 << counter <= n:
        counter += 1

    return counter


print(bit_lenght(245))
