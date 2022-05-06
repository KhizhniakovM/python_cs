# Problem challenge 1
# Find the Corrupt Pair (easy)

# * MARK: - Problem statement
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
# The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
# one of the numbers got duplicated which also resulted in one number going missing.
# Find both these numbers.

# * MARK: - Example 1
# Input: [3, 1, 2, 5, 2]
# Output: [2, 4]
# Explanation: '2' is duplicated and '4' is missing.

# * MARK: - Example 2
# Input: [3, 1, 2, 3, 6, 4]
# Output: [3, 5]
# Explanation: '3' is duplicated and '5' is missing.

# * MARK: - Solution
# This problem follows the Cyclic Sort pattern and shares similarities with Find all Duplicate Numbers.
# Following a similar approach, we will place each number at its correct index.
# Once we are done with the cyclic sort, we will iterate through the array to find the number
# that is not at the correct index. Since only one number got corrupted,
# the number at the wrong index is the duplicated number and the index itself represents the missing number.

def find_corrupt_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

    return [-1, -1]

# * MARK: - Time Complexity
# The time complexity of the above algorithm is O(n)

# * MARK: - Space Complexity
# The algorithm runs in constant space O(1)
