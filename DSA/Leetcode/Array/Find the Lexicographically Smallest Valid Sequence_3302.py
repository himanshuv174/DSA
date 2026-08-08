# 3302. Find the Lexicographically Smallest Valid Sequence

# You are given two strings word1 and word2.

# A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

# A sequence of indices seq is called valid if:

# The indices are sorted in ascending order.
# Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
# Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.

# Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

 

# Example 1:

# Input: word1 = "vbcca", word2 = "abc"

# Output: [0,1,2]

# Explanation:

# The lexicographically smallest valid sequence of indices is [0, 1, 2]:

# Change word1[0] to 'a'.
# word1[1] is already 'b'.
# word1[2] is already 'c'.
# Example 2:

# Input: word1 = "bacdc", word2 = "abc"

# Output: [1,2,4]

# Explanation:

# The lexicographically smallest valid sequence of indices is [1, 2, 4]:

# word1[1] is already 'a'.
# Change word1[2] to 'b'.
# word1[4] is already 'c'.
# Example 3:

# Input: word1 = "aaaaaa", word2 = "aaabc"

# Output: []

# Explanation:

# There is no valid sequence of indices.

# Example 4:

# Input: word1 = "abc", word2 = "ab"

# Output: [0,1]

 

# Constraints:

# 1 <= word2.length < word1.length <= 3 * 105
# word1 and word2 consist only of lowercase English letters.


# Approach
# I use two passes.

# In the first pass, I move from right to left.

# I keep a pointer j at the last character of word2.

# Whenever word1[i] == word2[j], I store i in last[j] and move j left.

# This builds a valid rightmost matching arrangement of word2.

# The important meaning of last[j] is:

# last[j] is the position used for word2[j] when I greedily match the suffix word2[j ...] from the right.

# Then I make a second pass from left to right.

# I keep j as the next character of word2 that I need to match.

# If word1[i] == word2[j], I take index i.

# If they are different, I can use the mismatch only if:

# I have not used the mismatch yet.
# Either this is the last character of word2, or i < last[j + 1].
# The second condition is important.

# If i < last[j + 1], then after using i as the mismatching character, I still have a position at last[j + 1] available for the next character of word2, and the rest of the suffix can continue to be matched.

# I never need to reconsider an earlier choice. Once I take an index, taking a later index at the same position would only make the answer lexicographically larger.

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        ans = []
        can_skip = True
        j = 0

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif can_skip and (j == m - 1 or i < last[j + 1]):
                can_skip = False
                ans.append(i)
                j += 1

        if j == m:
            return ans

        return []