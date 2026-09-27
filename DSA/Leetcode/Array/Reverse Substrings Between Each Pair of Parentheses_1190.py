# 1190. Reverse Substrings Between Each Pair of Parentheses

# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

# Example 1:

# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:

# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
# Example 3:

# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

# Constraints:

# 1 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It is guaranteed that all parentheses are balanced.


# Intuition

# We need to reverse the characters inside every pair of parentheses.

# A stack is useful here because parentheses are nested. Whenever we encounter (, we save the current string and start building a new string inside the parentheses.

# When we encounter ), we reverse the current string and append it back to the string stored before the corresponding (.

# Approach

# Use a stack to store the string built before each (.

# Maintain ans as the current string.

# For every character in s:

# If it is (:

# Push the current ans into the stack.
# Reset ans to an empty string.
# If it is ):

# Reverse the current ans.
# Pop the previous string from the stack.
# Append the reversed string to it.
# Otherwise:

# Add the character to ans.
# Finally, return ans.

# Algorithm

# Initialize an empty stack and an empty string ans.

# Traverse the string character by character.

# When ( is encountered:

# Push ans onto the stack.
# Reset ans.
# When ) is encountered:

# Reverse ans.
# Pop the previous string from the stack.
# Combine both strings.
# For normal characters, append them to ans.

# Return ans.

# Complexity Analysis

# Time Complexity: O(n²) in the worst case because string reversal and string concatenation can take O(n) time and may be performed multiple times.
# Space Complexity: O(n) because the stack and intermediate strings can store up to O(n) characters.


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []  # Stack to hold intermediate strings
        ans = ""  # String to build the current result

        for ch in s:
            if ch == '(':
                # Push the current string to the stack & start a new one
                stack.append(ans)
                ans = ""

            elif ch == ')':
                # Reverse the current string
                ans = ans[::-1]

                # Concatenate with the string on top of the stack
                ans = stack.pop() + ans

            else:
                # Append regular characters to the current string
                ans += ch

        return ans
    