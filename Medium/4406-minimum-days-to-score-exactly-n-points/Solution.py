class Solution:

    def minDays(self, n: int) -> int:

        INF = float('inf')

        dp = [INF] * (n + 1)
        dp[0] = 0

        k = 1

        while k * (k + 1) // 2 <= n:

            pnt = k * (k + 1) // 2
            cst = k + 1

            for i in range(pnt, n + 1):
                dp[i] = min(
                    dp[i],
                    dp[i - pnt] + cst
                )

            k += 1

        return dp[n] - 1