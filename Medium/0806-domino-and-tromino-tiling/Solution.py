from functools import cache

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        COMPLETE = 0
        MISSING_TOP = 1
        MISSING_BOTTOM = 2

        @cache
        def count_tilings(column: int, state: int) -> int:
            if column == n:
                return 1 if state == COMPLETE else 0

            if column > n:
                return 0

            ways = 0

            if state == COMPLETE:
                # Place one vertical domino.
                ways += count_tilings(column + 1, COMPLETE)

                # Place two horizontal dominoes.
                ways += count_tilings(column + 2, COMPLETE)

                # Place a tromino, leaving one cell incomplete.
                ways += count_tilings(column + 1, MISSING_TOP)
                ways += count_tilings(column + 1, MISSING_BOTTOM)

            elif state == MISSING_TOP:
                # Extend the gap using a horizontal domino.
                ways += count_tilings(column + 1, MISSING_BOTTOM)

                # Complete the gap using a tromino.
                ways += count_tilings(column + 2, COMPLETE)

            elif state == MISSING_BOTTOM:
                # Extend the gap using a horizontal domino.
                ways += count_tilings(column + 1, MISSING_TOP)

                # Complete the gap using a tromino.
                ways += count_tilings(column + 2, COMPLETE)

            return ways % MOD

        return count_tilings(0, COMPLETE)