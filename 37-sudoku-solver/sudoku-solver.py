class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and candidates
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        # Precompute candidate options for each empty cell
        def get_candidates(r, c):
            box_idx = (r // 3) * 3 + (c // 3)
            return [ch for ch in map(str, range(1, 10))
                    if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_idx]]

        # Backtracking with MRV heuristic
        def backtrack():
            if not empties:
                return True

            # Pick the empty cell with the fewest candidates (MRV)
            empties.sort(key=lambda pos: len(get_candidates(*pos)))
            r, c = empties.pop(0)
            box_idx = (r // 3) * 3 + (c // 3)

            for ch in get_candidates(r, c):
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box_idx].add(ch)

                if backtrack():
                    return True

                # Undo move
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[box_idx].remove(ch)

            empties.insert(0, (r, c))  # put back if failed
            return False

        backtrack()
