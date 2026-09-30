# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 
# Constraints:

# 1 <= n <= 45

# Intuition:
# To calculate the number of ways to climb the stairs, we can observe that when we are on the nth stair,
# we have two options:

# either we climbed one stair from the (n-1)th stair or
# we climbed two stairs from the (n-2)th stair.
# By leveraging this observation, we can break down the problem into smaller subproblems and apply the concept of the Fibonacci series.
# The base cases are when we are on the 1st stair (only one way to reach it) and the 2nd stair (two ways to reach it).
# By summing up the number of ways to reach the (n-1)th and (n-2)th stairs, we can compute the total number of ways to climb the stairs. 
# This allows us to solve the problem efficiently using various dynamic programming techniques such as recursion, memoization, tabulation, or space optimization.

# Approach 1: Recursion ❌ TLE ❌
# Explanation: The recursive solution uses the concept of Fibonacci numbers to solve the problem. 
# It calculates the number of ways to climb the stairs by recursively calling the climbStairs function for (n-1) and (n-2) steps. 
# However, this solution has exponential time complexity (O(2^n)) due to redundant calculations.

    
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)



# Approach 2: Space Optimization
# Explanation: The space-optimized solution further reduces the space complexity by using only two variables (prev and curr) instead of an entire DP table. 
# It initializes prev and curr to 1 since there is only one way to reach the base cases (0 and 1 steps). Then, in each iteration, it updates prev and curr by shifting their values. 
# curr becomes the sum of the previous two values, and prev stores the previous value of curr.



class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr