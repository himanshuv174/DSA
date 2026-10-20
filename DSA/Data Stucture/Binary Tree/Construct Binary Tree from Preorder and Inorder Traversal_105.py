# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


# Approach

# I'll show you 2 ways to solve question.

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Solution 1

# There is a hint in preorder array, because the first number(= 3) is definitely root node.

# ⭐️ Points

# Where is 3 in inorder array?
# We can find 3 at index 1 in inorder array, that means left side of 3 in inorder array is all left nodes of 3 in the tree, because inorder traversal is like left, root and right. We ususally find left nodes before we find root node.

# I believe now you can guess. All right numbers of 3 in inorder array should be all right nodes.

# inorder = [9,3,15,20,7]

# left nodes: 9
# root: 3
# right nodes: 15,20,7
# Let's see how it works.

# Now, let's say we created node 3 from preorder and inorder array(execute popleft 3 and find index from inorder, then create node 3) and call the same function recursively.

# In the solution code below, everytime we separate left side and right side in inorder array.

# root.left = build(preorder, inorder[:idx])
# root.right = build(preorder, inorder[idx+1:])
# Execute

# root.left = build(preorder, inorder[:idx])
# idx: 1
# preorder = [9,20,15,7] (= After executing popleft 3)
# inorder = [9]

# tree
#  3
# The next preorder number is 9, so create a new node with 9.

# preorder = [20,15,7] (= After executing popleft 9)
# inorder = [9]

# tree
#  3
# /
# 9
# Now Let's create left and right side of 9. First of all execute

# root.left = build(preorder, inorder[:idx])
# idx: 0
# preorder = [20,15,7]
# inorder = []

# tree
#   3
#  /
# 9
# Now inorder array is empty, so nothing will happen. Let's create right side of 9. Execute

# root.right = build(preorder, inorder[idx+1:])
# idx: 0
# preorder = [20,15,7]
# inorder = []

# tree
#   3
#  /
# 9
# Nothing will happen. We finish creating left side of 3. Let's create right side of 3.

# preorder = [20,15,7] (= After executing popleft 3 and 9 for left side)
# inorder = [9,3,15,20,7]

# tree
#   3
#  /
# 9
# Execute

# root.right = build(preorder, inorder[idx+1:])
# idx: 1
# preorder = [20,15,7]
# inorder = [15,20,7]

# tree
#   3
#  /
# 9
# The right side of 3 is 20, so popleft 20 from preorder array then create a new node with 20.

# Where is 20 in inorder array?
# We can find 20 at index 1 in inorder array, that means 15 is left node of 20 and 7 is right node of 20, because inorder traversal is like left, root and right. In this case, 20 is root node of subtree(15, 20 and 7).

# preorder = [15,7] (= After executing popleft 20)
# inorder = [15,20,7]

# tree
#   3
#  / \
# 9  20
# Let's create left side of 20. Execute

# root.left = build(preorder, inorder[:idx])
# idx: 1
# preorder = [15,7]
# inorder = [15]

# tree
#   3
#  / \
# 9  20
# Create a new node with popleft 15.

# preorder = [7](= After executing popleft 15)
# inorder = [15]

# tree
#     3
#    / \
#   9  20
#      /
#     15
# Let's create left and right of 15. Execute

# root.left = build(preorder, inorder[:idx])
# root.right = build(preorder, inorder[idx+1:])
# But nothing will happen because inorder array will be empty. Let me skip the explanation.

# Then let's create right side of 20.

# preorder = [7]
# inorder = [15,20,7]

# tree
#     3
#    / \
#   9  20
#      /
#     15
# Excecute

# root.right = build(preorder, inorder[idx+1:])
# idx: 1
# preorder = [7]
# inorder = [7]

# tree
#     3
#    / \
#   9  20
#      /
#     15
# Let's create a new node with popleft 7.

# preorder = []
# inorder = [7]

# tree
#     3
#    / \
#   9  20
#      / \
#     15  7
# Let's create left and right side of 7. Execute

# root.left = build(preorder, inorder[:idx])
# root.right = build(preorder, inorder[idx+1:])

# But nothing will happen because inorder array will be empty. Let me skip the explanation.


# Complexity
# Time complexity: O(n^2)
# Space complexity: O(n^2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx+1:])

                return root

        return build(preorder, inorder)
