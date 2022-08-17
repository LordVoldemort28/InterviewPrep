def get_max_profit(stock_prices):

    # Calculate the max profit
    min_price = stock_prices[0]
    max_profit = 0

    for idx in range(1, len(stock_prices)):

        current_price = stock_prices[idx]

        potential_profit = current_price - min_price

        max_profit = max(potential_profit, max_profit)

        min_price = min(min_price, current_price)

    return max_profit


actual = get_max_profit([1, 5, 3, 2])
print(actual)
