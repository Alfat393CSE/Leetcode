class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Use bitmasks instead of sets
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        # Initialize bitmasks
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    val = int(board[r][c])
                    mask = 1 << val
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def get_candidates(r, c):
            box_idx = (r // 3) * 3 + (c // 3)
            used = rows[r] | cols[c] | boxes[box_idx]
            # bits 1–9 → candidates
            return [d for d in range(1, 10) if not (used >> d) & 1]

        def backtrack():
            if not empties:
                return True

            # MRV: pick the cell with fewest candidates
            r, c = min(empties, key=lambda pos: len(get_candidates(*pos)))
            empties.remove((r, c))
            box_idx = (r // 3) * 3 + (c // 3)

            for val in get_candidates(r, c):
                mask = 1 << val
                board[r][c] = str(val)
                rows[r] |= mask
                cols[c] |= mask
                boxes[box_idx] |= mask

                if backtrack():
                    return True

                # Undo
                board[r][c] = "."
                rows[r] ^= mask
                cols[c] ^= mask
                boxes[box_idx] ^= mask

            empties.append((r, c))
            return False

        backtrack()
