import collections
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)
        edges = {}
        degrees = {}
        for u, v in pairs:
            if u not in edges:
                edges[u] = collections.deque()
            edges[u].append(v)

            if u not in degrees:
                degrees[u] = [0, 0]
            if v not in degrees:
                degrees[v] = [0, 0]
            degrees[u] = [degrees[u][0], degrees[u][1]+1]
            degrees[v] = [degrees[v][0]+1, degrees[v][1]]

        startingPosition = pairs[0][0]
        for k, v in degrees.items():
            if v[0] < v[1]:
                # in degree < out degree:
                startingPosition = k

        print(f'starting with {startingPosition}')
        visited = [startingPosition]
        ans = []
        while True:
            if len(visited) == 0:
                break

            lastItem = visited[-1]
            if lastItem not in edges or len(edges[lastItem]) == 0:
                # no more edges
                ans.append(lastItem)
                visited.pop()
                continue
            
            nextItem = edges[lastItem].popleft()
            visited.append(nextItem)

        ans2 = []
        for i in range(len(ans)-1, 0, -1):
            ans2.append([ans[i], ans[i-1]])

        return ans2

    def test(self):
        print(self.validArrangement([[5,1],[4,5],[11,9],[9,4]]))