class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 1. define original color, row count and column count
        old, row, col = image[sr][sc], len(image), len(image[0])

        # 2. define dfs function
        def dfs(i, j):
            # set [i, j] color as newColor
            image[i][j] = newColor
            # for  4-directional pixels
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # check the range of the position & color
                if 0 <= x < row and 0 <= y < col and image[x][y] == old:
                    # call dfs again
                    dfs(x, y)
        
        # 3. if original color is different from new color, call dfs
        if old != newColor:
            dfs(sr, sc)
        
        # 4. return flood filled list
        return image

#BFS
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image

# Source: https://leetcode.com/problems/flood-fill/discuss/187701/Python-nice-and-clean-DFS-and-BFS-solutions
        
#DFS
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            dfs(sr, sc)
        return image

# Source: https://leetcode.com/problems/flood-fill/discuss/187701/Python-nice-and-clean-DFS-and-BFS-solutions