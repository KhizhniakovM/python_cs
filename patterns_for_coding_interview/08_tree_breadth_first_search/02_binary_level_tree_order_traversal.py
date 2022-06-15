# Binary Tree Level Order Traversal (easy)

# * MARK: - Problem statement
# Given a binary tree, populate an array to represent its level-by-level traversal.
# You should populate the values of all nodes of each level from left to right in separate sub-arrays.

# * MARK: - Example
# ../images/08_tree_breadth_first_search/001.png

# * MARK: - Solution
# Since we need to traverse all nodes of each level before moving onto the next level,
# we can use the Breadth First Search (BFS) technique to solve this problem.

# We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

# 1. Start by pushing the root node to the queue.
# 2. Keep iterating until the queue is empty.
# 3. In each iteration, first count the elements in the queue (let’s call it levelSize).
#    We will have these many nodes in the current level.
# 4. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
# 5. After removing each node from the queue, insert both of its children into the queue.
# 6. If the queue is not empty, repeat from step 3 for the next level.

# Let’s take the example-2 mentioned above to visually represent our algorithm:

# ../images/08_tree_breadth_first_search/002.png
# ../images/08_tree_breadth_first_search/003.png
# ../images/08_tree_breadth_first_search/004.png
# ../images/08_tree_breadth_first_search/005.png
# ../images/08_tree_breadth_first_search/006.png
# ../images/08_tree_breadth_first_search/007.png
# ../images/08_tree_breadth_first_search/008.png

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
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

        result.append(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


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
