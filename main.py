# * MARK: - Problem Statement
# Given an array of positive numbers and a positive number ‘S’
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0 if no such subarray exists.

# * MARK: - Example 1
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

# * MARK: - Example 2
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# * MARK: - Example 3
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

import math


def find_smallest_subarry_with_greater_sum(s: int, arr: list[int]):
    result = math.inf
    window_sum, window_start = 0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            result = min(result, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if result == math.inf:
        return 0

    return result


def main():
    print("Smallest subarray length: " +
          str(find_smallest_subarry_with_greater_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(find_smallest_subarry_with_greater_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(find_smallest_subarry_with_greater_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " +
          str(find_smallest_subarry_with_greater_sum(8, [])))


main()
