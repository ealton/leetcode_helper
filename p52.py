class Solution:
    isDebug = False

    def totalNQueens(self, n: int) -> int:
        col = set()
        rpc_dig = set()
        rmc_dig = set()

        res = 0
        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return
            for c in range(n):
                if c in col or (r+c) in rpc_dig or (r-c) in rmc_dig:
                    continue
                col.add(c)
                rpc_dig.add(r+c)
                rmc_dig.add(r-c)

                backtrack(r+1)

                col.remove(c)
                rpc_dig.remove(r+c)
                rmc_dig.remove(r-c)

        backtrack(0)
        return res
