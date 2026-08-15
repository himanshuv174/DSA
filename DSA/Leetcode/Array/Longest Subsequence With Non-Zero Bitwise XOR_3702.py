# 3702. Longest Subsequence With Non-Zero Bitwise XOR

# You are given an integer array nums.

# Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

 

# Example 1:

# Input: nums = [1,2,3]

# Output: 2

# Explanation:

# One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

# Example 2:

# Input: nums = [2,3,4]

# Output: 3

# Explanation:

# The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        x = 0
        y = False
        for i in nums:
            x ^= i
            if i != 0:   # at least one element should be non zero
                y = True

        if x :
          return n 

        if y:
            return n-1

        return 0