# 230. Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Intuition
# The intuition behind this solution is to perform an inorder traversal of the binary search tree to collect values in ascending order. Once the values are collected, the kth smallest value can be easily retrieved.

# Approach 01

# Using Vector.
# Perform an inorder traversal, which involves visiting the left subtree, then the root, and finally the right subtree.
# Store the values from the left side in a vector, resulting in an increasing order of values.
# Return the (k-1)th element from the vector as it corresponds to the kth smallest element in the binary search tree. The vector is in increasing order, making it easy to access the kth smallest element directly.
# Complexity
# Time complexity: The time complexity of this solution is O(n), where n is the number of nodes in the binary search tree. The inorder traversal visits each node once.
# Space complexity: The space complexity is O(n), as the solution uses a list to store the values collected during traversal. In the worst case, when the binary search tree is skewed, the list could contain all node values.

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        data = []
        self.support(root, data)
        return data[k-1]

    def support(self,node,data):
        if not node:
            return   
        self.support(node.left, data)
        data.append(node.val)
        self.support(node.right, data)


# Approach 02

# Using Recursion.
# Perform an in-order traversal of the binary search tree.
# In each recursive call, check if the kth smallest element has been found.
# If found, update the result and stop further traversal.
# Return the result after the traversal.
# Complexity
# Time complexity: The time complexity of this solution is O(n), where n is the number of nodes in the binary search tree. The inorder traversal visits each node once.
# Space complexity: The space complexity is O(h), where h is the height of the binary search tree. The space complexity is determined by the recursion stack.

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count = 0
        self.final = 0
        self.support(root, k)
        return self.final

    def support(self,node,k):
        if not node or self.count >= k:
            return   
        self.support(node.left, k)
        self.count += 1
        if self.count == k:
            self.final = node.val
            return
        
        self.support(node.right, k)
        