# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:

# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Intuition

# We need to swap every two adjacent nodes. The simplest way to picture this is grabbing two nodes at a time (first and sec), swapping which one comes first, then reconnecting this swapped pair to whatever came before it and whatever comes after it.

# Approach

# Keep three pointers moving through the list:

# first and sec are the current pair being swapped.
# prev is the last node of the previous already-swapped pair (or NULL if we're at the start).
# For each pair:

# Save third, the node right after the pair, so we don't lose track of the rest of the list.
# Swap the pair by pointing sec -> next to first, and first -> next to third.
# Connect this swapped pair to what came before: if prev exists, point prev -> next to sec (the new front of this pair). If prev is NULL, this is the first pair, so sec becomes the new head.
# Move forward: prev becomes first (now the back of this pair), and first becomes third (start of the next pair). If third exists, sec becomes third -> next; otherwise there's no next pair, so sec is set to NULL to stop the loop.
# The loop keeps going as long as both first and sec are non-null, meaning a full pair is still available to swap. If only one node is left (sec is NULL), it's left untouched since it has no partner.

# Complexity

# Time complexity: O(n), since each node is visited a constant number of times.
# Space complexity: O(1), since only a fixed number of pointers are used.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        first = head
        sec = head.next
        prev = None

        while first is not None and sec is not None:
            third = sec.next
            sec.next = first
            first.next = third

            if prev is not None:
                prev.next = sec
            else:
                head = sec
            prev = first
            first = third
            if third is not None:
                sec = third.next
            else:
                sec = None
        return head

        