from collections import deque
from queue import Queue
from typing import List


class Solution:

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

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = deque()
        maxes = []

        for i in range(len(nums)):
            if mq and mq[0] <= i - k:
                mq.popleft()
            while mq and nums[mq[-1]] <= nums[i]:
                mq.pop()

            print(f'i = {i}, num = {nums[i]}, {mq}')

            mq.append(i)
            if i >= k - 1:
                maxes.append(nums[mq[0]])

        return maxes
