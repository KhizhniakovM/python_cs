# Challenge 1: Count Set Bits
# This is a traditional problem counting the number of set bits or 1's present in a number.

# * MARK: - Introduction
# Let’s see how we can count the set bits using the AND operator.

# What are set-bits?
# 1 = set-bit
# 0 = unset-bit

# For example:
# Input: 5
# Output: 0101 ( in binary)
# There are two set bits are two in the above example, as we have two 1’s in the binary representation.

# * MARK: - Problem statement
# Write a program to count set bits of an integer.

# Input: 125

# Output: 6
# Explanation: Input has six 1’s or set-bits so the output will be 6.

# * MARK: - Basic solution
# In this program, a while-loop is iterated until the expression number > 0 is evaluated to 0 (false).

# Let’s see the iterations for number = 125.

# Iterations
# - After the first iteration, number(125) will be divided by 2, its value will be 62, and the count incremented to 1.
# - After the second iteration, the value of number(62) will be 31 and , the count incremented to 2.
# - After the third iteration, the value of number(31) will be 15, and the count incremented to 3.
# - And so on.

# Then the expression is evaluated to false since the number is 0, and the loop terminates.

# ../images/035.png

def count_set_bit(n: int) -> int:
    result: int = 0
    while n > 0:
        if (n % 2 != 0):
            result += 1
        n //= 2
    return result


print(count_set_bit(125))

# We can further rewrite this code using the & operator as seen below.


def count_set_bit_another(n: int) -> int:
    result: int = 0
    while n > 0:
        if (n & 1 == 1):
            result += 1
        n >>= 1
    return result


print(count_set_bit_another(125))

# This can be further simplified as shown below:


def count_set_bit_simplified(n: int) -> int:
    result: int = 0
    while n > 0:
        result += n & 1
        n >>= 1
    return result


print(count_set_bit_simplified(125))

# * MARK: - Time and space complexities
# Time complexity: O(Total bits in n) / O(1) in simple terms
# The time taken is proportional to the total bits in binary representation, which means
# int takes 32 bits = > O(32 bits) time.
# long takes 64 bits = > O(64 bits) time.

# So, time taken is O(Total bits in n, which can be an int or long, etc.).
# The run time depends on the number of bits in n. In the worst case, all bits in n are 1-bits.
# In the case of a 32-bit integer, the run time is O(32) or O(1).

# Space complexity: O(1) extra space
# The space complexity is O(1). No extra space is allocated.

# * MARK: - Best solution
# We saw an algorithm to solve this problem in the previous lesson. Let’s see how to solve this in a more
# efficient way using Briann’s Algorithm.

# ? Brian Kernighan’s algorithm
# This is a faster execution than the previous naive approach.

# In this approach, we count only the set bits. So,
# - If a number has 2 set bits, then the while loop runs two times.
# - If a number has 4 set bits, then the while loop runs four times.

# For example, let us consider the example n = 125 and calculate using this algorithm.

#             n = 40 => 00000000 00000000 00000000 00101000
#         n - 1 = 39 => 00000000 00000000 00000000 00100111
# -----------------------------------------------------------
# (n & (n - 1)) = 32 => 00000000 00000000 00000000 00100000
# -----------------------------------------------------------

# Now n is 32, so we can calculate this to:
#          n  = 32    => 00000000 00000000 00000000 00100000
#       n - 1 = 31    => 00000000 00000000 00000000 00011111
# -----------------------------------------------------------
# (n & (n - 1)) = 0   => 00000000 00000000 00000000 00000000
# -----------------------------------------------------------

# * MARK: - Time and space complexities
# Time complexity: O(Set Bit count) / O(1) in simple terms
# The time taken is proportional to set bits in binary representation.

# So, time taken is O(SetBit Count).
# The run time depends on the number of set bits in n. In the worst case, all bits in n are 1-bits. In the case
# of a 32-bit integer, the run time is O(32) or O(1)

# Space complexity: O(1) extra space
# The space complexity is O(1). No additional space is allocated.

# Lookup table approach
# This approach is considered to be one of the fastest, as it uses a lookup table.

# - Why below algorithm is faster than previous approaches?
# - Lookup based approach.
# - This approach requires an O(1) time solution to count the set bits.
# - However, this requires some preprocessing.
# - So, we divide our 32-bit input into 8-bit chunks, so there are four chunks.
# - We have 8 bits in each chunk, then the range is from 0 - 255 (0 to 2^7 - 1).
# - So, we may need to count set bits from o to 255 in individual chunks.


def count_set_bit_best(n: int) -> int:
    table: list = list(range(256))

    for i in range(1, 256):
        table[i] = (i & 1) + table[i >> 1]

    result = 0
    for i in range(4):
        result += table[n & 0xff]
        n >>= 8

    return result


print(count_set_bit_best(125))

# We are initializing the table with the set bit count per each ith place.

# Algorithm:

# - Initialize table[0] with 0.
# - Loop through, in the range from 1 to 256
#   - for i = 1,
#      - table[1] = (1 & 1) + table[1 / 2] => table[1] = 1 + table[0]; => table[1] = 1.
#      - table[2] = (2 & 1) + table[2 / 2] => table[2] = 0 + table[1]; => table[2] = 1.
#      - table[3] = (3 & 1) + table[3 / 2] => table[3] = 1 + table[1]; => table[3] = 2. so on…
# - Initialize int res = 0.
# - Loop through, in the range from 0 to 3
#   - To check on each of the 4 8-bit chunks using res += table[n & 0xff];
#   - Shift n by 8 bits (n >>= 8), we do this to get the second last 8 bits…
#   - End loop.
# - Return res.

# ? Time and space complexities
# Time complexity: O(1) in simple terms
# This requires an O(1) time solution to count the set bits in each of the 8-bit chunks.

# Space complexity: O(1) extra space
# The space complexity is O(1). No additional space is allocated.
