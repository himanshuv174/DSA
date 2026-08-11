# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

# You are given a 0-indexed array of integers nums.

# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

# Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

# Example 1:

# Input: nums = [1,2,3,2,5]
# Output: 6
# Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
# Example 2:

# Input: nums = [3,4,5,1,12,14,13]
# Output: 15
# Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

# Constraints:

# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        unique_elements = set()  #creating an empty set for unique elements of list
        seq_sum = nums[0]  # initializing the sequential sum with the first element

        # calculating the sequential sum first
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1 :
                seq_sum += nums[i]
            else:
                break   # because we only want sequence stating from 0 index
        
        # adding the elements of nums in set so that we can get the unique element
        for i in nums:
            unique_elements.add(i)
        
        #searching the Sequential sum is present in the unique element array or not
        # if it is the add 1 to it
        while(seq_sum in unique_elements):
            seq_sum += 1

        return seq_sum
        