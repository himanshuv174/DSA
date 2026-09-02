# 3875. Construct Uniform Parity Array I

# You are given an array nums1 of n distinct integers.

# You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

# For each index i, you must choose exactly one of the following (in any order):

# nums2[i] = nums1[i]
# nums2[i] = nums1[i] - nums1[j], for an index j != i
# Return true if it is possible to construct such an array, otherwise, return false.

 

# Example 1:

# Input: nums1 = [2,3]

# Output: true

# Explanation:

# Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
# Choose nums2[1] = nums1[1] = 3.
# nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.
# Example 2:

# Input: nums1 = [4,6]

# Output: true

# Explanation:​​​​​​​

# Choose nums2[0] = nums1[0] = 4.
# Choose nums2[1] = nums1[1] = 6.
# nums2 = [4, 6], and all elements are even. Thus, the answer is true.
 

# Constraints:

# 1 <= n == nums1.length <= 100
# 1 <= nums1[i] <= 100
# nums1 consists of distinct integers.


# Intuition

# We only need to consider the parity of each element.

# Equal parities produce an even difference.
# Different parities produce an odd difference:
#     even−even =even
#     odd−odd =even
#     even−odd =odd 
#     odd−even =odd

# Essentitally, we can construct an all-odd array whenever the input contains at least one odd number.

#     -We keep every odd element unchanged.
#     -Choose any odd number as a reference, and we subtract it from every even element.
#     -Each difference becomes odd because different parities produce an odd difference:
#     -even−odd=odd

 
# An all-even array cannot be constructed when odd elements are present, because subtracting an even value from an odd element preserves its odd parity.

# Approach

# We have two cases:

# Case 1: All elements have the same parity.
# If all elements are odd or all are even, we keep every element unchanged.

#     -The resulting nums2 array already has uniform parity.


# Case 2: The array contains both odd and even elements.
# We choose any odd element as a reference.

#     -If nums1[i] is odd, we keep the element unchanged.
#     -Otherwise, we subtract the reference from nums[i].
#         This makes every element in nums2.odd:


# In either case, we can construct nums2 such that all elements have the same parity.

# Therefore, we simply return true.

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True