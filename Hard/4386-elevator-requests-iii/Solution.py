from typing import List

class Solution:
    def elevatorRequests(self, floors: int, start: int, requests: List[List[int]]) -> int:
        req = [[0, start]] + requests

        n = len(req)
        full_mask = (1 << n) - 1
        INF = 10**18

        dp = [[INF] * n for _ in range(1 << n)]
        dp[1][0] = 0

        for mask in range(full_mask + 1):
            for last in range(n):
                curr = dp[mask][last]
                if curr == INF:
                    continue

                for j in range(1, n):
                    if not (mask & (1 << j)):
                        new_mask = mask | (1 << j)

                        travel = abs(req[last][1] - req[j][1])
                        finish_time = max(curr + travel, req[j][0])

                        dp[new_mask][j] = min(dp[new_mask][j], finish_time)

        return min(dp[full_mask])