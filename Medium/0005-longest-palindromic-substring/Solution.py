class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for length in range(n, 0, -1):
            for i in range(n - length + 1):
                substring = s[i : i + length]
                if substring == substring[::-1]:
                    return substring