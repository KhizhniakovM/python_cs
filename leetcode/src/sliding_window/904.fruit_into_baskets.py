# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the
# ith tree produces.

# You want to collect as much fruit as possible.
# However, the owner has some strict rules that you must follow:

# 1. You only have two baskets, and each basket can only hold a single type of fruit.
#    There is no limit on the amount of fruit each basket can hold.
# 2. Starting from any tree of your choice, you must pick exactly one fruit from every tree
#    (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# 3. Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

# Given the integer array fruits, return the maximum number of fruits you can pick.

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

import unittest


class Solution(unittest.TestCase):
    # time_complexity: O(n)
    # space_complexity: O(len(trees))
    def getFruitIntoBaskets(self, trees):
        fruits_count = 0
        window_start = 0
        window_dict = {}

        for window_end in range(len(trees)):
            right_tree = trees[window_end]
            if right_tree not in window_dict:
                window_dict[right_tree] = 0
            window_dict[right_tree] += 1

            while len(window_dict) > 2:
                left_tree = trees[window_start]
                window_dict[left_tree] -= 1
                if window_dict[left_tree] == 0:
                    del window_dict[left_tree]
                window_start += 1

            fruits_count = max(fruits_count, window_end - window_start + 1)

        return fruits_count

    def test(self):
        trees = [1, 2, 3, 2, 2]
        expected = 4
        result = self.getFruitIntoBaskets(trees)
        self.assertEqual(expected, result)


unittest.main()
