# 856. Score of Parentheses

# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Example 1:

# Input: s = "()"
# Output: 1
# Example 2:

# Input: s = "(())"
# Output: 2
# Example 3:

# Input: s = "()()"
# Output: 2

# Constraints:

# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.

# Approach

# Start with score = 0 and depth = 0.
# Go through the string from left to right.
# ( → increase depth.
# ) → decrease depth.
# After seeing ), check whether the previous character was (.
# If yes, we found ().
# Add 2^depth to score.
# Return score.
# Here, 1 << depth is simply another way to calculate 2^depth.

# Complexity

# Time Complexity: O(n) where n is the length of the string, because I examine each character exactly once.
# Space Complexity: O(1) because I only use a handful of integer variables and never allocate any extra data structures.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += 1 << depth
        return score