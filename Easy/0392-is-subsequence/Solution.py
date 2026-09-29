class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = deque(s)
        
        for char in t:
            if s and char == s[0]:
                s.popleft()
        
        return len(s) == 0