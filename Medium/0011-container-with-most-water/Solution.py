class Solution:
    def maxArea(self, h: List[int]) -> int:
        res = 0
        l, r = 0, len(h) - 1
        while l < r:
            res = max(res, (r - l) * min(h[l], h[r]))
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return res