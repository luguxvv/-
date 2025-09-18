def maxProfit(prices):
    best_buy = prices[0]
    best_profit = 0
    
    for current_price in prices:
        if current_price < best_buy:
            best_buy = current_price
        current_profit = current_price - best_buy
        if current_profit > best_profit:
            best_profit = current_profit
    
    return best_profit
