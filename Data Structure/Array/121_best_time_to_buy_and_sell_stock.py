class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(0, len(prices)-2):
            for j in range(1,len(prices)-1):
                maxProfit = max((prices[j] - prices[i]), maxProfit)
                
        return maxProfit if maxProfit > 0 else 0