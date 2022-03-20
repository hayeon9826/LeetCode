# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(R):
    # write your code in Python 3.6
    visited = {}
    count_arr = []
    dfs(0, 0, 0, R, visited, count_arr)
    print(count_arr)

    return len(set(count_arr))


def dfs(x, y, direction, R, visited, count_arr):
    a = len(R)
    b = len(R[0])

    if x == a or x == -1 or y == b or y == -1:
        if x == a:
            dfs(x - 1, y, 2, R, visited, count_arr)
        elif x == -1:
            dfs(x + 1, y, 0, R, visited, count_arr)
        elif y == b:
            dfs(x, y - 1, 1, R, visited, count_arr)
        elif y == -1:
            dfs(x, y + 1, 3, R, visited, count_arr)
        return

    
    key = str(x) + "_" + str(x) + "_" + str(direction)

    if (key in visited) and (visited[key] > 5):
        return

    visited[key] = visited[key] + 1 if key in visited else 1

    if R[x][y] != "X":
        k = str(x) + "_" + str(y)
        count_arr.append(k)

        if direction == 0:
            dfs(x, y+1, 0, R, visited, count_arr)
        elif direction == 1:
            dfs(x+1, y, 1, R, visited, count_arr)
        elif direction == 2:
            dfs(x, y-1, 2, R, visited, count_arr)
        elif direction == 3:
            dfs(x-1, y, 3, R, visited, count_arr)
    else:
        if direction == 0:
            dfs(x, y-1, 1, R, visited, count_arr)
        elif direction == 1:
            dfs(x-1, y, 2, R, visited, count_arr)
        elif direction == 2:
            dfs(x, y+1, 3, R, visited, count_arr)
        elif direction == 3:
            dfs(x+1, y, 0, R, visited, count_arr)
    return










