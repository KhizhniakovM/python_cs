# Introduction to AND
# Bitwise AND is the most commonly used logical Bitwise operator. It is represented by a sign (&).

# What is the Bitwise AND operator?
# AND operator is the same as AND gate we studied in the chapter on digital electronics, as shown below:

# ../images/026.png

# The Bitwise AND operator is denoted by &. When an AND gate is given with two inputs, the corresponding
# output will be:

# - If two input bits are 1, the output is 1.
# - In all other cases its 0, for example
#   - 1 & 0 => yields to 0.
#   - 0 & 1 => yields to 0.
#   - 0 & 0 => yields to 0.

# AND compares each bit of the first operand to the second operand’s corresponding bit. If both bits are 1,
# the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.

# ../images/027.png


# * MARK: - Bitwise AND, Computations, and Examples
# Here, we discuss the '&' operator in more detail.

# * MARK: - Bitwise AND
# A Bitwise AND is a binary operation that takes two equal-length binary representations and performs the
# logical AND operation on each pair of the corresponding bits. This is equivalent to multiplying them.

# Bitwise ANDing any number x with 0 yields 0

# The Bitwise AND operator does the following:

# - It is a binary operator that takes two numbers.
# - When we do Bitwise & of these two numbers, it considers the binary representation of these two numbers.
# - Bitwise AND compares bit by bit in binary representation, and whatever binary representation you get,
#   the corresponding integer is returned as an output.

# The integer data type takes 4 bytes in C, C++, and Java.

# 4 bytes = 4 * (8 bits) = 32 bits. {1 byte = 8 bits}
# Let’s see one of the above examples in binary representation.

# For simplicity, let’s represent these in 16-bit instead of 32-bit binary.

# a = 12
# b = 10
# ---------------------------------
# a in Binary: 0000 0000 0000 1100
# b in Binary: 0000 0000 0000 1010
# ---------------------------------
# a & b: 0000 0000 0000 1000
# ---------------------------------
# The & operation starts from the rightmost bit traversing towards the leftmost bit in the 32-bit binary
# representation.

# Let’s visualize the steps below.

# bit_manipulation_pro/images/028.png
# bit_manipulation_pro/images/029.png
# bit_manipulation_pro/images/030.png
# bit_manipulation_pro/images/031.png
# bit_manipulation_pro/images/032.png
# bit_manipulation_pro/images/033.png
# bit_manipulation_pro/images/034.png

# Below is code representation of the & operator.
a = 10
b = 12

print(f"Bitwise AND of {a}, {b} is: {a & b}")
