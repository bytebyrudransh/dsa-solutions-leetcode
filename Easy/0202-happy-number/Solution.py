class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        if n==1: return True
        while n != 1 and n not in seen:
            seen.add(n)
            k=n
            ans=0
            while k>0:
                r=k%10
                k=k//10
                ans=ans+r*r
            n=ans  

        return n == 1            