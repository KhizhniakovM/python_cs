# House thief

# There are n houses built in a line. A thief wants to steal the maximum possible money from these houses.
# The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert
# the security system. How should the thief maximize his stealing?

# * MARK: - Problem Statement
# Given a number array representing the wealth of n houses, determine the maximum amount of money the
# thief can steal without alerting the security system.

# ? Example 1:
# Input: {2, 5, 1, 3, 6, 2, 4}
# Output: 15
# Explanation: The thief should steal from houses 5 + 6 + 4

# ? Example 2:
# Input: {2, 10, 14, 8, 1}
# Output: 18
# Explanation: The thief should steal from houses 10 + 8

# Let’s first start with a recursive brute-force solution.

# * MARK: - Basic Solution
# For every house i, we have two options:

# 1. Steal from the current house (i), skip one and steal from (i+2).
# 2. Skip the current house (i), and steal from the adjacent house (i+1).

# The thief should choose the one with the maximum amount from the above two options. So our algorithm will
# look like this:

def find_max_steal_basic(wealth):
    return find_max_steal_recursive_basic(wealth, 0)


def find_max_steal_recursive_basic(wealth, currentIndex):

    if currentIndex >= len(wealth):
        return 0

    # steal from current house and skip one to steal next
    stealCurrent = wealth[currentIndex] + \
        find_max_steal_recursive_basic(wealth, currentIndex + 2)
    # skip current house to steel from the adjacent house
    skipCurrent = find_max_steal_recursive_basic(wealth, currentIndex + 1)

    return max(stealCurrent, skipCurrent)


def main_basic():

    print(find_max_steal_basic([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_basic([2, 10, 14, 8, 1]))


main_basic()

# The time complexity of the above algorithm is exponential O(2^n). The space complexity is O(n)
# which is used to store the recursion stack.

# * MARK: - Top-down Dynamic Programming with Memoization
# To resolve overlapping subproblems, we can use an array to store the already solved subproblems.

# Here is the code:


def find_max_steal_TD(wealth):
    dp = [0 for x in range(len(wealth))]
    return find_max_steal_recursive_TD(dp, wealth, 0)


def find_max_steal_recursive_TD(dp, wealth, currentIndex):
    if currentIndex >= len(wealth):
        return 0

    if dp[currentIndex] == 0:
        # steal from current house and skip one to steal next
        stealCurrent = wealth[currentIndex] + \
            find_max_steal_recursive_TD(dp, wealth, currentIndex + 2)
        # skip current house to steel from the adjacent house
        skipCurrent = find_max_steal_recursive_TD(dp, wealth, currentIndex + 1)

        dp[currentIndex] = max(stealCurrent, skipCurrent)

    return dp[currentIndex]


def main_TD():

    print(find_max_steal_TD([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_TD([2, 10, 14, 8, 1]))


main_TD()

# * MARK: - Bottom-up Dynamic Programming
# Let’s try to populate our dp[] array from the above solution, working in a bottom-up fashion. As we saw in
# the above code, every findMaxStealRecursive() is the maximum of the two recursive calls; we can use this
# fact to populate our array.


def find_max_steal_BU(wealth):
    n = len(wealth)
    if n == 0:
        return 0
    dp = [0 for x in range(n+1)]  # '+1' to handle the zero house
    dp[0] = 0  # if there are no houses, the thief can't steal anything
    dp[1] = wealth[0]  # only one house, so the thief have to steal from it

    # please note that dp[] has one extra element to handle zero house
    for i in range(1, n):
        dp[i + 1] = max(wealth[i] + dp[i - 1], dp[i])

    return dp[n]


def main_BU():

    print(find_max_steal_BU([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_BU([2, 10, 14, 8, 1]))


main_BU()

# The above solution has time and space complexity of O(n)

# * MARK: - Memory optimization
# We can optimize the space used in our previous solution. We don’t need to store all the previous numbers
# up to n, as we only need two previous numbers to calculate the next number in the sequence. Let’s use
# this fact to further improve our solution:


def find_max_steal(wealth):
    n = len(wealth)
    if n == 0:
        return 0

    n1, n2 = 0, wealth[0]
    for i in range(1, n):
        n1, n2 = n2, max(n1 + wealth[i], n2)

    return n2


def main():

    print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal([2, 10, 14, 8, 1]))


main()

# The above solution has a time complexity of O(n) and a constant space complexity O(1)

# * MARK: - Fibonacci number pattern
# We can clearly see that this problem follows the Fibonacci number pattern. The only difference is that every
# Fibonacci number is a sum of the two preceding numbers, whereas in this problem every number (total wealth)
# is the maximum of previous two numbers.
