from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        total_profits = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            # print(f'i = {i}')
            if prices[i] < prices[i-1]:
                # print(f'get profit: {i-1} - {buy_price}')
                total_profits += max(0, prices[i-1] - buy_price)
                buy_price = prices[i]
            else:
                if i == len(prices) - 1:
                    # print(f'end action: {i} - {buy_price}')
                    total_profits += prices[i] - buy_price
        return total_profits