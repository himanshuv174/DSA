# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product:int = 1   # product used when non zero value or more than 1 zero is there
        product_zero:int = 1  # Product used when only one zero is there
        zero_flag = 0   # creating the zero_flag for count of zeros in the string
        
        #product of the values when non zero value or more than 1 zero is there
        for i in nums:
            product = i * product

        #product of the values used when only one zero is there
        for i in nums:
            if i == 0:
                zero_flag += 1  #counting the number of zero
                continue 
            else:
                product_zero = i * product_zero

        for i in range(len(nums)):
            if (nums[i] == 0) and (zero_flag == 1):  #when there is only one zero in the nums
                nums[i] = product_zero
            elif (nums[i] == 0) and (zero_flag > 1):  #when there is more than one zero in the nums and for the condition where denominator is also zero
                nums[i] = product
            else :
                nums[i] = product//nums[i]  #all the non zero numbers and there is more tham 1 zero

        return nums