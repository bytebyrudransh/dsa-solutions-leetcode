from math import gcd
from typing import List

class Solution:
    def solve(self, pre: List[int], suff: List[int], skip: int, a: List[int]) -> int:
        n = len(a)
        for i in range(1, n + 1):
            if i - 1 == skip:
                pre[i] = pre[i - 1]
                continue
            pre[i] = gcd(pre[i - 1], a[i - 1])
        for i in range(n - 1, -1, -1):
            if i == skip:
                suff[i] = suff[i + 1]
                continue
            suff[i] = gcd(suff[i + 1], a[i])
        curr = 0
        for i in range(n - 1):
            if i == skip:
                continue
            if pre[i + 1] == suff[i + 1]:
                curr += 1
        return curr

    def maxValidSplits(self, a: List[int]) -> int:
        n = len(a)
        ans = 0
        premain = [0] * (n + 1)
        for i in range(1, n + 1):
            premain[i] = gcd(premain[i - 1], a[i - 1])

        for i in range(n + 1):
            if i > 0 and premain[i] == premain[i - 1]:
                continue
            skip = i - 1
            pre = [0] * (n + 1)
            suff = [0] * (n + 1)
            ans = max(ans, self.solve(pre, suff, i - 1, a))


        return ans