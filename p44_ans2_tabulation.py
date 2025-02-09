class Solution:
    cache = []

    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        cache[0][0] = True

        for j in range(1, len(p) + 1):
            flag = True
            for k in range(1, j + 1):
                if p[k - 1] != '*':
                    flag = False
                    break
            cache[0][j] = flag

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    cache[i][j] = cache[i - 1][j - 1]
                elif p[j - 1] == '*':
                    cache[i][j] = cache[i - 1][j] or cache[i][j - 1]
                else:
                    cache[i][j] = False

        return cache[len(s)][len(p)]
