class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        n = ceil(log2(max(a,b,c)))+1
        flip = 0
        for i in range(n):
            mask = 1<<i
            if c&mask:      #at a position, if c has a 1, then either b or a should have a 1, else flip one bit.
                if not (a&mask | b&mask):
                    flip+=1
            else:           #if c has 0, then both need to be 0. If not, then flip those bits.
                if a&mask:
                    flip+=1
                if b&mask:
                    flip+=1
        return flip