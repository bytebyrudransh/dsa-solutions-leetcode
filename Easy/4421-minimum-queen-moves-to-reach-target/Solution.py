class Solution:
    def minQueenMoves(self, s: list[int], t: list[int]) -> int:
        if s == t:
            return 0
        if s[0] == t[0] or s[1] == t[1]:
            return 1
        if ((s[0]+s[1]) == (t[0]+t[1])) or ((s[0]-s[1]) == (t[0]-t[1])):
            return 1
        return 2