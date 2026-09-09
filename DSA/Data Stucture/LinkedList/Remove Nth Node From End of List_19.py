
# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Approach
# Initialize Pointers: Both ptr (fast) and temp (slow) start at the head.
# Create the Gap: Move the ptr forward times.
# Advance Together: Move both ptr and temp forward one step at a time until ptr reaches the last node (ptr.next == null).
# Edge Case - Removing Head: If after creating the gap, ptr is already null, it means we need to remove the first node of the list. We return head.next.
# Delete Node: Change the next pointer of the temp node to skip the target node: temp.next = temp.next.next.
# ⚙️ Dry Run Analogy
# Imagine two people walking. Person A starts walking and gets a head start of meters. Then Person B starts walking at the same speed. When Person A hits the wall at the end of the hallway, Person B is exactly meters away from that wall.

# 📈 Complexity
# Time complexity: O(L) — Where is the length of the linked list. We traverse the list exactly once.
# Space complexity: O(1) — We only use two additional pointers regardless of the list size.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = temp = head
        for _ in range(n):
            ptr = ptr.next
            
        if not ptr:
            return head.next
            
        while ptr.next:
            ptr = ptr.next
            temp = temp.next
            
        temp.next = temp.next.next
        return head
