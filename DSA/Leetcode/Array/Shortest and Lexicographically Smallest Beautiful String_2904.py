# 2904. Shortest and Lexicographically Smallest Beautiful String

# You are given a binary string s and a positive integer k.

# A substring of s is beautiful if the number of 1's in it is exactly k.

# Let len be the length of the shortest beautiful substring.

# Return the lexicographically smallest beautiful substring of string s with length equal to len. If s doesn't contain a beautiful substring, return an empty string.

# A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.

# For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.
 

# Example 1:

# Input: s = "100011001", k = 3
# Output: "11001"
# Explanation: There are 7 beautiful substrings in this example:
# 1. The substring "100011001".
# 2. The substring "100011001".
# 3. The substring "100011001".
# 4. The substring "100011001".
# 5. The substring "100011001".
# 6. The substring "100011001".
# 7. The substring "100011001".
# The length of the shortest beautiful substring is 5.
# The lexicographically smallest beautiful substring with length 5 is the substring "11001".
# Example 2:

# Input: s = "1011", k = 2
# Output: "11"
# Explanation: There are 3 beautiful substrings in this example:
# 1. The substring "1011".
# 2. The substring "1011".
# 3. The substring "1011".
# The length of the shortest beautiful substring is 2.
# The lexicographically smallest beautiful substring with length 2 is the substring "11".
# Example 3:

# Input: s = "000", k = 1
# Output: ""
# Explanation: There are no beautiful substrings in this example.
 

# Constraints:

# 1 <= s.length <= 100
# 1 <= k <= s.length



# Approach 2 — Sliding Window
# We can do better by observing something important: we need a substring with exactly k ones. Instead of generating every substring, we maintain a window [left ... right] and track how many ones are inside it. Once the window contains exactly k ones, we shrink it as much as possible.

# Expand right
#       ↓
# Count ones
#       ↓
# If we have k ones
#       ↓
# Shrink from left while possible
#       ↓
# Now we have the shortest window
#       ↓
# Compare with answer
# This avoids checking every possible substring.

# Why Can We Shrink the Window?
# Suppose s = "100011001", k = 3, and our current window contains exactly 3 ones. If the leftmost characters are zeros:

# 00011001
# ^
# 0
# removing those zeros does not change the number of ones, so we should remove them:

# "0011001"
#    ↓ remove leading zeros
# "11001"
# Both contain exactly 3 ones, but length("11001") < length("0011001"). So whenever we have exactly k ones, we should strip unnecessary leading zeros — this gives the shortest possible substring for the current right boundary.

# Sliding Window Example
# Take s = "100011001", k = 3. The window 100011001 contains three ones, so it's beautiful. Now remove unnecessary zeros from the left:

# 100011001
#    ↓
# 00011001
#    ↓
# 0011001
#    ↓
# 011001
#    ↓
# 11001
# We stop at 11001, because removing the next character would remove a 1. So "11001" is the shortest beautiful substring ending at this position. We repeat this for every window and keep the best answer.


# Complexity
# The left pointer only moves forward, and so does right. Each character is processed only a constant number of times, so maintaining the window itself takes:

# O(n)

# However, we build a substring (s.substr(...) / s.substring(...) / s[left:right+1]) every time we find a candidate, which can take O(n). There can be O(n) candidate windows, so the strict complexity of this exact implementation becomes:

# O(n^2)

# With n <= 100, this is still easily fast enough.

# Time	
# O(n^2) worst case for this exact implementation	

# Space
# O(n) for storing the answer/current substring

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        count_one = 0
        ans = ""
        l = 0
        r = 0
        n = len(s)
        while r < n:
            if s[r] == '1':
                count_one += 1
            # Too many ones -> move left
            while count_one > k:
                if s[l] == '1':
                    count_one -= 1

                l += 1


            # We have exactly k ones
            if count_one == k:

                 # Remove unnecessary leading zeros
                while l < r and s[l] == '0':
                    l +=1
                
                cur = s[l:r + 1]

                if ans == "" or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                   ans = cur

            r += 1
            
        return ans
                

            
