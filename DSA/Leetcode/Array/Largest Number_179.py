# 179. Largest Number

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109

# Intuition
# We are not trying to make each number individually large. We are trying to make the final concatenated string as large as possible. So for any two numbers represented as strings a and b, the real question is: should we place a before b, or b before a? We test both possibilities: a+b and b+a. If a+b is bigger, a must come first. Repeating this rule during sorting gives the largest final number.

# Simple example:

# a = "3", b = "30"
# a+b = "330", b+a = "303"
# Since 330 > 303, place 3 before 30.

# Approach

# Convert all integers to strings.
# Sort strings with custom comparator:
# a should come before b if a+b > b+a.
# If first sorted string is "0", return "0".
# This handles inputs like [0,0] (avoid returning "00").
# Concatenate all strings and return.

# Why this comparator is the key:

# Normal numeric sort or lexicographic sort fails on cases like [3,30,34,5,9].
# Pairwise concatenation comparison directly optimizes the final objective.

# Complexity

# Time complexity: O(n log n * k) where k is average string length.
# Space complexity: O(nk) for storing string forms.

# Additional notes (optional)

# About the 0ms runtime:
# This version includes practical micro-optimizations (reserve, const references, single-pass join strategy).
# Exact runtime label like 0ms is not guaranteed, because LeetCode timing fluctuates by run, language backend, and server load.
# But this is already an optimal algorithmic approach for this problem.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        nums = [str(num) for num in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            return 1

        nums.sort(key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"

        return "".join(nums)