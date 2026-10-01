class Solution:
    def countRotations(self, s: str, k: int) -> int:
        same = sum(a == b for a, b in pairwise(s)) + (s[0] == s[-1])
        return len(s) - same if k == same else same if k == same - 1 else 0