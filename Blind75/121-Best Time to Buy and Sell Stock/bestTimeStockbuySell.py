class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = max(prices)
        maxPr = 0                
        for price in prices:
            minP = min(minP, price)
            maxPr = max(maxPr, price - minP)
        
        return maxPr
