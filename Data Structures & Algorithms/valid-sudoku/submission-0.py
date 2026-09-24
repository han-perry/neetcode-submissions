from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            c = Counter(row)
            c.pop(".", None)
            if any(val >= 2 for val in c.values()):
                return False

        # cols
        for j in range(9):
            seen = set()
            for i in range(9):
                elem = board[i][j]
                if elem == ".":
                    continue
                elif elem in seen:
                    return False
                seen.add(elem)
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()

                for rr in range(r, r+3):
                    for cc in range(c, c+3):
                        elem = board[rr][cc]
                        if elem == ".":
                            continue
                        elif elem in seen:
                            return False
                        seen.add(elem)
        

        return True

        