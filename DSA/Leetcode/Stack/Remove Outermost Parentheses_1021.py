# 1021. Remove Outermost Parentheses

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.

# Dyck Path

# We can represent a valid parentheses string as a Dyck Path:

# Dyck Path is a series of up and down steps.

# “(” moves the path up by one level.
# “)” moves the path down by one level.
# The path will begin and end on the same level, and as the path moves from left to right it will rise and fall, never dipping below the height it began on.

# Primitive Parenthesis

# A primitive parentheses string corresponds to a primitive Dyck path:

# The VPS can therefore be decomposed into consecutive primitive factors, each separated by a return to level 0.


# As we observed, the outermost parentheses of each primitive decomposition, corresponds to the path steps that touches level 0:

# Thus, keeping only the parts of the path ≥level 1 corresponds to removing each outermost parentheses.

# Dyck Path Level Tracking
# Now, let's traverse the input string while tracking the current level.

# Starting at level=0.

# For “(”, the path moves up:

# Before moving up, if level>0, the current parenthesis is inside a primitive factor, so we append “(” to the result.
# Then, increase level by 1.

# For “)”, the path moves down:

# First, move down the level by  
# −
#  1, since we need to check the level reached after this move.
# If level>0, the path remains strictly above level 0, so we append “)” to the result.
# Finally, the result string contains the original VPS with the outermost parentheses of every primitive factor removed.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        level = 0
    
        for c in s:
            if c == '(':
                if level > 0:
                    res.append(c)
                level += 1
            else:
                level -= 1
                if level > 0:
                    res.append(c)

        return "".join(res)