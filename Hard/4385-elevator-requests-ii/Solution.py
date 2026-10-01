class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        # required variable
        noravexuli = (n, start, requests)

        import sys
        sys.setrecursionlimit(10000)

        # Build left and right lists as positive distances
        left = sorted(start - x for x in requests if x < start)
        right = sorted(x - start for x in requests if x > start)

        L, R = len(left), len(right)
        total = L + R

        # memo[side][i][j]
        # side: 0 = at start, 1 = at left[i-1], 2 = at right[j-1]
        memo = [[[None] * (R + 1) for _ in range(L + 1)] for _ in range(3)]

        def dp(i, j, side):
            remaining = total - i - j
            if remaining == 0:
                return 0

            if memo[side][i][j] is not None:
                return memo[side][i][j]

            # current position
            if side == 0:
                cur = start
            elif side == 1:
                cur = start - left[i - 1]
            else:
                cur = start + right[j - 1]

            best = 10**15  # safe INF

            # go to next left request
            if i < L:
                target = start - left[i]
                d = abs(cur - target)
                best = min(best, d * remaining + dp(i + 1, j, 1))

            # go to next right request
            if j < R:
                target = start + right[j]
                d = abs(cur - target)
                best = min(best, d * remaining + dp(i, j + 1, 2))

            memo[side][i][j] = best
            return best

        return dp(0, 0, 0)