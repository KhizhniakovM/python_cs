# Binary Number System and Its Representation
# In mathematics and digital electronics, a binary number is a number expressed in the base-2 number
# system, as it uses only two symbols: "0" and "1".

# * MARK: - What is the binary number system?
# Another number system that became famous after the decimal is the binary number system, which has only
# two digits, 0 and 1.

# If a number system has n digits, we say that the base of the number system is n. So the binary number
# system can also be called the base-2 number system.

# Why does a computer understand binary?
# The simplest explanation would be that a computer is an electrical device, and all electrical devices
# understand electrical signals, which have only two states.

# For example:
# If we have an input wire to this machine, there are only two possible states for this wire: either
# the current is flowing through this wire, or it is not flowing through this wire. If the current is
# flowing, we say that the state of this wire is signaled. And we say that the signal state corresponds to 1.

# If the current is not flowing, it is not signaled. The not signal state corresponds to 0. So, 1 and 0,
# in binary, translate to a signal or non-signal in an electrical device, and we can have multiple wires
# or multiple inputs to represent multiple ones and zeros.

# ../images/011.png

# As we see, the powers of 2 are increasing, so the bits go from right to left based on the decimal value
# given as input. All other left bits will be 0.

# For example:
# 125 can be represented as 01111101 in the computer binary system. Anything in computer language gets
# converted into a binary number system.

# * MARK: - What do binary numbers represent?
# In mathematics and digital electronics:

# - A binary number is a number expressed in the base-2 number system or binary number system.
# - It uses only two symbols: typically “0” (zero) and “1” (one).

# The base-2 number system is a positional notation with a radix of 2. Each digit is referred to as a bit.

# ? Binary counting
# Binary counting follows the same procedure, except that only the two symbols 0 and 1 are available.
# Thus, after a digit reaches 1 in binary, an increment resets it to 0 but also causes an increment of the
# next digit to the left.

# ../images/012.png

# Binary to decimal conversion
# In the binary system, each digit represents an increasing power of 2, with the rightmost digit representing 2^0,
# the next representing 2^1, then 2^2, and so on. The value of a binary number is the sum of the powers
# of 2 represented by each “1” digit. For example, the binary number 100101 is converted to decimal form as follows:

# Decimal to binary representation
# Below is the 32-bit binary representation.

# 5 -> 00000000 00000000 00000000 00000101
# Below is another widget that shows output in HTML. In the next lessons, we will cover this topic in-depth.

# ? Representing decimals & ASCII in binary
# A computer only understands byte-code that is made of 0’s and 1’s. We have to represent every decimal
# character as binary digits so a computer can understand the instructions we give.

# Decimal numbers in binary(8-bit representation)
# Each software programming language uses its own pre-defined sizes for primitive data types. So, let’s
# represent the rightmost 8-bits(1 byte) in binary.

# ../images/013.png
# ../images/014.png
