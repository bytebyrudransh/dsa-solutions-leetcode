class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[]
        for w in s:
            if w in "aeiouAEIOU":
                vowel.append(w)
        res=""
        for w in s:
            if w in "aeiouAEIOU":
                res+=vowel.pop()
            else:
                res+=w
        return res