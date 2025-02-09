from typing import List
from queue import PriorityQueue


class Solution:

    def test(self):
        print()
        print(self.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))
        q = PriorityQueue()
        q.put()
        PriorityQ

    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        for x in range(w):
            for y in range(h):
                print(f'x y = {x}, {y}')
                if self.helper(board, word, 0, x, y, w, h):
                    return True
        return False

    def helper(self, board: List[List[str]], word: str, wordIndex: int, x: int, y: int, w: int, h: int) -> bool:
        # print(f'helper {wordIndex} {x} {y}')
        if wordIndex >= len(word):
            return True
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        if board[y][x] != word[wordIndex]:
            return False

        board[x][y] = '.'
        if self.helper(board, word, wordIndex + 1, x + 1, y, w, h): return True
        if self.helper(board, word, wordIndex + 1, x, y + 1, w, h): return True
        if self.helper(board, word, wordIndex + 1, x - 1, y, w, h): return True
        if self.helper(board, word, wordIndex + 1, x, y - 1, w, h): return True
        board[x][y] = word[wordIndex]
        return False
