# Imagine you're a trader looking at historical stock price data, with an array 'prices' where each 'prices[i]' represents the stock's price on the ith day.
# Your goal is to identify the perfect day to buy and another day to sell that stock to maximize your earnings.
# Remember, the selling day must be after the buying day.
# If it's not possible to make any profit, your earnings would be 0.
 
# For instance: 
# - With an input 'prices' array of [7,1,5,3,6,4], the optimal strategy would be to purchase the stock on day 2 at a price of 1 and sell it on day 5 at a price of 6, yielding a profit of 5 (6-1).
# - For a 'prices' array of [7,6,4,3,1], no profit can be made, so the output would be 0.
 
# Constraints to keep in mind: The length of the 'prices' array will be at least 1 and no more than 10^5, with each price ranging from 0 to 10^4.

def optimizeTradingGains(prices):
    if len(prices) <= 1:
        return 0
    buy = prices[0]
    profit = 0
    for i in range(1,len(prices)):
        if buy < prices[i]:
            profit = max(profit, prices[i]-buy)
        else:
            buy = prices[i]
    return profit

print(optimizeTradingGains([7, 1, 5, 3, 6, 4]))