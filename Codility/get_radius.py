# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def getDistance(circle, current):
    x = abs(circle[0] - current[0])
    y = abs(circle[1] - current[1])

    length = math.sqrt((x * x) + (y * y))
    return length

def solution(A, B, X, Y):
    # write your code in Python 3.6
    for i in range(len(A)):
        if getDistance([A[i], B[i]], [X, Y]) <= 20:
            return i 
    return -1