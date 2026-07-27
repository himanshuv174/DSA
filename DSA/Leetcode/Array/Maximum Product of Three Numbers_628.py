# 628. Maximum Product of Three Numbers

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        flag_zero = 0
        
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        sorted_list = sorted(nums)

        #checking both the cases where number can be maximum
        # 1 All max positive numbers
        # 2 2 lower negative and one max positive
        case1 = sorted_list[len(nums) -1] * sorted_list[len(nums) -2] * sorted_list[len(nums) -3]
        case2 = sorted_list[0] * sorted_list[1] * sorted_list[len(nums) -1]
       
        return max(case1, case2)
