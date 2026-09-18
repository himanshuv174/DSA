# 190. Reverse Bits

# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:

# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
# Example 2:

# Input: n = 2147483644

# Output: 1073741822

# Explanation:

# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110
 

# Constraints:

# 0 <= n <= 231 - 2
# n is even.
 

# The Analogy: Reversing a Base-10 Number

# Imagine you have the number 1234 and you want to reverse it to 4321. You would follow these steps:

# Pop (n/10) the last digit: 4 (1234 becomes 123).
# Push (res + n%10) it onto your result: (Result was 0, now it's 4).
# To add the next digit (3), you first shift your result (res*10) (4 becomes 40) and then add the 3 to get 43.
# The Binary Simulation
# The bit reversal works exactly the same way, but instead of using base-10 (digits 0-9), it uses base-2 (bits 0-1).

# Extract the Bit (n & 1):
# This is like taking the "last digit." In binary, & 1 tells you if the number ends in a 0 or a 1.
# Shift the Result (res << 1):
# In base-10, you multiply by 10 to move digits over. In binary, you shift left by 1 to move bits over. This makes the "ones" place empty so you can drop a new bit into it.
# Combine (res | bit):
# You put the bit you just extracted into that empty space you just created in the result.
# Discard the Used Bit (n >>= 1):
# You shift the original number to the right, effectively throwing away the "last digit" so you can look at the next one in the next loop.
# Simulation
# bit_reversal.webp

# Approach

# Initialize a variable res to 0.
# Run a loop 32 times (since it's a 32-bit integer).
# In each iteration:
# Left-shift res by 1 (res <<= 1).
# Extract the last bit of n using the bitwise AND operator (n & 1) and add it to res.
# Right-shift n by 1 (n >>= 1).
# After the loop, res will contain the reversed bits.
# Note on Signed Integers: In C++, bitwise operations on signed integers (especially right shifts) can behave differently depending on the compiler (arithmetic vs. logical shift). For competitive programming, it is safer to treat the input as an unsigned int during the reversal process to ensure bits are shifted in as 0s.

# Complexity

# Time Complexity: O(1).
# While we use a loop, it always runs exactly 32 times regardless of the input value.
# Space Complexity: O(1).
# We only use a single variable res to store the result.


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res