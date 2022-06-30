# Single Element in a Sorted Array
# Let's try to use a sorted array with duplicates as the input array.

# Difficulty Level: Medium

# * MARK: - Problem statement
# Suppose we are given a sorted array that only consists of integers, where every element appears
# twice, except for one element which appears once. Find the element that appears only once.

# ? Constraints:
# 1  <= nums.length  <= 10 ^ 3
# 0  <= nums[i]  <= 10 ^ 3

# ? Example 1:
# Input: [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2

# ? Example 2:
# Input: [3, 3, 7, 7, 10, 11, 11]
# Output: 10

# ? Example 3:
# Input: [1, 1, 2, 2, 3]
# Output: 3

# ? Example 4:
# Input: [1]
# Output: 1

# * MARK: - Intuition
# Since the array contains one element that appears only once, and all of the other elements appear
# twice, it must always have an odd number of elements.

# * MARK: - Algorithm
# - Set the left boundary to 0, and the right boundary to the size of nums
# - While left + 1 < right
#   - Take mid = (left + right) / 2 as a guess. Compare nums[mid] with nums[mid - 1]
#      - If nums[mid] != nums[mid - 1] and (1 + mid == size of nums or nums[mid] != nums[mid + 1]),
#        the job will be done and we will return nums[mid]
#      - Else, if (mid is odd and nums[mid] == nums[mid - 1]), or (mid is even, and nums[mid] == nums[mid + 1]),
#        we will move the left boundary left = mid
#      - Otherwise, we will move the right boundary right = mid
# - Return nums[left]

def singleNonDuplicate(nums):
    # the initial value for left index is 0
    left = 0
    # the initial value for right index is the number of elements in the array
    right = len(nums)
    # left + 1 >= right will finish while loop
    while left + 1 < right:
        mid = (right + left) // 2

        if nums[mid] != nums[mid - 1] and (1 + mid == len(nums) or nums[mid] != nums[mid + 1]):
            # the element on the mid index is the answer
            return nums[mid]
        elif ((mid % 2) != 0 and nums[mid] == nums[mid - 1]) or ((mid % 2) == 0 and nums[mid] == nums[mid + 1]):
            # there is no sense to search in the left half of the array
            left = mid
        else:
            # there is no sense to search in the right half of the array
            right = mid
    # the element on the left index is the answer
    return nums[left]


def main():
    print("The single element is ---> " +
          str(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])))
    print("The single element is ---> " +
          str(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])))
    print("The single element is ---> " +
          str(singleNonDuplicate([1, 1, 2, 2, 3])))
    print("The single element is ---> " + str(singleNonDuplicate([1])))


main()

# * MARK: - Complexity analysis
# Time complexity: O(log n)
# Space complexity: O(1)
# O(1)
