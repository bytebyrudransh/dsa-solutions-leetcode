class Solution:
    def minRotations(self, n, s):
        def dist(a, b):
            x = abs(a - b)
            return min(x, 10 - x)

        pref = [0] * n
        suf = [0] * n

        pref[0] = dist(0, int(s[0]))

        for i in range(1, n):
            pref[i] = pref[i - 1] + dist(int(s[i - 1]), int(s[i]))

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + dist(int(s[i]), int(s[i + 1]))

        mn = pref[n - 1]

        for k in range(n):
            if k == 0:
                cur = dist(0, int(s[n - 1])) + suf[0]
            else:
                cur = (pref[k - 1]
                       + dist(int(s[k - 1]), int(s[n - 1]))
                       + suf[k])

            mn = min(mn, cur)

        return mn