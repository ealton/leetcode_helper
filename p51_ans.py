from typing import List


class Solution:
    isDebug = False

    result = []
    col = set()
    rpcDig = set()
    rmcDig = set()

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.col = set()
        self.rpcDig = set()
        self.rmcDig = set()

        board = [["."] * n for i in range(n)]
        self.backtrack(board, 0, n)
        return self.result

    def backtrack(self, board: List[List[str]], r: int, n: int):
        if r == n:
            copy = ["".join(row) for row in board]
            self.result.append(copy)
            return
        for c in range(n):
            if c in self.col or (r + c) in self.rpcDig or (r - c) in self.rmcDig:
                continue

            self.col.add(c)
            self.rpcDig.add(r+c)
            self.rmcDig.add(r-c)
            board[r][c] = "Q"

            self.backtrack(board, r + 1, n)

            self.col.remove(c)
            self.rpcDig.remove(r+c)
            self.rmcDig.remove(r-c)
            board[r][c] = "."
