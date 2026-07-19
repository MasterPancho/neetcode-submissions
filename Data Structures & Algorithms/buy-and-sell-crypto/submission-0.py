class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Highest number possible in python
        buy = float('inf')

        #Lowest sell point
        sell = 0

        for i, price in enumerate(prices):
            #Buy when price is cheapest
            if price < buy:
                buy = price
            
            #Sell when maximum profit can be made
            if (sell < price - buy):
                sell = price - buy

        return(sell)    


            