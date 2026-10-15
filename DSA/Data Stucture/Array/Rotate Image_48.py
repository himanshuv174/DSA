# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# Intuition

# This problem asks us to rotate a square matrix 90 degrees clockwise. The elegant approach is to recognize that a 90° clockwise rotation can be achieved through two simple transformations: first transpose the matrix (swap rows with columns), then reverse each row. This avoids complex index calculations and uses straightforward operations.

# Approach

# We'll use a two-phase transformation strategy:

# Transpose operation: Swap elements across the main diagonal (matrix[i][j] ↔ matrix[j][i])
# Upper triangle iteration: Only swap elements above diagonal to avoid double-swapping
# Row reversal: Reverse each row to complete the 90° clockwise rotation
# In-place modification: Both operations modify the matrix directly without extra space
# Sequential application: Transpose converts rows to columns, reversal flips their order
# This approach leverages the mathematical property that rotation = transpose + reverse for clockwise 90°.

# Complexity

# Time complexity: O(n^2)
# Where n is the matrix dimension, for transposing (n²/2 swaps) and reversing (n²/2 operations).

# Space complexity: O(1)
# We perform all operations in-place using only constant extra space for swap variables.    

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for k in range(row):
            matrix[k].reverse()

#################################

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        edge_length = len(matrix)

        top = 0
        bottom = edge_length - 1

        while top < bottom:
            for col in range(edge_length):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        for row in range(edge_length):
            for col in range(row+1, edge_length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        return matrix


