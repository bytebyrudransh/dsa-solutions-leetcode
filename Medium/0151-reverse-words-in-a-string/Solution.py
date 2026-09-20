class Solution(object):
    def reverseWords(self, s):
        x = s.split()
        reversedWords = x[::-1]   
        answer = " ".join(reversedWords)
        return answer