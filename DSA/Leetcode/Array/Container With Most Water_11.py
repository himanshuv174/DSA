# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 10^4


# Works but it is O(N^2), we need to optimize it
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_water_stored = 0

        while l<r:
            while l<r:
                min_height = min(height[l],height[r])
                distance = r-l
                stored_water = min_height * distance
                max_water_stored = max(max_water_stored,stored_water)
                l += 1
            
            l = 0
            r -= 1

        return max_water_stored


# Again this solution is also correct O(N^2) solution but we need to modify the logic to get less time complexity

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_water_stored = 0

        while l<=r:
            min_height = min(height[l],height[r])
            distance = r-l
            stored_water = min_height * distance
            max_water_stored = max(max_water_stored,stored_water)
            if l == r:
                l = -1
                r -= 1
            l += 1

        return max_water_stored


# O(n) solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_water_stored = 0

        while l<=r:
            min_height = min(height[l],height[r])
            distance = r-l
            stored_water = min_height * distance
            max_water_stored = max(max_water_stored,stored_water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water_stored