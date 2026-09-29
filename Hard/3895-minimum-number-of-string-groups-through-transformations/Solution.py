class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        # Booth's algorithm: lexicographically smallest rotation
        def booth(s: str) -> str:
            n = len(s)
            if n == 0:
                return ""
            s2 = s + s
            i, j, k = 0, 1, 0
            while i < n and j < n and k < n:
                if s2[i + k] == s2[j + k]:
                    k += 1
                else:
                    if s2[i + k] > s2[j + k]:
                        i = i + k + 1
                    else:
                        j = j + k + 1
                    if i == j:
                        j += 1
                    k = 0
            start = min(i, j)
            return s2[start:start + n]

        signatures = set()

        for w in words:
            even = w[0::2]
            odd = w[1::2]
            sig = (booth(even), booth(odd))
            signatures.add(sig)

        return len(signatures)