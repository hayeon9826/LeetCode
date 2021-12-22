# python combination 라이브러리 사용
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solution = []
        def backtrack(remain, combination, next):
            if remain == 0:
                solution.append(combination.copy())
            else:
                for i in range(next, n + 1):
                    combination.append(i)
                    backtrack(remain - 1, combination, i + 1)
                    combination.pop()
        
        backtrack(k, [], 1)
        return solution


# 풀이 예시: https://hyoeun-log.tistory.com/124