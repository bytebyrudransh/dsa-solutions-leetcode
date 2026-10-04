class Solution:
    def countGoodStrings(self, n: int) -> int:
        if n == 0:
            return 0

        mod = 10**9 + 7

        def multiply(A, B):
            C = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
            return C

        T = [[1, 1], [1, 0]]
        res = [[1, 0], [0, 1]]
        p = n - 1

        while p > 0:
            if p & 1:
                res = multiply(res, T)
            T = multiply(T, T)
            p >>= 1

        fib = res[0][0]
        return (2 * fib) % mod