class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        rr,cc = source
        tt, ee = target

        if rr ==tt and cc ==ee :
            return 0 

        if rr == tt or cc == ee or abs(rr -tt) == abs(cc -ee):
            return 1

        return 2
        