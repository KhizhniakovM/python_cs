# 2260. Minimum Consecutive Cards to Pick Up (medium)
# You are given an integer array cards where cards[i] represents the value of the ith card.
# A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to
# have a pair of matching cards among the picked cards. If it is impossible to
# have matching cards, return -1.


# Example 1:
# Input: cards = [3,4,2,3,4,7]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair
# of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

# Example 2:
# Input: cards = [1,0,5,3]
# Output: -1
# Explanation: There is no way to pick up a set of consecutive cards that
# contain a pair of matching cards.

import unittest


class Solution(unittest.TestCase):
    def minimumCardPickup(self, cards):
        window_start, min_length = 0, -1
        window_set = set()

        for window_end in range(len(cards)):
            right_card = cards[window_end]

            while right_card in window_set:
                if min_length == -1:
                    min_length = len(cards)
                min_length = min(min_length, window_end - window_start + 1)

                left_card = cards[window_start]
                window_set.remove(left_card)
                window_start += 1

            window_set.add(right_card)

        return min_length

    def test(self):
        cards = [3, 4, 2, 3, 4, 7]
        expected = 4
        result = self.minimumCardPickup(cards)
        self.assertEqual(expected, result)


unittest.main()
