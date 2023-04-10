# 876. Middle of the Linked List (easy)

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(unittest.TestCase):
    def middle_node(self, head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow 
    
    def test(self):
        pass


unittest.main()
