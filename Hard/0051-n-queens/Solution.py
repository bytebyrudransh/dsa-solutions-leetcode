class Solution:
    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isSafe(row, col):
            # Vertical Up
            for i in range(row - 1, -1, -1):
                if board[i][col] == 'Q':
                    return False

            # Diagonal Left Up
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Diagonal Right Up
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def nQueen(row):
            # Base Case: all queens placed successfully
            if row == n:
                ans.append([''.join(r) for r in board])
                return

            # Try every column
            for col in range(n):
                if isSafe(row, col):
                    # Place queen
                    board[row][col] = 'Q'

                    # Explore next row
                    nQueen(row + 1)

                    board[row][col] = '.'

        nQueen(0)

        return ans