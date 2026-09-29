# 98. Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Example 1:

# Input: root = [2,1,3]
# Output: true

# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Solution 1

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))

#Solution 2

class Solution:
    def isValidBST(self, root: TreeNode | None, min_val = -2**31-1, max_val = 2**31) -> bool:
        if root is None:
            return True
        if root.val < min_val or root.val > max_val:
            return False
        a=self.isValidBST(root.left, min_val,root.val-1) and self.isValidBST(root.right, root.val+1,max_val)
        return a