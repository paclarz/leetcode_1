# problem No.0121
# created by setup.py at 2024-06-17 01:32:58

from solve import Jun_17_0121

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

def main():
    solution = Jun_17_0121
    FUN = solution.Solution().maxProfit

    assert FUN([7, 1, 5, 3, 6, 4]) == 5
    assert FUN([7, 6, 4, 3, 1]) == 0
    assert FUN([2, 4, 1]) == 2
