# Reverse Level Order Traversal (easy)

# * MARK: - Problem statement
# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e.,
# the lowest level comes first.
# You should populate the values of all nodes in each level from left to right in separate sub-arrays.

# * MARK: - Example
# ../images/08_tree_breadth_first_search/009.png

# * MARK: - Solution
# This problem follows the Binary Tree Level Order Traversal pattern.
# We can follow the same BFS approach. The only difference will be that instead of appending
# the current level at the end, we will append the current level at the beginning of the result list.

# Here is what our algorithm will look like; only the highlighted lines have changed.
# Please note that, for Java, we will use a LinkedList instead of an ArrayList for our result list.
# As in the case of ArrayList, appending an element at the beginning means shifting all the existing elements.
# Since we need to append the level array at the beginning of the result list,
# a LinkedList will be better, as this shifting of elements is not required in a LinkedList.
# Similarly, we will use a double-ended queue (deque) for Python, C++, and JavaScript.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.appendleft(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()

# * MARK: - Time Complexity
# The time complexity of the above algorithm is O(N),
# where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.

# * MARK: - Space Complexity
# The space complexity of the above algorithm will be O(N) as we need to return
# a list containing the level order traversal.
# We will also need O(N) space for the queue. Since we can have a maximum of N/2
# nodes at any level (this could happen only at the lowest level), therefore we will need O(N)
# space to store them in the queue.
