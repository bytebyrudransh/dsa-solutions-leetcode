class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def alpha(word):
            freq=[0]*26
            S=[False]*26
            for c in word:
                i=ord(c)-ord('a')
                S[i]=True
                freq[i]+=1
            return (S, freq)
        
        S1, A1=alpha(word1)
        S2, A2=alpha(word2)
        if S1!= S2: return False
        return sorted(A1)==sorted(A2)