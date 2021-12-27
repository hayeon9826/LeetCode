class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, prev2, current = 0, 0, 0
        # recursive dp
        # f(0) = nums[0]
        # f(1) = max(num[0], num[1])
        # f(k) = max( f(k-2) + nums[k], f(k-1) )
        # ... f(k)를 구함
        for num in nums:
            current = max(prev + num, prev2)
            prev = prev2
            prev2 = current
        return current
            


# source: https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.
class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now


# 참고하면 좋은 풀이: https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP

# Dynamic Programming - Memoization
class Solution:
    def rob(self, A):
        @cache
        def rob(i):
            return max(rob(i+1), A[i] + rob(i+2)) if i < len(A) else 0
        return rob(0)


# Dynamic Programming - Tabulation
class Solution:
    def rob(self, A):
        if len(A) == 1: return A[0]
        dp = [*A]
        dp[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            dp[i] = max(dp[i-1], A[i] + dp[i-2])
        return dp[-1]



# Space-Optimzed Dynamic Programming
class Solution:
    def rob(self, A):
        prev2, prev, cur = 0,0,0
        for i in A:
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur