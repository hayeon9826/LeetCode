class Solution:
    def climbStairs(self, n: int) -> int:
        solution = [1, 2]
        
        for i in range(2, n):
            solution.append(solution[i-1] + solution[i-2])
        return solution[n-1]
        
        