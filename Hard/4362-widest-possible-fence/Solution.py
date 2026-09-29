class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        freq = Counter(planks)
        sums = defaultdict(int)
        vals = list(freq.keys())
        
        ans = 1
        m = len(vals)

        for i in range(m):
            x = vals[i]
            cx = freq[x]

            sums[2 * x] += cx // 2

            for j in range(i + 1, m):
                y = vals[j]
                sums[x + y] += min(cx, freq[y])


        for h, pairs in sums.items():
            ans = max(ans, pairs + freq.get(h, 0))

        if freq:
            ans = max(ans, max(freq.values()))

        return ans