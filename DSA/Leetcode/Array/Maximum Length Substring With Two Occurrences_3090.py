# 3090. Maximum Length Substring With Two Occurrences

# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        #this can be done by sliding window
        n = len(s)
        mp = defaultdict(int)    #declaring the map of int as value
        l = 0
        r = 0
        max_length = 0

        while r < n:
            mp[s[r]] += 1

            while (l < r) and (mp[s[r]] > 2) :
                mp[s[l]] -= 1
                l += 1
            
            if mp[s[r]] <= 2:
                max_length = max(max_length, r-l+1)
                r += 1

        return max_length