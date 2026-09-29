class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i):
        while i <= self.n:
            self.bit[i] += 1
            i += i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        even = odd = 0
        val = [0] * (n + 1)
        oddCnt = [0] * (n + 1)

        groups = [[] for _ in range(n + 1)]
        groups[0].append(0)

        for i in range(1, n + 1):
            if nums[i - 1] & 1:
                odd += 1
            else:
                even += 1
            oddCnt[i] = odd
            val[i] = b * even - a * odd
            groups[odd].append(i)

        comp = sorted(set(val))
        bit = Fenwick(len(comp))

        ans = 0
        active = 0

        for curOdd in range(n + 1):
            while active < curOdd:
                for idx in groups[active]:
                    bit.update(bisect_left(comp, val[idx]) + 1)
                active += 1

            for idx in groups[curOdd]:
                p = bisect_left(comp, val[idx]) + 1
                ans += bit.query(len(comp)) - bit.query(p - 1)

        return ans