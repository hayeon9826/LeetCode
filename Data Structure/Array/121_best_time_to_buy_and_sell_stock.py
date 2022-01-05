# O(n^2)
# time limits exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(0, len(prices)-1):
            for j in range(i+1,len(prices)):
                maxProfit = max((prices[j] - prices[i]), maxProfit)
                
        return maxProfit if maxProfit > 0 else 0


# O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
                return 0
            
        today, profit = prices[0], 0
        for i in range(1,len(prices)):
            # if prices[i] is smaller than today, turn today to prices[i]
            if prices[i] < today:
                today = prices[i]
            # else, get the maximum of prices[i]-today and profit(default 0)
            else:
                profit = max(prices[i]-today,profit)
        return profit

# console
# Input: prices = [7,1,5,3,6,4]
# Output: 5
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
                return 0
            
        today, profit = prices[0], 0
        for i in range(1,len(prices)):
            print(today, '@@today')
            if prices[i] < today:
                today = prices[i]
            else:
                profit = max(prices[i]-today,profit)
        return profit

# 7 @@today
# 1 @@today
# 1 @@today
# 1 @@today
# 1 @@today