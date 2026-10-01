class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        res = 0

        for num in nums:
            # Last digit tells how many digits belong to x
            width = num % 10

            # Remove the width digit
            d = str(num // 10)

            # Extract x and y
            x = int(d[:width]) % MOD
            y = int(d[width:])

            # Binary exponentiation: calculate x^y % MOD
            exp = 1

            while y > 0:
                # If current bit of y is 1, include x
                if y % 2 == 1:
                    exp = (exp * x) % MOD

                # Square the base and halve the exponent
                x = (x * x) % MOD
                y //= 2

            # Add current decoded power to the answer
            res = (res + exp) % MOD

        return res