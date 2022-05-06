# Find all Duplicate Numbers (easy)

# * MARK: - Problem statement
# We are given an unsorted array containing n numbers taken from the range 1 to n.
# The array has some numbers appearing twice, find all these duplicate numbers using constant space.

# * MARK: - Example 1
# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]

# * MARK: - Example 2
# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]

# * MARK: - Solution
# This problem follows the Cyclic Sort pattern and shares similarities with Find the Duplicate Number.
# Following a similar approach, we will place each number at its correct index.
# After that, we will iterate through the array to find all numbers that are not at the correct indices.
# All these numbers are duplicates.

def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    duplicateNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers

# * MARK: - Time Complexity
# The time complexity of the above algorithm is O(n)

# * MARK: - Space Complexity
# Ignoring the space required for storing the duplicates, the algorithm runs in constant space O(1)
