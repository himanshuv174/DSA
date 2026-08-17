# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.

# 
# Solving using two pointer and Sliding window.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Solving using two pointer and Sliding window.

        l = 0
        r = 0
        mp = defaultdict(int)
        max_length = 0
        n = len(s)
        

        if n == 0:
            return 0

        while r < n:
            mp[s[r]] += 1

            while l < r and mp[s[r]] > 1:
                mp[s[l]] -= 1
                l += 1
            
            if mp[s[r]] <= 1:
                max_length = max(max_length,r-l+1)
                r += 1

        return max_length

##############################################################################################

#Adding the element in the dictionary or map and checking it already exist in it or not.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        l=0
        res=0
        for r in range(len(s)):
            if s[r] in mp:
                l=max(mp[s[r]]+1,l)
            mp[s[r]]=r
            res=max(r-l+1,res)
        return res