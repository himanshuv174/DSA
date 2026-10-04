# 678. Valid Parenthesis String

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true
# Example 3:

# Input: s = "(*))"
# Output: true
# Example 4:

# Input: s = "("
# Output: false
 
# Constraints:

# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.


# Approach

# Start with low = 0 and high = 0.
# Traverse the string character by character:
# ( → low++, high++
# ) → low--, high--
# * → low--, high++
# If high < 0, return false.
# Even in the best case, there are too many ) characters.
# If low < 0, set it back to 0.
# A * can also be treated as empty, so the minimum balance cannot be negative.
# After the loop, return low == 0.
# This means there is at least one valid way to balance all parentheses.

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for i in s:
            if i == '(':
                low += 1
                high += 1
            
            if i == ')':
                low -= 1
                high -= 1

            if i == '*':
                low -= 1
                high += 1
            
            if high < 0:
                return False

            if low < 0:
                low = 0
        
        return low == 0

        