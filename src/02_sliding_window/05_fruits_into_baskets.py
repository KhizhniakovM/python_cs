# Fruits into Baskets (medium)

# * MARK: - Problem Statement
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
# You will be given two baskets, and your goal is to pick as many fruits as possible to be placed
# in the given baskets.

# You will be given an array of characters where each character represents a fruit tree.
# The farm has following restrictions:

# 1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# 2. You can start with any tree, but you can’t skip a tree once you have started.
# 3. You will pick exactly one fruit from every tree until you cannot, i.e.,
#    you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both baskets.

# * MARK: - Example 1
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# * MARK: - Example 1
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

# * MARK: - Solution
# This problem follows the Sliding Window pattern and is quite similar to
# Longest Substring with K Distinct Characters.
# In this problem, we need to find the length of the longest subarray with no more than two distinct
# characters (or fruit types!).
# This transforms the current problem into Longest Substring with K Distinct Characters where K=2.

def fruits_into_baskets(fruits: list[str]) -> int:
    fruits_frequency: dict[str, int] = {}
    window_start = 0
    max_fruits_count = 0

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruits_frequency:
            fruits_frequency[right_fruit] = 0
        fruits_frequency[right_fruit] += 1

        while len(fruits_frequency) > 2:
            left_fruit = fruits[window_start]
            fruits_frequency[left_fruit] -= 1

            if fruits_frequency[left_fruit] == 0:
                del fruits_frequency[left_fruit]
            window_start += 1

        max_fruits_count = max(max_fruits_count, window_end - window_start + 1)

    return max_fruits_count

# * MARK: - Time Complexity
# The above algorithm’s time complexity will be O(N), where ‘N’ is the number of characters
# in the input array. The outer for loop runs for all characters, and the inner while loop processes
# each character only once; therefore, the time complexity of the algorithm will be O(N+N),
# which is asymptotically equivalent to O(N)

# * MARK: - Space Complexity
# The algorithm runs in constant space O(1)
# as there can be a maximum of three types of fruits stored in the frequency map.

# * MARK: - Similar Problems
# Problem 1: Longest Substring with at most 2 distinct characters

# Given a string, find the length of the longest substring in it with at most two distinct characters.

# Solution: This problem is exactly similar to our parent problem.
