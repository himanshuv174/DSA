# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

# Approach

# Use two pointers: start and end.

# Calculate mid.

# If nums[mid] == target, return the index directly.

# Determine which half is sorted:

# If nums[mid] > nums[end], left half is sorted.
# Else, right half is sorted.
# Check if the target lies inside the sorted half:

# If yes → move towards that side.
# Else → move towards the other side.
# Continue until start > end.

# If not found, return -1.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        n = len(nums)
        high = n - 1
        # nums = [4,5,6,7,0,1,2]

        while low <= high:
            # Calculate value for mid
            mid = low + (high - low) // 2

            if nums[mid] == target:  # If mid is equal to target
                return mid
            # Because it is left rotated array
            # Check if left part of aray is sorted
            if nums[mid] >= nums[low]:
                # Checks if the target falls within the sorted left part
                # that means the target is in between low and mid.
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1   # Move left
                else:
                    low = mid + 1 # Move right
            
            # Right part is sorted
            else:
                # Checks if the target falls within the sorted right part
                # that means the target is in between High and mid.
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1 # Move right
                else:
                    high = mid - 1   # Move left
        
        return -1