class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if smth buy = x
        #if smt sell = x return sell-buy
        buy = prices[0]
        best = 0

        for i in prices:
            if i < buy: 
                buy = i
            if i - buy > best:
                best = i - buy
            
        
        return best

        