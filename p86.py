class Solution:
    cache = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # print(f'start: {s1}, {s2}')
        if len(s1) == 1:
            return s1 == s2
        if s1 == s2:
            return True
        if (s1, s2) in self.cache:
            return self.cache[(s1, s2)]

        for i in range(1, len(s1)):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                self.cache[(s1, s2)] = True
                return True
            if self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[0:i], s2[-i:]):
                self.cache[(s1, s2)] = True
                return True

        self.cache[(s1, s2)] = False
        return False
