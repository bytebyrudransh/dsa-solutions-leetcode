class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        while a or b or c:
            n1 = a & 1
            n2 = b & 1
            n3 = c & 1

            if n3:
                if not n1 and not n2:
                    ans += 1
            else:
                if n1 and n2:
                    ans += 2
                elif n1 or n2:
                    ans += 1

            a = a >> 1
            b = b >> 1
            c = c >> 1

        return ans