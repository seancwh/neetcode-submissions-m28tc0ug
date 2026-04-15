class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                b_n = i//3 + j//3*5
                if (board[i][j] in r[i] 
                    or board[i][j] in c[j]
                    or board[i][j] in b[b_n]):
                    return False
                else:
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    b[b_n].add(board[i][j])
        return True