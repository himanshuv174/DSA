# 3517. Smallest Palindromic Rearrangement I

# You are given a palindromic string s.

# Return the lexicographically smallest palindromic permutation of s.

# Example 1:

# Input: s = "z"

# Output: "z"

# Explanation:

# A string of only one character is already the lexicographically smallest palindrome.

# Example 2:

# Input: s = "babab"

# Output: "abbba"

# Explanation:

# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

# Example 3:

# Input: s = "daccad"

# Output: "acddca"

# Explanation:

# Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        string = list(s)
        size = len(string)
        res3 = ""
        size1 = size//2
        if size % 2 != 0:
            n = (size+1)//2
            res3 = string[n-1]
        str1 = []
        str2 = []

        for i in range(size1):
            str1.append(string[i])
            str2.append(string[size-i-1])

        res1:str = sorted(str1)
        res2:str = sorted(str2, reverse=True)

        if res3:
            return "".join(res1) + res3 + "".join(res2)
        else:
            return "".join(res1) + "".join(res2)
        
        