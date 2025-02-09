from typing import List


class Solution:
    isDebug = False

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        col = set()
        rpc_dig = set()
        rmc_dig = set()

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                result.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c) in rpc_dig or (r-c) in rmc_dig:
                    continue
                col.add(c)
                rpc_dig.add(r+c)
                rmc_dig.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                rpc_dig.remove(r+c)
                rmc_dig.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return result
