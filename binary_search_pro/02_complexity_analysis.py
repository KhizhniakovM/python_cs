# Complexity Analysis
# Let's discuss how fast binary search is and how much memory it uses.

# * MARK: - Time complexity
# The essential property of binary search is to reduce the search area to, nearly, half of the original size.

# Suppose we have n` elements in our search array. On each iteration, we’re down to ​ 2n elements.
# The search area keeps halving from n to ​2​n, to 4​n, to 8n, and so on, until the area becomes of size 1
# (unless we found the target in some previous step).

# At this point, we either find the value or prove that it doesn’t exist in the search array.

# The total runtime is then a matter of how many steps(dividing n by 2 each time) we can take until n becomes 1.

# Here is a visual representation of our algorithm for the worst cases:

# When the target is the first element in the array:

# images/022.png

# There are 17 elements in our array. To find the number of times we have to do halving to ended up with only
# one item we use a logarithm function log_2 \space 17=4. Thus at most 4 iterations will be enough to reduce
# our array to one element. If n represents the total number of items, in log_2 \space n
# operations the answer will be found, which is asymptotically equivalent to O(log_2 \space n)

# * MARK: - Space complexity
# Binary search takes very little space and therefore has a space complexity of O(1).

# Let’s apply this knowledge to solve some of the frequently-asked binary search problems.
