# 1927. Sum Game

# Alice and Bob take turns playing a game, with Alice starting first.

# You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

# Choose an index i where num[i] == '?'.
# Replace num[i] with any digit between '0' and '9'.
# The game ends when there are no more '?' characters in num.

# For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

# For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
# Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.

 

# Example 1:

# Input: num = "5023"
# Output: false
# Explanation: There are no moves to be made.
# The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
# Example 2:

# Input: num = "25??"
# Output: true
# Explanation: Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.
# Example 3:

# Input: num = "?3295???"
# Output: false
# Explanation: It can be proven that Bob will always win. One possible outcome is:
# - Alice replaces the first '?' with '9'. num = "93295???".
# - Bob replaces one of the '?' in the right half with '9'. num = "932959??".
# - Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
# - Bob replaces the last '?' in the right half with '7'. num = "93295927".
# Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.
 

# Constraints:

# 2 <= num.length <= 105
# num.length is even.
# num consists of only digits and '?'.

# Intuition

# The goal is to determine whether Bob can force the sum of the two halves to be equal.

# The fixed digits determine the current difference between the two halves.

# The character ? determine who gets the final move and how each side can change.

# When ? exist on both sides, Bob can cancel Alice's move by choosing the same digit on the other side, keeping the diff unchanged.

# When extra ? remain on one side, we only need to consider how much those remaining ? can change that side's sum.

# Approach

# For example, let's take:

# Here, the sum of the left side, right side are:
#     sumL=14, and sumR=5, respectively.

# The total number of ? is even:
#     Which means Bob makes the final move, so Bob can always counter Alice's move.

# If Alice places a digit x on one side, Bob can place the same digit on the other:
#     So, the difference (diff=sumL−sumR) does not change.

# If two ? remain on the same side, Bob can choose complementary digits:

# So after pairing as many ? as possible between the two halves:

#     If one ? remains, it is the final move.
#     Otherwise, the remaining ? form pairs on the same side.


# Let's explore all possible cases:

# Case 1:

# If there are no ? left, so there's 0 possible moves:

# Hence, we simply compare the sums, and determine the winner based on the diff:

# Case 2:

# If there are odd number of ?, Alice always makes the final move.

# Alice controls the final digit, so Alice can choose a digit that leaves the diff>0.

# Therefore, Alice always win.

# Case 3:

# If there are an even number of ?, Bob always makes the final move:

# a.) Same Number of ? on both sides:

#     We determine the winner based ON the diff:

# b.) Different Number of  ? on both sides:

# Suppose there are more ? on the right.

#     We know that when ? exist on both sides, Bob can simply counter Alice's move on the opposite side, making the diff the same.
#     So we only need to consider the ? that cannot be paired across the two halves.

# To make the contribution of the remaining ? fixed, Bob answers Alice with the complementary digit 9−x:

#         Alice(x) + Bob(9−x) = 9
 
# So each extra pair contributes an additional 9 to the sum of the side with more ?.

# Basically, we need to find the extra pair left on a single side:
#     Consider the number of ? on left, and right as:
#         qL, and qR, respectively.
#     The net difference is:
#         diff Q = qR-qL
 
#     Dividing by 2 gives the number of remaining pairs:
#         pairs= diff Q / 2

 
#     Then, we check if the contribution of those pairs is enough to balance the current difference:
#             diff = 9⋅diff Q / 2
#                  or
#             2 * diff = 9⋅diff Q
 
#     If  2⋅diff = 9⋅diff Q are equal:

#         Bob can balance the left and right sum and wins.
#         Otherwise, Alice wins.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        q = 0

        for i in range(n):
            if num[i] == '?':
                q += 1
            elif i < n // 2:
                diff += int(num[i])
            else:
                diff -= int(num[i])

        if q % 2:
            return True
        left = num[:n//2].count('?')
        right = q - left

        return diff != 9 * (right - left) // 2