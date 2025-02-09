class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        p = self.removeDuplicateStars(p)
        sn = len(s)
        pn = len(p)
        cache_previous = [False] * (pn + 1)
        cache_current = [False] * (pn + 1)
        cache_previous[0] = True
        start_index = 1

        for j in range(1, pn + 1):
            if p[j-1] == '*':
                cache_previous[j] = cache_previous[j-1]

        for i in range(1, sn + 1):
            for j in range(start_index, pn + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    cache_current[j] = cache_previous[j-1]
                elif p[j - 1] == '*':
                    cache_current[j] = cache_previous[j] or cache_current[j-1]
                    if cache_current[j]:
                        start_index = j
                else:
                    cache_current[j] = False

            if pn > 0 and p[pn-1] == '*' and cache_current[pn]:
                return True

            for j in range(pn + 1):
                cache_previous[j] = cache_current[j]

        if sn == 0:
            return cache_previous[pn]
        return cache_current[pn]

    def removeDuplicateStars(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            if i == 0:
                result = s[i]
                continue
            if s[i] == '*' and s[i-1] == '*':
                continue
            result += s[i]
        return result
