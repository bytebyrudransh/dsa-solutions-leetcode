class Solution:
    def largestString(self, nums):
        # convert[i] = 2^i, so convert[0..25] holds powers of two for 'a' to 'z'
        convert = [1] * 26
        base = 1

        for i in range(26):
            convert[i] = base
            base *= 2

        res = []

        for n in nums:
            cur = []

            # greedily break n into powers of two (its binary representation),
            # largest power first, mapping each power to a letter
            while n > 0:
                i = 25

                while convert[i] > n:
                    i -= 1

                cur.append(chr(ord('a') + i))
                n -= convert[i]

            res.append("".join(cur))

        return res