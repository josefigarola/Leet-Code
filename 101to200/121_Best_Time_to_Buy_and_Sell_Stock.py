class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0
        i = 0

        while(i<len(prices)):
            if(prices[i] < min_price):
                min_price = prices[i]
            if(prices[i] - min_price > max_price):
                max_price = prices[i] - min_price
            
            i+=1

        return max_price