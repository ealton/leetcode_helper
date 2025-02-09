from typing import List


class Solution:

    def test(self):
        print(self.wordBreak('catsanddog', ["cat","cats","and","sand","dog"]))
        # a = 0

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        cache = {}
        def dp(s: str, wordList: List[str], wordDict: List[str]):
            if not s:
                result.append(' '.join(wordList))
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    wordList.append(s[:i])
                    dp(s[i:], wordList, wordDict)
                    wordList.pop()
        dp(s, [], wordDict)
        return result
