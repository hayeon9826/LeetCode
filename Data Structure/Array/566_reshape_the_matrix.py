class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = sum(mat, [])
        answer = []
        
        if len(flatten) != r * c:
            return mat
        else:
            for i in range(r):
                answer.append(flatten[:c])
                flatten = flatten[c:]
            return answer
# Runtime: 96 ms, faster than 32.60% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 15.2 MB, less than 8.88% of Python3 online submissions for Reshape the Matrix.