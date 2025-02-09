class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ei = len(s) - 1
        while s[ei] == " " and ei >= 0:
            ei -= 1

        si = ei-1
        while s[si] != " " and si >= 0:
            si -= 1

        return ei - si
