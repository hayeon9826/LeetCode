class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dq, row, col = deque(), len(mat), len(mat[0])
        
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dq.append((i, j)) # 0 인 좌표를 dq에 넣고
                else:
                    mat[i][j] = float("inf") # 0이 아닌 좌표는 infinite로 표기
        print(dq)
        while dq:
            (x, y) = dq.popleft()
            for newX, newY in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                z = mat[x][y] + 1 # 0 + 1
                
                if 0 <= newX < row and 0 <= newY < col and mat[newX][newY] > z: # up, down, right, left 좌표가 0이 아닐 때 
                    mat[newX][newY] = z # 새로운 좌표에 + 1 을 해준다. 한번만 (mat[newX][newY] > z 이므로)
                    dq.append((newX, newY)) # 해당 좌표 주변에 0 이 없으므로, 다시 dq에 넣고 돌린다?

        
        return mat

# REFERENCED:
# https://kkminseok.github.io/posts/leetcode_01_Matrix/
# BFS solution

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        dq = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0 :
                    dq.append((i,j))
                else : 
                    mat[i][j] = 987654321
        while dq : 
            x,y = dq.popleft()
            for k in range(4):
                newx,newy = x + dx[k] , y + dy[k]
                z = mat[x][y]+1 
                if 0 <= newx and newx < row and 0 <= newy and newy < col and mat[newx][newy] > z :
                    mat[newx][newy] = z
                    dq.append((newx,newy))
        return mat
    