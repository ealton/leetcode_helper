import itertools
import sys
from typing import List

class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        accumulated = list(itertools.accumulate(nums))
        accumulated.insert(0, 0)
        # print(accumulated)
        ans = 0
        foundAnswer = False
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) == k:
                    if foundAnswer:
                        ans = max(ans, accumulated[j+1] - accumulated[i])
                    else:
                        foundAnswer = True
                        ans = accumulated[j+1] - accumulated[i]
        return ans

    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[1])
        print(points)

        stack = [points[0]]

        ans = 0
        for i, point in enumerate(points):
            if i == 0:
                continue
            while stack and (point[0] == stack[-1][0] or point[1] == stack[-1][1]):
                ans += 1
                stack.pop()

            if not stack:
                stack.append(point)
                continue

            while stack and point[0] < stack[-1][0]:
                ans += 1
                stack.pop()
            stack.append(point)

        print(f'ans = {ans}')
        return ans



    def test(self):
        # print(self.countOfPairs(3,1,3))
        # [37, 6, 46, 32, 23]

        # print(self.maximumSubarraySum([1,5], 2))
        # print(self.maximumSubarraySum([1,2,3,4,5,6], 1))
        # print(self.maximumSubarraySum([-1,3,2,4,5], 3))
        # print(self.maximumSubarraySum([-1,3,2,4,5,2], 3))
        # print(self.maximumSubarraySum([-1,-2,-3,-4], 2))
        #
        #
        #
        # return


        assert self.numberOfPairs([[1,1],[2,2],[3,3]]) == 0, "ERROR1"
        assert self.numberOfPairs([[6,2],[4,4],[2,6]]) == 2, "ERROR2"
        assert self.numberOfPairs([[3,1],[1,3],[1,1]]) == 2, "ERROR3"
        assert self.numberOfPairs([[0,1],[1,3],[6,1]]) == 2, "ERROR4"
        assert self.numberOfPairs([[0,2],[5,1],[5,6]]) == 2, "ERROR5"
        assert self.numberOfPairs([[1,6],[3,1],[4,4],[2,0]]) == 3, "ERROR6"
        # print(self.minOrAfterOperations([0,1073741823], 0))
        # print(self.minOrAfterOperations([7,3,15,14,2,8], 4))
        # print()
        # print(self.minOrAfterOperations([10,7,10,3,9,14,9,4], 4))


        # for i in range(3, 11):
        #     print(self.countOfPairs(i, 1, i))
        #     print(self.countOfPairs2(i, 1, i))

