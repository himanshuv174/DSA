# 2265. Count Nodes Equal to Average of Subtree

# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

# Note:

# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.
 

# Example 1:


# Input: root = [4,8,5,0,1,null,6]
# Output: 5
# Explanation: 
# For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
# For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
# For the node with value 0: The average of its subtree is 0 / 1 = 0.
# For the node with value 1: The average of its subtree is 1 / 1 = 1.
# For the node with value 6: The average of its subtree is 6 / 1 = 6.
# Example 2:


# Input: root = [1]
# Output: 1
# Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000


# Approach

# Step 1 : Traverse the Tree Using Postorder DFS
# We need the children's results before we can process the current node, so we recurse into the left and right subtrees first.

# Step 2 : Combine What the Children Return
# For every node:

# 1. Get {sum, count} from the left subtree.
# 2. Get {sum, count} from the right subtree.
# 3. Add the current node:

# subtreeSum = leftSum + rightSum + root->val;
# subtreeCount = leftCount + rightCount + 1;
# Step 3 : Check the Average at This Node
# subtreeSum / subtreeCount == root->val
# If yes, increment the answer.

# Step 4 : Pass the Result Up
# Return {curSum, curCount} to the parent, so it can be combined the same way one level up.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfSubtree(self, root):
        self.count = 0

        def trav(node):
            if node is None:
                return (0, 0)

            leftSum, leftCount = trav(node.left)
            rightSum, rightCount = trav(node.right)

            subtreeSum = leftSum + rightSum + node.val
            subtreeCount = leftCount + rightCount + 1

            if subtreeSum // subtreeCount == node.val:
                self.count += 1

            return (subtreeSum, subtreeCount)

        trav(root)
        return self.count
