# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Approach
# The most intuitive and elegant approach is to use recursion (Depth-First Search).

# Base Case: The simplest possible tree is an empty one. If the root is null, there are no nodes, so its depth is 0. This is our stopping condition for the recursion.

# Recursive Step: If the root is not null, we can calculate its depth by considering the depths of its children.

# First, we recursively find the maximum depth of the left subtree by calling maxDepth(root.left).

# Next, we recursively find the maximum depth of the right subtree by calling maxDepth(root.right).

# The total depth of the current tree is 1 (for the current node) plus the maximum of the depths of its left and right children.

# Return Value: The function returns this calculated depth. The recursion unwinds, with each level adding 1 to the count until the initial call returns the final maximum depth of the entire tree.

# Complexity

# Time complexity: O(n)
# We visit each node of the tree exactly once. Therefore, the time complexity is linear with respect to the number of nodes, n.

# Space complexity: O(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)