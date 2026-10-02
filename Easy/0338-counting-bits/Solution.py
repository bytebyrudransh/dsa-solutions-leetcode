class Solution:
    def countBits(self, n: int) -> List[int]:
        bins: list[int] = [0] * (n+1)

        for i in range(0, n+1):
            if i % 2 == 0:
                bins[i] = bins[i // 2]   
            else:
                bins[i] = bins[i // 2] + 1

        return bins