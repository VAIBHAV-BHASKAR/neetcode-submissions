class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        
        max_profit = 0
        
        
        for price in prices:
            
            # profit if sold today
            profit = price - min_price
            
            # update best profit
            max_profit = max(max_profit, profit)
            
            # update minimum buying price
            min_price = min(min_price, price)
        
        
        return max_profit