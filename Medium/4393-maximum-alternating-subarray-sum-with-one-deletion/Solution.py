class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        neg = -float('inf')
        p1 = [[neg, neg], [neg, neg]]
        p2 = [[neg, neg], [neg, neg]]
        ans = neg

        for v in nums:
            x = v
            c = [[0, 0], [0, 0]]

            c[0][0] = max(x, p1[0][1] + x)
            c[0][1] = p1[0][0] - x
            c[1][0] = max(p1[1][1] + x, p2[0][1] + x)
            c[1][1] = max(p1[1][0] - x, p2[0][0] - x)

            for d in range(2):
                for s in range(2):
                    ans = max(ans, c[d][s])

            for d in range(2):
                for s in range(2):
                    p2[d][s] = p1[d][s]
                    p1[d][s] = c[d][s]

        return ans