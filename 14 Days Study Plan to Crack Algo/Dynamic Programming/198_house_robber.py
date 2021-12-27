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