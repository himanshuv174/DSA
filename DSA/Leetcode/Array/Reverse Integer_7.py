# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            sign = -1 
        else:
            sign = 1 

        num = 0
        x = abs(x)   # this will store only the absolute value of the number (not the positive or negative sign)

        while x:                        #this will store the number in the reverse order
           digit  = x % 10
           num = num * 10 + digit
           x = x//10
           
        num = num * sign      #multiplying with the sign 

        if num < -(2 ** 31) or num > 2 ** 31 - 1:     # working on the edge case for the limit of integer
            return 0

        return num

        