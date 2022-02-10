class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > target:
                    break
                if matrix[i][j] == target:
                    return True
        return False

# with binary search (Better)
# source: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/528263/Two-efficient-python-sol.-sharing.-90%2B-w-Diagram

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        
        for row in matrix:
			# range check
            if row[0] <= target <= row[-1]:
				# launch binary search on current possible row
                left, right = 0, w-1
                while left <= right:
                    mid = left + (right - left) // 2
                    mid_value = row[mid]
                    
                    if target > mid_value:
                        left = mid+1
                    elif target < mid_value:
                        right = mid-1
                    else:
                        return True
        return False