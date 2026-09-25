class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for a in range(n+1):
            b = 0
            while a>0:
                b+=a&1
                a = a>>1
            ans.append(b)
        return ans