# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    x, y = len(A[0]), len(A)
    max_len = min(x, y)

    for max_count in range(max_len, 1, -1):
        for i in range(y - max_count + 1):
            for j in range(x - max_count + 1):
                if checkSquare(i, j, max_count, A):
                    return max_count

    return 1


def checkSquare(i, j, length, grid):
    add_arr = set()
    add_arr2 = set()
    # check sum of rows
    for x in range(length):
        sum = 0
        for y in range(length):
            sum += grid[i+x][j+y]
        add_arr.add(sum)
        if len(add_arr) > 1:
            return False
            
    # check sum of cols
    for y in range(length):
        sum = 0
        for x in range(length):
            sum += grid[i+x][j+y]
        add_arr.add(sum)
        if len(add_arr) > 1:
            return False

    # check sum of right, left diagonals
    right_sum = 0
    left_sum = 0
    for x in range(length):
        right_sum += grid[i+x][j+x]
        left_sum += grid[i+x][j+length - 1 - x]
    add_arr.add(right_sum)
    add_arr2.add(left_sum)
    if len(add_arr) > 1 or len(add_arr2) > 1:
        return False

    return True

