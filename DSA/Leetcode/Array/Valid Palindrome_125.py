# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

        # Step-by-Step Breakdown

        # low = 0: Sets the left pointer to the first character of the string (index 0).

        # high = len(s) - 1: Sets the right pointer to the last character of the string (last index).

        # The loop continues as long as the left pointer is to the left of the right pointer.

        # Once the pointers meet in the middle (or cross each other), all relevant character pairs have been verified.

        # s[low] == s[high]: Compares the character at the left pointer with the character at the right pointer.

        # If they match: low += 1 moves the left pointer one step right, and high -= 1 moves the right pointer one step left.

        # If they don't match: It enters the else block and immediately returns False. The string cannot be a palindrome, so no further checking is needed.

        # If the loop finishes without finding any mismatched characters, every opposite pair matched. The function concludes the string is a palindrome and returns True.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # How this works:

        # result = "": Starts with an empty string.
        # for c in s:: Looks at each character c in the string one by one.
        # if c.isalnum():: Checks if the character is a letter or number (ignoring spaces and punctuation).
        # result += c.lower(): Converts the character to lowercase and adds it to result.
        # s = result: Stores the cleaned string back into s.

        result = ""

        for c in s:
            if c.isalnum():
                result += c.lower()
        s = result

        low = 0 
        high = len(s) - 1

        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False 

        return True

