class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        vmin = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < vmin:
                vmin = prices[i]
                
            profit = max(profit, prices[i] - vmin)
                
        return profit