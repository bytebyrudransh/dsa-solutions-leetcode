class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_no = 0
        dp_hold = -prices[0]

        for i in range(1,n+1):
            curr_no = max(dp_hold + prices[i-1] - fee, dp_no)
            curr_hold = max(dp_no - prices[i-1], dp_hold)
            dp_no = curr_no
            dp_hold = curr_hold
        
        return dp_no