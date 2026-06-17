class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        max_profit = 0
        min_buy = prices[0]

        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)

        return max_profit