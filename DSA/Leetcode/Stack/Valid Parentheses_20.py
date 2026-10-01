# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Approach 1 — explicit checks
# The straightforward version. Check each bracket type with its own if.
# Create an empty stack
# Walk through every character:
# If it's (, [ or { → push it
# Otherwise it's a closing bracket:
# Stack empty? → return false (nothing to match)
# Pop the top and check it's the right partner
# Wrong type? → return false
# At the end, return stack.isEmpty()

class Solution:
    def isValid(self, s: s) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[' :
                stack.append(i)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if i == ')' and top != '(':
                    return False
                if i == '}' and top != '{':
                    return False
                if i == ']' and top != '[':
                    return False

        
        return not stack



# Approach 2 — HashMap lookup or Map Lookup
# Same idea, less repetition. Instead of three separate if checks, store the pairs in a map once.

# map:   ')' → '('      '}' → '{'      ']' → '['
# Build the map of closing → opening
# Create an empty stack
# Walk through every character:
# map.containsValue(c) → it's an opening bracket → push it
# map.containsKey(c) → it's a closing bracket:
# Stack empty? → return false
# Does map.get(c) equal stack.pop()? If not → return false
# At the end, return stack.isEmpty()

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack