# 3727. Maximum Alternating Sum of Squares

# You are given an integer array nums. You may rearrange the elements in any order.

# The alternating score of an array arr is defined as:

# score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
# Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

# Example 1:

# Input: nums = [1,2,3]

# Output: 12

# Explanation:

# A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

# The alternating score is calculated as:

# score = 22 - 12 + 32 = 4 - 1 + 9 = 12

# Example 2:

# Input: nums = [1,-1,2,-2,3,-3]

# Output: 16

# Explanation:

# A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

# The alternating score is calculated as:

# score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

# Constraints:

# 1 <= nums.length <= 105
# -4 * 104 <= nums[i] <= 4 * 104


# 🪜 Approach

# 🧩 One idea: squaring removes the sign — (-4)² = 16 = 4². So only the size of each number matters, not whether it is positive or negative.
# 📐 The score is + − + − + … : the places 0, 2, 4, … get plus, the places 1, 3, 5, … get minus. We can reorder freely, so we just decide which squares go to plus places and which to minus places.

# Step by step

# Square every number into an array a (use long).
# Sort a — smallest on the left, biggest on the right.
# Count the minus places: k = n / 2 (integer division — the plus places are the other n − k).
# Subtract the first k squares (the smallest ones) → ans -= a[i].
# Add all the other squares (the biggest ones) → ans += a[i].
# Return ans.

# 💡 Why the smallest go to minus?
# Every plus place adds a square and every minus place removes one. To get the biggest total we add the biggest numbers and remove the smallest ones.

# 💡 What if n is odd?
# Then there is one more plus place than minus places (n = 5 → 3 plus, 2 minus). k = n / 2 = 2 takes care of it, so the extra place goes to the biggest side.

# 🎬 Visualization

# ▶️ Left = nums, the squares, the sorted squares, the + − slots and ans. Right = the exact line of code running.
# ✏️ Example nums = [3,-1,2,-4,1] → 27.
# 🔍 The 2 main steps for nums = [3,-1,2,-4,1]

# 1️⃣ Step 1 — Square every number, then sort

# 👉 Squares are never negative, so the signs disappear. Then sort so the small ones are on the left and the big ones on the right.

# i = 0   3  → 3 × 3   = 9      a = [9, ?, ?, ?, ?]
# i = 1  -1  → -1 × -1 = 1      a = [9, 1, ?, ?, ?]
# i = 2   2  → 2 × 2   = 4      a = [9, 1, 4, ?, ?]
# i = 3  -4  → -4 × -4 = 16     a = [9, 1, 4, 16, ?]
# i = 4   1  → 1 × 1   = 1      a = [9, 1, 4, 16, 1]
# sort →  a = [1, 1, 4, 9, 16]
# Notice -1 and 1 both became 1 — the sign really does not matter.

# 2️⃣ Step 2 — Subtract the small half, add the big half

# 👉 k = 5 / 2 = 2 → subtract the first 2 squares, add the other 3.
# k = 5 / 2 = 2        ans = 0
# i = 0   ans -= a[0]   ans = 0 − 1   = −1      (minus half)
# i = 1   ans -= a[1]   ans = −1 − 1  = −2      (minus half)
# i = 2   ans += a[2]   ans = −2 + 4  = 2       (plus half)
# i = 3   ans += a[3]   ans = 2 + 9   = 11      (plus half)
# i = 4   ans += a[4]   ans = 11 + 16 = 27      (plus half)
# The red numbers 1, 1 are subtracted, the green numbers 4, 9, 16 are added.
# That is the arrangement [-4, -1, 3, 1, 2] → 16 − 1 + 9 − 1 + 4 = 27.

# 🏆 Final Result
# (9 + 16 + 4) − (1 + 1) = 29 − 2 = 27
# Answer = 27 ✅

# 📋 Quick Recap
# Part	What happens	Result
# Step 1	square + sort	a = [1, 1, 4, 9, 16]
# Step 2a	subtract first k = 2	ans = −2
# Step 2b	add the other 3	ans = 27

# ⚠️ Things to watch out for

# Use long. Each square is up to 1.6 × 10⁹ and there are up to 10⁵ of them, so the total reaches about 10¹⁴ — cast before multiplying: (long) nums[i] * nums[i].
# Subtract exactly k = n / 2 squares, not half rounded up. For odd n the plus side is the bigger side, so the middle value is added, not subtracted.

# ⏳ Complexity Analysis

# Time: O(nlogn) — squaring is O(n), sorting is O(n log n), the two loops are O(n).
# Space: O(n) — the array a of n squares.


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1 + 2: square every number, then sort (smallest on the left)
        b = []

        for x in nums:
            b.append(x * x)

        b = sorted(b)

        k = len(nums) // 2   # number of minus places

        # Step 3 + 4: add the big squares, subtract the k smallest ones
        return sum(b[k:]) - sum(b[:k])