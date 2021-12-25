class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                solution.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i+1)
                backtrack(sub + s[i], i+1)
        solution = []
        backtrack()
        return solution


# https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
def letterCasePermutation(self, S):
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res


# https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)
                
        res = []
        backtrack()
        return res

# https://leetcode.com/problems/letter-case-permutation/discuss/369127/Python3-backtracking-solution
class Solution:
	def letterCasePermutation(self, S: str) -> List[str]:
		self.res=[]
		self.dfs(S,'',0)
		return self.res

	def dfs(self,S,path,index):
		if index==len(S):
			self.res.append(path)            
			return

		if S[index].isalpha():
			self.dfs(S,path+S[index].lower(),index+1)
			self.dfs(S,path+S[index].upper(),index+1)
		else:
			self.dfs(S,path+S[index],index+1)