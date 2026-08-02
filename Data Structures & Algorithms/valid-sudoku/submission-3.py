class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = collections.defaultdict(set)
        column_dict = collections.defaultdict(set)
        box_dict = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                e = board[r][c]
                if e == '.':
                    continue
                elif (e in row_dict[r]) or (e in column_dict[c]) or (e in box_dict[(r//3,c//3)]):
                    return False
                else:
                    row_dict[r].add(e)
                    column_dict[c].add(e)
                    box_dict[(r//3,c//3)].add(e)
        return True
        