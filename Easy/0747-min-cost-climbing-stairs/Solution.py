class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one_step = cost[-1]   # dp[i+1]
        two_steps = 0         # dp[i+2]

        for i in range(len(cost) - 2, -1, -1):
            current = cost[i] + min(one_step, two_steps)
            two_steps = one_step
            one_step = current

        return min(one_step, two_steps)