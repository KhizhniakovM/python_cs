# Kth Smallest Number (easy)

# * MARK: - Problem statement
# Given an unsorted array of numbers, find Kth smallest number in it.

# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

# Note: For a detailed discussion about different approaches to solve this problem,
# take a look at Kth Smallest Number.

# * MARK: - Example 1
# Input: [1, 5, 12, 2, 11, 5], K = 3
# Output: 5
# Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

# * MARK: - Example 2
# Input: [1, 5, 12, 2, 11, 5], K = 4
# Output: 5
# Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

# * MARK: - Example 3
# Input: [5, 12, 11, -1, 12], K = 3
# Output: 11
# Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

# * MARK: - Solution
# This problem follows the Top ‘K’ Numbers pattern but has two differences:

# Here we need to find the Kth smallest number, whereas in Top ‘K’ Numbers
# we were dealing with ‘K’ largest numbers.
# In this problem, we need to find only one number (Kth smallest) compared
# to finding all ‘K’ largest numbers.
# We can follow the same approach as discussed in the ‘Top K Elements’ problem.
# To handle the first difference mentioned above, we can use a max-heap instead
# of a min-heap. As we know, the root is the biggest element in the max heap.
# So, since we want to keep track of the ‘K’ smallest numbers, we can compare every
# number with the root while iterating through all numbers, and if it is smaller than
# the root, we’ll take the root out and insert the smaller number.

from heapq import *


def find_Kth_smallest_number(nums, k):
    maxHeap = []
    # put first k numbers in the max heap
    for i in range(k):
        heappush(maxHeap, -nums[i])

    # go through the remaining numbers of the array, if the number from the array is smaller than the
    # top(biggest) number of the heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    # the root of the heap has the Kth smallest number
    return -maxHeap[0]


def main():

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()


# * MARK: - Time Complexity
# As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK),
# which is asymptotically equal to O(N*logK)

# * MARK: - Space Complexity
# The space complexity will be O(K) because we need to store ‘K’ smallest numbers in the heap.

# * MARK: - An Alternate Approach
# Alternatively, we can use a Min Heap to find the Kth smallest number.
# We can insert all the numbers in the min-heap and then extract the top ‘K’ numbers
# from the heap to find the Kth smallest number. Initializing the min-heap with all numbers will take O(N)
# and extracting ‘K’ numbers will take O(KlogN). Overall, the time complexity of this algorithm
# will be O(N+KlogN) and the space complexity will be O(N)
