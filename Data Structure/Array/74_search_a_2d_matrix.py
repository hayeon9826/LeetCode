class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col, row = len(maxtrix[0]), len(matrix)
        for i in col:
            if matrix[i][0] <= target and matrix[i][row] >= target:
                return target in matrix[i]
        return False