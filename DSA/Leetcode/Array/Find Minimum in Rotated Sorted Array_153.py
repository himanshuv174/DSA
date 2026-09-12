# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.


# Step by Step Algorithm

# Initialize Pointers

# left = 0
# right = len(nums) - 1
# We define two pointers, left and right.
# left starts at the beginning of the array (0), and right starts at the last index (len(nums) - 1).
# The goal is to narrow down the range between left and right until we find the minimum element.
# Binary Search Loop

# while left < right:
# We enter a loop that continues as long as left is less than right.
# This loop performs a binary search to locate the minimum value in the rotated sorted array.
# Calculate Midpoint

# mid = (left + right) // 2
# We calculate the midpoint mid by taking the integer division of (left + right) / 2.
# mid represents the middle index of the current subarray defined by left and right.
# Compare Midpoint with Right Element

# if nums[mid] <= nums[right]:
#     right = mid
# If the element at mid is less than or equal to the element at right, this means the minimum element could be at mid or to its left (in the left half of the current subarray).
# We update right to mid, effectively discarding the right half of the array in the next iteration.
# Move Left Pointer

# else:
#     left = mid + 1
# If nums[mid] is greater than nums[right], this means the minimum element must be in the right half of the current subarray.
# We update left to mid + 1, moving it to the right half of the array for the next iteration.
# Return Minimum Element

# return nums[left]
# Once the loop exits (when left == right), both left and right will be pointing to the minimum element in the array.
# We return nums[left] as the minimum value.


class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = nums[-1]  #storing the last element of the list
        low = 0  # first element of array
        n = len(nums)
        high = n - 1 # last element of array

        while low < high:
            mid = low + (high - low) //2    

            if nums[mid] <= right:
                high = mid
            else:
                low = mid + 1
        return nums[low]
