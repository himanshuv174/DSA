# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:     #if the length is 0 then return 0
            return 0

        max_length = 1   #taking the default length as 1
        n = set(nums)    #taking an unsorted set, so that we can check the element in the set directly

        for i in n:
            if i-1 not in n:      # Checking the previous element in the series is present or not 
                l = 1             #if not present then put length 1
                while i+l in n:   #checking if the next element in the series are present in the set or not
                    l += 1        #if it is present the add 1 in l
                    max_length = max(max_length,l)    # Checking the max length and assigning it

        return max_length