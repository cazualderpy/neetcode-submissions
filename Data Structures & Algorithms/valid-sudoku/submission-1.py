class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcheck = set()
        colcheck = set()
        for row in board:
            for num in row:
                if num not in rowcheck and num != ".":
                    rowcheck.add(num)
                elif num == ".":
                    pass
                else:
                    return False
            rowcheck.clear()

        # Äußere Schleife: Spalten (0 bis 8)
        for col_idx in range(9):
        # Innere Schleife: Zeilen (0 bis 8)
            for row_idx in range(9):
                num = board[row_idx][col_idx]
                if num not in colcheck and num != ".":
                    colcheck.add(num)
                elif num == ".":
                    pass
                else:
                    return False
            colcheck.clear()
        boxcheck = set()
        for box_row in range(0, 9, 3):        # Startzeile der Box: 0, 3, 6
            for box_col in range(0, 9, 3):    # Startspalte der Box: 0, 3, 6
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        num = board[r][c]
                        if num == ".":
                            continue
                        if num in boxcheck:
                            return False
                        boxcheck.add(num)
                boxcheck.clear()
        return True
        
        
