class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j][i] = number of ways using points 0..i with exactly j segments,
        # where the j-th segment's right endpoint is <= i (segment may or may not touch i)
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(n):
            dp[0][i] = 1  # 0 segments: exactly 1 way (draw nothing)

        for j in range(1, k + 1):
            # dp2[i] = ways to have j segments where the j-th segment ends exactly at i
            # (i.e., "committed" state), used to build running sums
            running_sum = 0
            dp2 = [0] * n

            for i in range(1, n):
                # dp2[i]: either extend the segment ending at i-1 to now end at i,
                # or start a brand new j-th segment ending at i using dp[j-1][i-1]
                dp2[i] = (dp2[i - 1] + dp[j - 1][i - 1]) % MOD
                dp[j][i] = (dp[j][i - 1] + dp2[i]) % MOD

        return dp[k][n - 1]

