# python combination 라이브러리 사용
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))


#backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solution = []

        
        def backtrack(k, combination, next):
            if k == 0:
              # 3. 만약 combination 안에 숫자가 k개 다 찾다면, 해당 combination을 solution 배열에 넣는다.
                solution.append(combination.copy())
            else:
                for i in range(next, n + 1):
                    # 1. combination에 테스트할 숫자를 넣어준다. 숫자 하나 들어갈때 마다 총 숫자 (k) 를 하나씩 줄인다.
                    combination.append(i)
                    # 2. next 값인 i 를 하나 올려서 다시 backtracking 시작
                    backtrack(k - 1, combination, i + 1)
                    # 4. k == 0 까지 갔다면, combination 마지막에 있던 숫자를 빼고 새로운 숫자 넣고 다시 시작한다.
                    combination.pop()
        
        backtrack(k, [], 1)
        return solution


# 풀이 예시: https://hyoeun-log.tistory.com/124


# dfs example
class Solution(object):
    def combine(self, n, k):
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
    def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+[nums[i]], ret)

# source: https://leetcode.com/problems/combinations/discuss/26990/Python-easy-to-understand-DFS-solution