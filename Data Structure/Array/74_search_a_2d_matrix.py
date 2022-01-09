class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][last] >= target:
                return target in matrix[i]
        return False


# binary search O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        row, col = len(matrix[0]), len(matrix)
        start, end = 0, row*col - 1
        while start < end:
            mid = (start + end)//2
            if matrix[mid//row][mid%row] < target:
                start = mid + 1
            else:
                end = mid
        return matrix[start//row][start%row] == target


# Source: https://leetcode.com/problems/search-a-2d-matrix/discuss/896821/Python-Simple-binary-search-explained
# What we have in this problem is matrix, which is sorted and what we use to find element in sorted structure? Correct, this is binary search. Imagine, that we have matrix

# 10 11 12 13
# 14 15 16 17
# 18 19 20 21

# Let us flatten this matrix, so now we have 10 11 12 13 14 15 16 17 18 19 20 21 and do binary search in this list. 
# However if you do it, we will have O(mn) complexity, so we will use virtual flatten: we do not do it for all matrix, but only for elements we need: 
# if we need element number i from our flattened list, it coresponds to element matrix[i//m][i%m] in our matrix.

# Complexity: time complexity is O(log mn), space complexity is O(1).

# [참고]
# //: 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
# %: 나누기 연산 후 몫이 아닌 나머지를 구함

# binary search with flattened list
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        flatten = [item for sublist in matrix for item in sublist]
        start, end = 0, len(flatten) - 1
        while start < end:
            mid = (start + end) // 2
            if flatten[mid] == target:
                return True
            elif flatten[mid] < target:
                start = mid + 1
            else:
                end = mid
        mid = (start + end) // 2
        return flatten[mid] == target