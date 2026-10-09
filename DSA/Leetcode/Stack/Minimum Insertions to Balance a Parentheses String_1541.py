# 1541. Minimum Insertions to Balance a Parentheses String

# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.

# Return the minimum number of insertions needed to make s balanced.

# Example 1:

# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
# Example 2:

# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
# Example 3:

# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 
# Constraints:

# 1 <= s.length <= 105
# s consists of '(' and ')' only.


#  Approach
# 🧩 One rule: every ( needs exactly two ) right after it → ( + ))

# We keep two counters and go left → right:

# 🔹 open → how many ( are waiting for their ))
# 🔹 ans → how many characters we must insert

# For every character:

# Char	What we do

# (	     open++ (one more bracket is waiting)
# )	     it must become a )) → do Step 1 and then Step 2

# Step 1 — make the )) (look at the next char)

# next char is also ) → already a pair → skip it with i++
# next char is not ) → only one ) → insert one ) → ans++

# Step 2 — find its ( (look at open)

# open > 0 → a ( is waiting → match it → open--
# open == 0 → nobody is waiting → insert a ( → ans++
# At the end: every ( still waiting needs its own )) → return ans + open * 2


class Solution:
    def minInsertions(self, s: str) -> int:
        open = ans = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1
            else:
                # Step 1: make a "))"
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                # Step 2: find its '('
                if open > 0:
                    open -= 1
                else:
                    ans += 1
            i += 1

        return ans + open * 2


# Algorithm

# Initialize an empty stack and an insertion counter ans = 0.
# Traverse the string from left to right.
# If the current character is (, push it onto the stack.
# If the current character is ):
# If the next character is also ), treat both characters as one closing pair and skip the next character.
# Otherwise, insert one ) to complete the closing pair and increase ans by one.
# If the stack is not empty, pop one opening parenthesis because the closing pair matches it.
# Otherwise, insert one ( before the closing pair and increase ans by one.
# After processing the string, every opening parenthesis still in the stack needs two closing parentheses. Add 2 * stack.size() to ans.
# Return ans.
# This approach avoids repeatedly searching the string for matching parentheses. Each character is processed at most once, but the stack requires additional space.

# Complexity

# Time Complexity: O(n)
# We traverse the string from left to right. Each character is processed at most once, so the total time complexity is O(n), where nnn is the length of the string.

# Space Complexity: O(n)
# In the worst case, the stack may contain every character when the string consists entirely of opening parentheses.
# This is O(n) auxiliary space, excluding the input string and the constant-sized return value.


class Solution:
    def minInsertions(self, s: str) -> int:
        st = []
        ans = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                st.append('(')
                i += 1
            else:
                # Ensure every closing pair contains two ')'.
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    ans += 1
                    i += 1

                # Match the closing pair with an opening parenthesis.
                if st:
                    st.pop()
                else:
                    ans += 1  # Insert a missing '('.

        # Each unmatched '(' needs two closing parentheses.
        ans += 2 * len(st)

        return ans

# Algorithm

# Initialize res = 0 and need = 0.
# Traverse every character in the string.
# If the current character is (:
# Increase need by 2.
# If need is odd, increment res and decrease need by 1. This inserts the missing closing parenthesis needed to complete the previous pair.
# If the current character is ):
# Decrease need by 1.
# If need becomes negative, increment res and set need = 1. We insert an opening parenthesis before the current closing parenthesis. The current character satisfies one of its two closing requirements, leaving one more required.
# After processing all characters, add need to res because those closing parentheses are still missing.
# Return res.
# Why does the greedy approach work?
# Each insertion handles a requirement that cannot be avoided:

# An odd need after an opening parenthesis means an extra ) is required to finish the previous pair before starting a new opening parenthesis.
# A negative need means a new ( must be inserted because no existing opening parenthesis can match the current closing parenthesis.
# Any positive need remaining at the end represents closing parentheses that must be inserted.
# The algorithm inserts only the characters required to fix these situations. It never needs to revisit earlier characters or store the string's matching structure.

# Because we process each character once and maintain only two integer variables, this approach achieves O(n) time and O(1) auxiliary space. The time complexity is optimal because every input character must be examined.


class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        need = 0

        for c in s:
            if c == '(':
                need += 2

                # Complete the previous closing pair if needed.
                if need % 2 == 1:
                    res += 1
                    need -= 1
            else:
                need -= 1

                # Insert an opening parenthesis for this ')'.
                if need < 0:
                    res += 1
                    need = 1

        # Insert all remaining required closing parentheses.
        return res + need


