class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]
                if num == '.':
                    continue
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in squares[r//3][c//3]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[r//3][c//3].add(num)
                print(rows)
        return True