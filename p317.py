from typing import List
import sys

class Solution:
    def createDistanceMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        matrix = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                matrix[y][x] = 0 if grid[y][x] == 0 else -1
        return matrix

    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        obstacles = []
        houses = []
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1: houses.append((y, x))
                elif grid[y][x] == 2: obstacles.append((y, x))

        if len(houses) + len(obstacles) >= m * n:
            return -1

        def isValidSpace(matrix: List[List[int]], y: int, x: int) -> bool:
            nonlocal m, n
            if y < 0 or x < 0 or y >= m or x >= n:
                return False
            if matrix[y][x] < 0:
                return False
            return True

        def getMinimumDistance(matrix: List[List[int]], cy: int, cx: int) -> int:
            distance = sys.maxsize
            for y, x in [(cy-1, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)]:
                if isValidSpace(matrix, y, x) and matrix[y - 1][x] > 0:
                    distance = min(distance, matrix[y - 1][x])

            return -1 if distance == sys.maxsize else distance + 1

        def buildDistanceMatrix(sy: int, sx: int) -> List[List[int]]:
            nonlocal m, n, grid, obstacles
            distanceMatrix = self.createDistanceMatrix(grid)
            distanceMatrix[sy][sx] = 0
            candidates = [(sy, sx)]

            while len(candidates) > 0:
                nextCandidates = []
                for cy, cx in candidates:
                    for y, x in [(cy-1, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)]:
                        if y != sy and x != sx and isValidSpace(distanceMatrix, y, x):
                            distanceMatrix[y][x] = getMinimumDistance(distanceMatrix, cy - 1, cx)
                            if distanceMatrix[y][x] > 0:
                                nextCandidates.append((y, x))

                candidates = nextCandidates

            return distanceMatrix

        ans = [[0] * n for _ in range(m)]
        for hy, hx in houses:
            houseMatrix = buildDistanceMatrix(hy, hx)
            # print(f'for {hy} {hx}')
            # print(houseMatrix)
            for i in range(m):
                for j in range(n):
                    if houseMatrix[i][j] < 0 or ans[i][j] < 0:
                        # print(f'unreachable at {i} {j}')
                        ans[i][j] = -1
                    else:
                        ans[i][j] += houseMatrix[i][j]

        # print(ans)
        minDistance = m * n * len(houses)
        for i in range(m):
            for j in range(n):
                if ans[i][j] > 0:
                    minDistance = min(minDistance, ans[i][j])

        return minDistance if minDistance < m * n * len(houses) else -1


    def test(self):
        print(self.shortestDistance([[1,0,2,0,1],[0,2,0,2,0],[0,0,0,0,0]]))