# Maximum Sum Subarray of Size K (easy)

# * MARK: - Problem statement
# Given an array of positive numbers and a positive number ‘k,’
# find the maximum sum of any contiguous subarray of size ‘k’.

# * MARK: - Example 1
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# * MARK: - Example 2
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# * MARK: - Solution
# A basic brute force solution will be to calculate the sum of all ‘k’ sized subarrays of the given array
# to find the subarray with the highest sum. We can start from every index of the given array and add
# the next ‘k’ elements to find the subarray’s sum.
# Following is the visual representation of this algorithm for Example-1:

# images/01_sliding_window/003.png

# * MARK: - Brut-force solution
def brutforce_max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum

# The above algorithm’s time complexity will be O(N*K),
# where ‘N’ is the total number of elements in the given array. Is it possible to find a better algorithm than this?

# * MARK: - Better approach
# If you observe closely, you will realize that to calculate the sum of a contiguous subarray,
# we can utilize the sum of the previous subarray. For this, consider each subarray as a Sliding Window of size ‘k.’
# To calculate the sum of the next subarray, we need to slide the window ahead by one element.
# So to slide the window forward and calculate the sum of the new position of the sliding window, we need to do two things:

# 1. Subtract the element going out of the sliding window, i.e., subtract the first element of the window.
# 2. Add the new element getting included in the sliding window, i.e., the element coming right after the end of the window.
# This approach will save us from re-calculating the sum of the overlapping part of the sliding window.
# Here is what our algorithm will look like:


def max_sub_array_of_size_k(k: int, arr: list[int]) -> int:
    windowSum, windowStart, maxSum = 0, 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum

# * MARK: - Time Complexity
# The time complexity of the above algorithm will be O(N)

# * MARK: - Space Complexity
# The algorithm runs in constant space O(1)
