class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]




# 참고: https://leetcode.com/problems/rotate-image/discuss/842087/Easy-Python-from-scratch-(2-Steps)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """      
        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
          matrix[l], matrix[r] = matrix[r], matrix[l]
          l += 1
          r -= 1
        # transpose 
        for i in range(len(matrix)):
          for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]