class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        self.dfs(nums, [], solution)
        return solution
        
    def dfs(self, nums, temp, solution):
      # 만약 nums 배열에 아무 원소도 없다면, temp 배열에 모든 원소가 이동되었다는 뜻.
      # 따라서 해당 temp 배열을 정답 (solution) 배열에 추가한다. 
      # deep copy로 추가
        if len(nums) == 0:
            solution.append(temp[:])
            return
        else:
            for i in range(len(nums)):
              # nums 배열에서 n 번째 숫자를 제거하고, temp 배열에 추가한다
                self.dfs(nums[:i]+nums[i+1:], temp+[nums[i]], solution)



# DFS
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# source: https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).



class Solution:
    def permute(self, l: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            if len(path) == len(l):
                res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over
                return

            for i, letter in enumerate(l):
                # skip used letters
                if used[i]:
                    continue
                # add letter to permutation, mark letter as used
                path.append(letter)
                used[i] = True
                dfs(path, used, res)
                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False
            
        res = []
        dfs([], [False] * len(l), res)
        return res

# source: https://leetcode.com/problems/permutations/discuss/685868/DFSbacktracking-PythonJavaJavascript-PICTURE