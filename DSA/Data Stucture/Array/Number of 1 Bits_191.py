# 191. Number of 1 Bits

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

# Constraints:

# 1 <= n <= 231 - 1

# Method 1

class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0

        bit = []
        sum = 0
        while n > 0:
            bit.append(n & 1)
            n >> 1

        for i in bit:
            sum = sum + i

        return sum

# Method 2

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0

        while n:
            sum += (n % 2) # taking the last bit as reminder and adding it
            n = n >> 1    # moving the 1 bit to the left

        return sum

# Method 3

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n:
            if n & 1:
                sum += 1
            n = n >> 1

        return sum

# Method 4

# Intuition

# Instead of checking every single bit of the number one by one, we can speed up the process by skipping directly to the bits that are actually set to 1

# Approach

# The solution uses Brian Kernighan’s Algorithm.The core trick is the bitwise operation n & (n - 1). When you subtract 1 from a number, it flips all the bits after the rightmost set bit (including the set bit itself). Performing a bitwise AND between n and n - 1 effectively clears the lowest set bit to 0.By looping and applying n &= (n - 1) until n becomes 0, the number of iterations will exactly match the number of set bits (1s) in the integer.

# Complexity

# Time complexity:
# [O(1)]
# The loop runs exactly (k) times, where (k) is the number of set bits (1s). In the absolute worst-case scenario (a 32-bit integer with all 1s), the loop runs at most 32 times. Since 32 is a fixed, constant upper bound that does not grow with the size of the input, the time complexity simplifies to [O(1)] constant time.

# Space complexity:
# [O(1)]
# The algorithm only uses a single auxiliary variable (count) to keep track of the set bits, utilizing a constant amount of memory regardless of the input.
 
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        
        while n:
            n = n & (n-1)
            sum += 1

        return sum


