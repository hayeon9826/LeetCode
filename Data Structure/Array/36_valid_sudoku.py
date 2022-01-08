class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow():
            for i in range(len(board)):
                flatten = [i for i in board[i] if i != '.']
                if len(set(flatten)) != len(flatten):
                    return False
            return True
        
        def checkCol():
            for col in zip(*board):
                flatten = [i for i in col if i != '.']
                if len(set(flatten)) != len(flatten):
                    return False
            return True

        
        def checkSquare():
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    flatten = [i for i in square if i != '.']
                    if len(set(flatten)) != len(flatten):
                        return False
            return True
            
        return checkRow() and checkCol() and checkSquare()