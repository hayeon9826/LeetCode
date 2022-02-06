class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        answer = [1]
        
        def dfs(prev):
            arr = []
            for i in range(len(prev)+1):
                if i > 0 and i < len(prev):
                    arr.append(prev[i] + prev[i-1])
                else:
                    arr.append(1)
            return arr
        
        while rowIndex > 0:
            answer = dfs(answer)
            rowIndex = rowIndex - 1
            
        return answer

# for 문 만을 이용한 반복문:
# source: https://leetcode.com/problems/pascals-triangle-ii/discuss/1742190/Python-3-(40ms)-or-Iterative-Easy-Approach
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        for i in range(rowIndex+1):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res[rowIndex]


# faster code
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer=[1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                answer[i-j]+=answer[i-j-1]
        return answer