from typing import List


# O(n)
def max_profit(stock_prices: List[int]) -> int:
    purchase, sale, best_profit = float('inf'), 0, 0
    for price in stock_prices:
        if price > purchase:
            sale = max(sale, price)
        else:
            best_profit = max(best_profit, sale - purchase)
            purchase, sale = price, 0
    else:
        return max(best_profit, sale - purchase)


# basic cases
assert max_profit([1, 2]) == 1
assert max_profit([1, 2, 3, 1]) == 2
assert max_profit([1, 2, 3]) == 2

assert max_profit([2, 1]) == 0
assert max_profit([4, 3, 2, 1]) == 0
assert max_profit([1, 4, 2]) == 3

# accept cases
assert max_profit([9, 11, 8, 5, 7, 10]) == 5
assert max_profit([2, 3, 10, 6, 4, 8, 1]) == 8
assert max_profit([7, 9, 5, 6, 3, 2]) == 2
