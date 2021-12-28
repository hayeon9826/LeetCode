class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        answer = [0] * (len(triangle) + 1)
        # reverse the list
        for row in triangle[::-1]:
            for i in range(len(row)):
                answer[i] = row[i] + min(answer[i], answer[i + 1])
        return answer[0]
# Bottom up DP 
# https://leetcode.com/problems/triangle/discuss/38741/Python-Bottom-up-DP-O(n)%2BO(n)-solution-(-5-lines-)
def minimumTotal(self, triangle):
    f = [0] * (len(triangle) + 1)
    for row in triangle[::-1]:
        for i in xrange(len(row)):
            f[i] = row[i] + min(f[i], f[i + 1])
    return f[0]]