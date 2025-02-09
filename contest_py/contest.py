import collections
import heapq
import itertools
import math
import sys
from functools import lru_cache
from typing import List
import bisect

import utils
from SieveOfEratosthenes import sieveOfEratosthenes


class Solution:

    def question(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        if totalSum == 0:
            return k * 2

        if k == 1:
            return 0

        oneIndices = []
        for i, num in enumerate(nums):
            if num == 1:
                oneIndices.append(i)

        print(f"oneIndices = {oneIndices}")

        targetOnes = k - maxChanges - 1
        if targetOnes <= 0:
            # we can use maxChanges to change to 1 to achieve our goal
            adjacent = 0
            for i in range(1, n):
                if i < n - 1 and nums[i] == 1 and nums[i - 1] == 1 and nums[i + 1] == 1:
                    adjacent = 2
                    break
                if nums[i] == 1 and nums[i - 1] == 1:
                    adjacent = 1

            adjacent = min(k - 1, adjacent)
            print(f"adjacent = {adjacent}")
            return adjacent + (max(0, k - adjacent - 1)) * 2

        left, right = 0, n
        shortest = n
        for i in range(len(oneIndices) - targetOnes):
            t = abs(oneIndices[i + targetOnes] - oneIndices[i])
            if t <= shortest:
                shortest = t
                left, right = i, i + targetOnes

        print(f"left, right = {left} {right}")

        totalWeight = 0
        for i in range(left, right + 1):
            totalWeight += oneIndices[i]
        midValue = totalWeight // len(oneIndices)
        print(f"midValue = {totalWeight} // {len(oneIndices)} = {midValue}")
        t = n
        midIndex = 0
        for i in range(left, right + 1):
            tt = abs(oneIndices[i] - midValue)
            if tt < t:
                t = tt
                midIndex = oneIndices[i]

        print(f"midIndex = {midIndex}")

        adjacent = 0
        if midIndex > 0 and nums[midIndex - 1] == 1:
            adjacent += 1
        if midIndex < n - 1 and nums[midIndex + 1] == 1:
            adjacent += 1

        adjacent = min(k - 1, adjacent)
        ans = adjacent
        neededOnes = k - 1 - adjacent
        print(f"neededOnes = {neededOnes}")
        if neededOnes <= 0:
            return ans

        if neededOnes <= maxChanges:
            ans += neededOnes * 2
            neededOnes = 0
        else:
            ans += maxChanges * 2
            neededOnes -= maxChanges

        print(f"neededOnes = {neededOnes}")

        if neededOnes <= 0:
            return ans

        distanceList = []
        for index in oneIndices:
            if index != midIndex and index != midIndex - 1 and index != midIndex + 1:
                distanceList.append(abs(index - midIndex))
        distanceList.sort()
        print(f"distanceList = {distanceList}")

        for distance in distanceList:
            ans += distance

        return ans

    # ["aagha", "bc"]
    def test(self):
        # print(self.question([1,1,0,0,0,1,1,0,0,1], 3, 1))
        # print(self.question([0,0,0,0], 2, 3))
        # print(self.question([1,0,1,0,1], 3, 0))
        # print(self.question([1,1], 2, 4))
        # print(self.question([1,1,1], 2, 1))
        # print(self.question([1,1,1], 6, 4))
        # print(self.question([0,1,1,1], 3, 0))
        print(self.question([1, 0, 1], 2, 0))


if __name__ == "__main__":
    Solution().test()


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        n, m = len(difficulty), len(worker)
        worker.sort()
        jobs = [[difficulty[i], -profit[i]] for i in range(n)]
        jobs.sort()
        jobIndex = 0
        ans = []
        availableJobs = []
        for w in worker:
            while jobIndex < m and jobs[jobIndex][0] <= w:
                heapq.heappush(availableJobs, jobs[jobIndex][1])
                jobIndex += 1
            if jobIndex == 0:
                ans.append(0)
            else:
                ans.append(-availableJobs[0])

        print(jobs)
        print(worker)
        print(ans)
        return sum(ans)
