# 3718. Smallest Missing Multiple of K

# Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.

# A multiple of k is any positive integer divisible by k.

 

# Example 1:

# Input: nums = [8,2,3,4,6], k = 2

# Output: 10

# Explanation:

# The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.

# Example 2:

# Input: nums = [1,4,7,10,15], k = 5

# Output: 5

# Explanation:

# The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.

 
# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 100

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1 and nums[0] == k:
            return k*2

        data = set(nums)
        i = 1
        while (i <= len(nums)):
            if k * i not in data:
                return k * i
            i += 1
        
        return k*i


