# Middle of the LinkedList (easy)

# * MARK: - Problem statement
# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# * MARK: - Example 1
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# * MARK: - Example 2
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

# * MARK: - Example 3
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4

# * MARK: - Solution
# One brute force strategy could be to first count the number of nodes in the LinkedList
# and then find the middle node in the second iteration. Can we do this in one iteration?

# We can use the Fast & Slow pointers method such that the fast pointer is always
# twice the nodes ahead of the slow pointer.
# This way, when the fast pointer reaches the end of the LinkedList,
# the slow pointer will be pointing at the middle node.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    slow = head
    fast = head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

# * MARK: - Time Complexity
# The above algorithm will have a time complexity of O(N)
# where ‘N’ is the number of nodes in the LinkedList.

# * MARK: - Space Complexity
# The algorithm runs in constant space O(1)
