class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, p2-p1) for (p1, p2) in zip(prices, prices[1:]))