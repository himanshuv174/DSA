# 3536. Maximum Product of Two Digits

# You are given a positive integer n.

# Return the maximum product of any two digits in n.

# Note: You may use the same digit twice if it appears more than once in n.

 

# Example 1:

# Input: n = 31

# Output: 3

# Explanation:

# The digits of n are [3, 1].
# The possible products of any two digits are: 3 * 1 = 3.
# The maximum product is 3.
# Example 2:

# Input: n = 22

# Output: 4

# Explanation:

# The digits of n are [2, 2].
# The possible products of any two digits are: 2 * 2 = 4.
# The maximum product is 4.
# Example 3:

# Input: n = 124

# Output: 8

# Explanation:

# The digits of n are [1, 2, 4].
# The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
# The maximum product is 8.
 

# Constraints:

# 10 <= n <= 109

class Solution:
    def maxProduct(self, n: int) -> int:
        # first we will extract the digits of the number
        num: int = abs(n)  # Handles negative inputs safely
        digits = []
        
        # Handle single digit case explicitly or 0
        if num == 0:
            return 0

        # Extract digits correctly using floor division
        while num > 0:
            lastdigit = num % 10
            num = num // 10  # Fix: Use // instead of /
            digits.append(lastdigit)

        # Edge case: If the number has fewer than 2 digits
        if len(digits) < 2:
            return digits[0]

        # Fix: Use sorted() to return a new sorted list
        sorted_digits = sorted(digits)

        # Calculate max product of the top two digits
        result = sorted_digits[-1] * sorted_digits[-2]

        return result

