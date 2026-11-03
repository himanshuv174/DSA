# 462. Minimum Moves to Equal Array Elements II

# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

# Test cases are designed so that the answer will fit in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# Example 2:

# Input: nums = [1,10,2,9]
# Output: 16
 
# Constraints:

# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# O(N^2)
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        result = 10000000000000
        
        for i in nums:
            a = i
            c = 0
            for j in nums:
                b = abs(a - j)
                c += b
            
            result  = min(c,result)

        return result

# Approach O(N Log N)

# Sort the array in ascending order.
# Pick the middle element as the median. If the length is even, either middle element works.
# Loop through the array and calculate the absolute difference between each number and the median.
# Add all the differences to get the minimum number of moves.
# The median is the best target because it minimizes the total absolute difference.

# Time Complexity: O(n log n) where n is the length of the array, because sorting takes the most time and the later pass is only linear.
# Space Complexity: O(1) extra space if we sort in place (or O(log n) for the sort’s internal stack). We do not build any extra arrays.


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = nums[n // 2]
        result = 0

        for i in nums:
            result += abs(mid - i)
        
        return result


# Approach

# Sort nums in ascending order.
# Initialize two pointers:
# left = 0
# right = nums.length - 1
# While left < right:
# Add nums[right] - nums[left] to total_moves.
# Move left one step right.
# Move right one step left.
# Return total_moves.

# Complexity

# Time complexity: O(n log n) — sorting takes O(n log n) and the two-pointer traversal takes O(n).
# Space complexity: O(1) auxiliary space — excluding the sorting implementation's internal space.

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        total_moves = 0

        # Pair the smallest value with the largest, then move inward.
        while left < right:
            total_moves += nums[right] - nums[left]
            left += 1
            right -= 1

        return total_moves