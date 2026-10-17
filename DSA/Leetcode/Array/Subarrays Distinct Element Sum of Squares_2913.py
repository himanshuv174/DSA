# 2913. Subarrays Distinct Element Sum of Squares I

# You are given a 0-indexed integer array nums.

# The distinct count of a subarray of nums is defined as:

# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,2,1]
# Output: 15
# Explanation: Six possible subarrays are:
# [1]: 1 distinct value
# [2]: 1 distinct value
# [1]: 1 distinct value
# [1,2]: 2 distinct values
# [2,1]: 2 distinct values
# [1,2,1]: 2 distinct values
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
# Example 2:

# Input: nums = [1,1]
# Output: 3
# Explanation: Three possible subarrays are:
# [1]: 1 distinct value
# [1]: 1 distinct value
# [1,1]: 1 distinct value
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# Intuition

# All subarrays that start at the same index are prefixes of one another: [1], [1,2], [1,2,1]. Each one is the previous subarray plus one more element, so nothing needs rebuilding: fix the start, grow the end, and keep the values seen so far in a set. A repeated value doesn't change the set, so its size is always the distinct count.

# Example: nums = [1,2,1]

# start 0: {1} → 1, {1,2} → 4, {1,2} → 4
# start 1: {2} → 1, {2,1} → 4
# start 2: {1} → 1
# Total: 1 + 4 + 4 + 1 + 4 + 1 = 15 ✅

# Approach: Fix the Start, Grow the End | O(n²)

# For every start i, begin with an empty set.
# Move the end to the right and add each element to the set. Its size is the distinct count of the current subarray.
# Add the size squared to the total.
# Values are at most 100, so C++ and Java use a 101-bit bitset instead of a hash set.

# Complexity: O(n^2) time, O(n) space for the set (a fixed 101 bits in C++ and Java).

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            seen = set()
            for x in nums[i:]:  # grow the subarray to the right
                seen.add(x)  # a repeat doesn't change the size
                total += len(seen) ** 2
        return total