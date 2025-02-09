from collections import deque
from operator import itemgetter
from queue import Queue
from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelopes = sorted(envelopes, key=itemgetter(0))
        print(sorted_envelopes)


    def test(self):
        q = Queue()
        # q.

        # print(self.calculate("1 + 1"))
        # print(self.calculate(" 2-1 + 2 "))
        # print(self.calculate(" 4+5+2"))
        # print(self.calculate("1+(4+5+2)"))
        # print(self.calculate("1+(4+5+2)-3"))
        # print(self.calculate("(1+(4+5+2)-3)"))
        # print(self.calculate("(1+(4+5+2)-3)+(6+8)"))
        print(self.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

