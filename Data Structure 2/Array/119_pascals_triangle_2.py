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