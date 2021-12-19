class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq, fresh, row, col = deque(), deque(), len(grid), len(grid[0])
        min, rottenCnt = 0, 0 # min은 시간 count는 rotten 수
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    dq.append((i, j)) # 2 인 좌표를 dq에 넣고
                elif grid[i][j] == 1:
                    fresh.append((i, j))

        
        while dq:
            length = len(dq)
            for i in range(length):
                (x, y) = dq.popleft()
                for newX, newY in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1: # up, down, right, left 좌표가 1일 때 
                        rottenCnt += 1
                        print(rottenCnt)
                        grid[newX][newY] = 2 # 새로운 좌표를 2로 체크
                        dq.append((newX, newY)) # 해당 좌표를 dq에 추가하고 다시 테스팅
            if dq: # 만약 dq에 좌표가 있다면 카운트
                min = min + 1