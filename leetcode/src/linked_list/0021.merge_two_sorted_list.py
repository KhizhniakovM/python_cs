# 21. Merge Two Sorted Lists (easy)

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by
# splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(unittest.TestCase):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head

        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    current.next = list1
                    current = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    current = list2
                    list2 = list2.next
            else:
                if list1 is None and list2 is not None:
                    current.next = list2
                    current = list2
                    list2 = list2.next
                else:
                    current.next = list1
                    current = list1
                    list1 = list1.next

        return head

    def test(self):
        pass

    unittest.main()
