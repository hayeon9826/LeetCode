
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid[0]), len(grid)
        
        def dfs(i, j):
            if grid[i][j] and i < row and j < col:
                grid[i][j] = 0
                up = dfs(i, j - 1)
                down = dfs(i, j + 1)
                right = dfs(i + 1, j)
                left = dfs(i - 1, j)
                return 1 + up + down + right + left
            return 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)


# references:
# https://leetcode.com/problems/max-area-of-island/discuss/108541/easy-python
def maxAreaOfIsland(self, grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j]:
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
        return 0

    areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
    return max(areas) if areas else 0



def dfs(i,j,grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
        return 0
    
    grid[i][j] = 0
    
    up = dfs(i,j+1,grid)
    down = dfs(i,j-1,grid)
    left = dfs(i-1,j,grid)
    right = dfs(i+1,j,grid)
    
    return up + down + left + right + 1

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 1:
                    count = max(dfs(i,j,grid), count)
                    
        return count