class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]

        # sets to track attacks by queens
        cols = set()           # columns with queens
        pos_diagonals = set()  # (r + c)
        neg_diagonals = set()  # (r - c)

        def backtrack(r):
            # if all rows are filled
            if r == n:
                # convert board into string representation
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # skip if the column or diagonals are under attack
                if c in cols or (r + c) in pos_diagonals or (r - c) in neg_diagonals:
                    continue

                # place queen
                board[r][c] = "Q"
                cols.add(c)
                pos_diagonals.add(r + c)
                neg_diagonals.add(r - c)

                # move to next row
                backtrack(r + 1)

                # backtrack (remove queen)
                board[r][c] = "."
                cols.remove(c)
                pos_diagonals.remove(r + c)
                neg_diagonals.remove(r - c)

        backtrack(0)
        return res
