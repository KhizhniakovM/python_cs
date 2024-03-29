# Level Order Successor (easy)

# * MARK: - Problem statement
# Given a binary tree and a node, find the level order successor of the given node in the tree.
# The level order successor is the node that appears right after the given node in the level order traversal.

# * MARK: - Example
# ../images/08_tree_breadth_first_search/013.png
# ../images/08_tree_breadth_first_search/014.png

# * MARK: - Solution
# This problem follows the Binary Tree Level Order Traversal pattern.
# We can follow the same BFS approach. The only difference will be that we will not keep
# track of all the levels. Instead we will keep inserting child nodes to the queue.
# As soon as we find the given node, we will return the next node from the queue as the level order successor.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if root is None:
        return None

    queue = deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        # break if we have found the key
        if currentNode.val == key:
            break

    return queue[0] if queue else None


def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    if result:
        print(result.val)

    result = find_successor(root, 12)
    if result:
        print(result.val)


main()

# * MARK: - Time Complexity
# The time complexity of the above algorithm is O(N),
# where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.

# * MARK: - Space Complexity
# The space complexity of the above algorithm will be O(N) which is required for the queue.
# Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
# therefore we will need O(N) space to store them in the queue.
