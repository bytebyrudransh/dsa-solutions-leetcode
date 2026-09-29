class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        md=1000000000+7
        if n<=k:
            return 0
        all=comb(n-1,k-1)%md
        if n&1==k&1:
            a=int((n+k)/2)
            allodd=comb(a-1,k-1)%md;
            all=(all%md-allodd%md+md)%md
        return all