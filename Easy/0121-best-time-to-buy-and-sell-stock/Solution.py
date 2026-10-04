class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        next_buy = 0
        next_hold = 0

        current_buy = 0
        current_hold = 0

        for i in range(n - 1, -1, -1):
            current_buy = max(-prices[i] + next_hold, next_buy)

            current_hold = max(prices[i], next_hold)

            next_buy = current_buy
            next_hold = current_hold

        return current_buy