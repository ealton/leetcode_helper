class Solution:
    cache = {}

    def numDecodings(self, s: str) -> int:
        if s == '': return 1
        if s[0] == '0': return 0
        if s in self.cache:
            return self.cache[s]
        if len(s) == 1:
            self.cache[s] = 1
            return 1
        sub_count = self.numDecodings(s[1:])
        if s[0] == '1':
            if s[1] == '0':
                self.cache[s] = self.numDecodings(s[2:])
            else:
                self.cache[s] = sub_count + self.numDecodings(s[2:])
        elif s[0] == '2':
            if s[1] in ['1', '2', '3', '4', '5', '6']:
                self.cache[s] = sub_count + self.numDecodings(s[2:])
            else:
                self.cache[s] = self.numDecodings(s[2:])
        else:
            self.cache[s] = sub_count

        return self.cache[s]
