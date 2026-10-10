# 2333. Minimum Sum of Squared Difference

# You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

# The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

# You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

# Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

# Note: You are allowed to modify the array elements to become negative integers.

# Example 1:

# Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
# Output: 579
# Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
# The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.
# Example 2:

# Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# Output: 43
# Explanation: One way to obtain the minimum sum of square difference is: 
# - Increase nums1[0] once.
# - Increase nums2[2] once.
# The minimum of the sum of square difference will be: 
# (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
# Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 105
# 0 <= nums1[i], nums2[i] <= 105
# 0 <= k1, k2 <= 109

# 🪜 Approach

# 🧩 One idea: every +1 / -1 (on nums1 or nums2) shrinks one |difference| by exactly 1 → so k1 and k2 become one shared budget k = k1 + k2.

# 📐 Squares punish big numbers → spend the budget on the biggest differences first.

# Step by step

# Make the differences. For every position take x = |nums1[i] - nums2[i]|.
# Count them in buckets. d[x] = how many positions have difference x. Also remember the total sum and the biggest value max. (No sorting needed — a difference is at most 10⁵.)
# Merge the budgets. k = k1 + k2.
# Shortcut. If sum <= k, every difference can reach 0 → answer is 0.
# Shave from the top, level by level. Go from i = max down to 1 while k > 0:
# move = min(k, d[i]) → how many positions at level i we can lower
# they all go down one level: d[i] -= move, d[i-1] += move
# spend the budget: k -= move
# Add the squares. Answer = sum of i × i × d[i] for every level.

# ⏳ Complexity Analysis

# Time: O(n+M) — one pass over the arrays plus one sweep over the levels (M ≤ 10⁵ is the biggest difference).
# Space: O(M) — the bucket array d of size 100001.

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        d = [0] * 100001   # Creating a list of max length
        k = k1 + k2  #adding the both k values
        total = 0
        mx = 0

        # Step 1: count the differences
        for a, b in zip(nums1, nums2):
            x = abs(a - b)  #absolute difference
            d[x] += 1     #adding the 1 at the x index
            total += x
            mx = max(mx, x)

        # Enough budget -> every difference becomes 0
        if total <= k:
            return 0

        # Step 2: shave the biggest differences, level by level
        for i in range(mx, 0, -1):
            if k <= 0:
                break
            move = min(k, d[i])
            d[i] -= move    # removing count from that index
            d[i - 1] += move  # moving count to the previous index
            k -= move    #at last removing the moves

        # Step 3: add up the squares
        ans = 0
        for i in range(mx + 1):
            ans += i * i * d[i]

        return ans