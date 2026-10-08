class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0] 
        max_profit = 0
        for price in prices:
            if minimum_price > price: 
                minimum_price = price 
            if max_profit < price- minimum_price:
                max_profit = price-minimum_price
        
        return max_profit


