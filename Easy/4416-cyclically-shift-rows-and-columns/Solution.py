class Solution:
    def cyclicShift(
        self,
        n: int,
        grid: list[list[int]],
        rowShift: list[int],
        colShift: list[int]
    ) -> list[list[int]]:

        def reverse_row(row, left, right):
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1

        def reverse_col(col, top, bottom):
            while top < bottom:
                grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
                top += 1
                bottom -= 1

        # Rotate every row to the left
        for i in range(n):
            r = rowShift[i] % n

            if r:
                reverse_row(grid[i], 0, r - 1)
                reverse_row(grid[i], r, n - 1)
                reverse_row(grid[i], 0, n - 1)

        # Rotate every column upward
        for j in range(n):
            r = colShift[j] % n

            if r:
                reverse_col(j, 0, r - 1)
                reverse_col(j, r, n - 1)
                reverse_col(j, 0, n - 1)

        return grid